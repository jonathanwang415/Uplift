#!/usr/bin/env python3
import MySQLdb as mdb
from collections import OrderedDict
from selenium import webdriver
from report_generator import PHENOTYPES, UserProfile, login, driver

phenotypes = []
for category in ['trait', 'personality', 'allergy', 'disease', 'food_and_nutrition']:
    phenotypes += list(PHENOTYPES[category])
phenotypes.sort()


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
        for category in ['trait', 'personality', 'allergy', 'disease', 'food_and_nutrition']:
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
    state = cursor.fetchone()
    if state is not None:
        return state[0]
    else:
        return None


def set_user_name(phone_number, name, cursor):
    query = 'UPDATE users SET name=\'{}\' WHERE phone_number={};'.format(str(name), phone_number)
    cursor.execute(query)


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


def num_suggestions(phenotype, cursor):
    query = 'SELECT s_one, s_two, s_three, s_four FROM {} WHERE phenotype_name=\'' + phenotype.replace('-', '_') + '\';'
    if phenotype in PHENOTYPES['disease']:
        query = query.format('disease')
    elif phenotype in PHENOTYPES['food_and_nutrition']:
        query = query.format('foodnutrition')
    elif phenotype in PHENOTYPES['personality']:
        query = query.format('personality')
    else:
        return 0
    cursor.execute(query)
    sugestions = cursor.fetchone()
    if sugestions:
        return len(sugestions)
    else:
        return 0


def get_suggestions(phenotype, cursor):
    query = 'SELECT s_one, s_two, s_three, s_four FROM {} WHERE phenotype_name=\'' + phenotype.replace('-', '_') + '\';'
    if phenotype in PHENOTYPES['disease']:
        query = query.format('disease')
    elif phenotype in PHENOTYPES['food_and_nutrition']:
        query = query.format('foodnutrition')
    elif phenotype in PHENOTYPES['personality']:
        query = query.format('personality')
    else:
        return None
    cursor.execute(query)
    return cursor.fetchone()


if __name__ == '__main__':
    login()
    try:
        with mdb.connect('localhost', 'root', 'toor', 'userdb') as cur:
            add_user('+17146235999', 'Patrick Woo-Sam', cur)
            set_user_state('+17146235999', 2, cur)
            get_user_state('+17146235999', cur)
            egg_allergy_score = get_score('+17146235999', 'egg-allergy', cur)
            disease_scores = get_scores('+17146235999', PHENOTYPES['disease'], cur)
            for phenotype in phenotypes:
                if num_suggestions(phenotype, cur):
                    print(phenotype)
                    print(get_suggestions(phenotype, cur))
    except Exception as err:
        print(err)
    finally:
        driver.close()
