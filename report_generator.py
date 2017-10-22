#!/usr/bin/env python3
import genomelink

PHENOTYPES = {'traits': ['eye-color', 'beard-thickness', 'morning-person', 'weight',
                         'bmi', 'red-hair', 'black-hair', 'motion-sickness', 'lobe-size',
                         'handedness', 'longevity', 'skin-pigmentation',
                         'male-pattern-baldness-aga', 'freckles'],
              'personality': ['agreeableness', 'neuroticism', 'extraversion',
                              'conscientiousness', 'openness', 'depression', 'anger',
                              'reward-dependence', 'harm-avoidance', 'gambling',
                              'novelty-seeking'],
              'food_and_nutrition': ['protein-intake', 'carbohydrate-intake', 'bitter-taste',
                                     'vitamin-a', 'vitamin-b12', 'vitamin-d', 'vitamin-e', 'folate',
                                     'calcium', 'magnesium', 'phosphorus', 'iron',
                                     'alpha-linolenic-acid', 'beta-carotene'],
              'allergies': ['egg-allergy', 'peanuts-allergy', 'milk-allergy'],
              'disease': ['lung-cancer', 'colorectal-cancer', 'gastric-cancer', 'breast-cancer',
                          'liver-cancer', 'pancreatic-cancer', 'prostate-cancer', 'type-2-diabetes',
                          'myocardial-infarction', 'nicotine-dependence', 'smoking-behavior']}


class UserProfile():
    def __init__(self, population_type, interest, token=None):
        if token is None:
            self.token = 'GENOMELINKTEST'
        else:
            self.token = token

        self.population = population_type
        self.scores = self.get_scores(phenotypes=PHENOTYPES[interest])

    def get_report(self, phenotype):
        '''Return a Report object for a given phenotype and population.'''
        return genomelink.Report.fetch(phenotype, self.population, token=self.token)

    def get_scores(self, phenotypes=None):
        '''Get the scores for phenotypes.'''
        if phenotypes is None:
            phenotypes = []
        scores = {}
        if phenotypes:
            for phenotype in phenotypes:
                report = self.get_report(phenotype)
                try:
                    scores[phenotype] = report.summary['score']
                except KeyError:
                    continue
        return scores


if __name__ == '__main__':
    profile = UserProfile('european', 'personality')
    for key, val in profile.scores.items():
        print(key + ':', val)
