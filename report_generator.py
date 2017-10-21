#!/usr/bin/env python3
import genomelink

class UserProfile():
    def __init__(self, population_type, token=None):
        if token is None:
            self.token = 'GENOMELINKTEST'
        else:
            self.token = token
        phenotypes = ['agreeableness', 'neuroticism', 'extraversion', 'conscientiousness',
                      'openness', 'depression', 'anger', 'reward-dependence', 'harm-avoidance',
                      'gambling', 'novelty-seeking']
        self.population = population_type
        self.scores = self.get_scores(phenotypes=phenotypes)

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
    profile = UserProfile('european')
    print(profile.scores)
