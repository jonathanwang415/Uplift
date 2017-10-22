#!/usr/bin/env python3
import MySQLdb as mdb
from collections import OrderedDict
from selenium import webdriver
from report_generator import PHENOTYPES, UserProfile, login, driver


def add_user(name, phone_number, cursor):
    query = 'SELECT * FROM users WHERE phone_number={}'.format(phone_number)
    cursor.execute(query)
    user = cursor.fetchone()
    if not user:
        scores = {}
        for category in ['personality', 'allergy', 'disease', 'food_and_nutrition']:
            for key, value in UserProfile('european', category).scores.items():
                scores[key] = value
        scores = OrderedDict(sorted(scores.items(), key=lambda t: t[0]))
        query = 'INSERT INTO scores VALUES(' + ', '.join([str(x) for x in scores.values()]) + ', {});'.format(phone_number)
        try:
            cursor.execute(query)
        except Exception as err:
            print(err)
        query = 'INSERT INTO users VALUES(\'{}\', {}, {});'.format(name, '0', phone_number)
        try:
            cursor.execute(query)
        except Exception as err:
            print(err)


if __name__ == '__main__':
    login()
    try:
        with mdb.connect('localhost', 'root', 'toor', 'userdb') as cur:
            add_user('Patrick Woo-Sam', '+17146235999', cur)
    except Exception as err:
        print(err)
    finally:
        driver.close()
