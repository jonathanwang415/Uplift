#!/usr/bin/env python3
import MySQLdb as mdb
from collections import OrderedDict
from selenium import webdriver
from report_generator import PHENOTYPES, UserProfile, login, driver


def user_exists(phone_number, cursor):
    query = 'SELECT * FROM users WHERE phone_number={}'.format(phone_number)
    cursor.execute(query)
    user = cursor.fetchone()
    if user:
        return True
    else:
        return False


def add_user(phone_number, name, cursor):
    if not user_exists(phone_number, cursor):
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


def set_user_state(phone_number, state, cursor):
    query = 'UPDATE users SET state={} WHERE phone_number={};'.format(str(state), phone_number)
    cursor.execute(query)


def get_user_state(phone_number, cursor):
    query = 'SELECT state FROM users WHERE phone_number={};'.format(phone_number)
    cursor.execute(query)
    return cursor.fetchone()[0]


def get_scores(phone_number, phenotypes, cursor):
    scores = {}
    for phenotype in phenotypes:
        score = get_score(phone_number, phenotype, cursor)
        for key, value in score.items():
            scores[key] = value
    return scores


def get_score(phone_number, phenotype, cursor):
    query = 'SELECT {} FROM scores WHERE phone_number={};'.format(phenotype.replace('-', '_'), phone_number)
    cursor.execute(query)
    result = cursor.fetchone()[0]
    return {phenotype: result}


def get_suggestions(phone_number, phenotype, cursor):
    query = ''


if __name__ == '__main__':
    login()
    try:
        with mdb.connect('localhost', 'root', 'toor', 'userdb') as cur:
            add_user('+17146235999', 'Patrick Woo-Sam', cur)
            set_user_state('+17146235999', 0, cur)
            get_user_state('+17146235999', cur)
            egg_allergy_score = get_score('+17146235999', 'egg-allergy', cur)
            disease_scores = get_scores('+17146235999', PHENOTYPES['disease'], cur)
    except Exception as err:
        print(err)
    finally:
        driver.close()
