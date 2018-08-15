from main_classes import *
from os import path
from util import *

numberOfRaces = 4


reglist = []
racelist = []
for i in range(1, numberOfRaces + 1):
    if i == 2 or i == 3:
        continue

    registrationsFromResults(infile = './results/seemoc{0}.csv'.format(i), outfile = './registrations/registrations_seemoc{0}.csv'.format(i), clubType = 'country')
    reglist.append('./registrations/registrations_seemoc{0}.csv'.format(i))
    racelist.append({'resultloc': './results/seemoc{0}.csv'.format(i), 'name': 'seemoc{0}'.format(i)})
    if i == 4:
        racelist[-1]['type'] = 'relay'

registrations = Registrations(reglist=reglist)

races = Races('seemoc',
              raceslist= racelist,
              runners = registrations.runners,
              clubs = registrations.clubs,
              categories= registrations.categories,
              maxScoredRunners=2,
              maxScoredTeamsRelay=1,
              scoreFunction=pointsSEEOC,
              scoreFunctionRelay=pointsSEEOCRelay,
              clubType='country')

races.scoreRaces()

for name,club in races.clubs.clubs.items():
    print(name, club.getClubScore())

#races.saveResults('seemoc_2018.csv')