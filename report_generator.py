#!/usr/bin/env python3
import genomelink
import threading
import time
from requests_oauthlib import OAuth2Session
from urllib import parse
from selenium import webdriver
from bs4 import BeautifulSoup
import json
import random


driver = webdriver.Chrome()

# PHENOTYPES = {'trait': ['eye-color', 'beard-thickness', 'morning-person', 'weight',
#                          'bmi', 'red-hair', 'black-hair', 'motion-sickness', 'lobe-size',
#                          'handedness', 'longevity', 'skin-pigmentation',
#                          'male-pattern-baldness-aga', 'freckles'],
#               'personality': ['agreeableness', 'neuroticism', 'extraversion',
#                               'conscientiousness', 'openness', 'depression', 'anger',
#                               'reward-dependence', 'harm-avoidance', 'novelty-seeking'],
#               'food_and_nutrition': ['protein-intake', 'carbohydrate-intake',
#                                      'vitamin-a', 'vitamin-b12', 'vitamin-d', 'vitamin-e', 'folate',
#                                      'calcium', 'magnesium', 'phosphorus', 'iron',
#                                      'alpha-linolenic-acid', 'beta-carotene'],
#               'allergy': ['egg-allergy', 'peanuts-allergy', 'milk-allergy'],
#               'disease': ['lung-cancer', 'colorectal-cancer', 'gastric-cancer', 'breast-cancer',
#                           'liver-cancer', 'pancreatic-cancer', 'prostate-cancer', 'type-2-diabetes',
#                           'myocardial-infarction', 'nicotine-dependence']}
PHENOTYPES = {'trait': ['eye-color', 'beard-thickness', 'morning-person', 'weight',
                         'bmi', 'red-hair', 'black-hair', 'motion-sickness', 'lobe-size',
                         'handedness', 'longevity', 'skin-pigmentation',
                         'male-pattern-baldness-aga', 'freckles'],
              'personality': ['neuroticism', 'depression'],
              'food_and_nutrition': ['folate', 'calcium'],
              'allergy': ['egg-allergy', 'peanuts-allergy', 'milk-allergy'],
              'disease': ['lung-cancer', 'colorectal-cancer', 'prostate-cancer', 'type-2-diabetes',
                          'nicotine-dependence']}

def login():
    driver.get('https://genomelink.io/login/')
    time.sleep(1)
    driver.find_element_by_id('id_login').send_keys('mr3tiago')
    driver.find_element_by_id('id_password').send_keys('63baby2night_test')
    driver.find_element_by_xpath('/html/body/div[2]/div/form/button').click()


def threaded(fn):
    def wrapper(*args, **kwargs):
        thread = threading.Thread(target=fn, args=args, kwargs=kwargs)
        thread.start()
        return thread
    return wrapper


class UserProfile():
    def __init__(self, population_type, category):
        clientid = 'K2akFUb86npj5QDnommNDsCEw5QuIKqIYQ6Juf6X'
        callbackurl = 'http://127.0.0.1:5000/callback'
        scope = ''
        for phenotype in PHENOTYPES[category]:
            scope += 'report:{} '.format(phenotype)
        scope.rstrip()
        self.token = self.generate_token(clientid, callbackurl, scope.replace(' ', '%20'))
        self.population = population_type
        self.scores = {}
        threads = []
        for phenotype in PHENOTYPES[category]:
            threads.append(self.add_score(phenotype))
        for thread in threads:
            thread.join()


    def generate_token(self, clientid, callbackurl, scope):
        baseauthurl = 'https://genomelink.io/oauth/authorize?redirect_uri={}&client_id={}&response_type=code&scope={}'
        authurl = baseauthurl.format(callbackurl, clientid, scope.replace(' ', '%20'))
        driver.get(authurl)
        driver.find_element_by_xpath('//*[@id="authorizationForm"]/div/div/input[2]').click()
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        return json.loads(soup.find('body').text.replace("'", "\""))['access_token']


    def get_report(self, phenotype):
        '''Return a Report object for a given phenotype and population.'''
        try:
            return genomelink.Report.fetch(phenotype, self.population, token=self.token)
        except Exception as e:
            print(e)


    @threaded
    def add_score(self, phenotype):
        '''Add the score for a phenotypes to self.scores.'''
        report = self.get_report(phenotype)
        try:
            score = report.summary['score']
            if score is None:
                score = random.randint(0, 4)
            self.scores[phenotype] = score
        except KeyError:
            print(report._data)
        except AttributeError:
            print(phenotype)


if __name__ == '__main__':
    login()
    profile = UserProfile('european', 'disease')
    for key, val in profile.scores.items():
        print(key + ':', val)
    driver.close()
