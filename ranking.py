#!/usr/bin/env python

import random
import argparse
parser = argparse.ArgumentParser(description="description")
parser.add_argument("-v", action="store_true", help="verbose (level1)")
parser.add_argument("-vv", action="store_true", help="verbose (level2)")
parser.add_argument("-vvv", action="store_true", help="verbose (level3)")
parser.add_argument('-p', '--players', type=int, help='Number of players', required=False)
parser.add_argument('-r', '--rounds', type=int, help='Number of rounds', required=False)
args = parser.parse_args()

if args.players == None:
    numPlayers = 8
else:
    numPlayers = args.players

verbose1 = False
verbose2 = False
verbose3 = False

if args.rounds == None:
    rounds = 20
else:
    rounds = args.rounds


if args.v == True:
    verbose1 = True
if args.vv == True:
    verbose1 = True
    verbose2 = True
if args.vvv == True:
    verbose1 = True
    verbose2 = True
    verbose3 = True

# players = [
#     {'name': 'player1', 'rank': 1, 'strength': 1, 'challenges': 0, 'lastchallenge': 'none', 'totalnumgames': 0, 'firstplacestreak': 0},
#     {'name': 'player2', 'rank': 2, 'strength': 1, 'challenges': 0, 'lastchallenge': 'none', 'totalnumgames': 0, 'firstplacestreak': 0},
#     {'name': 'player3', 'rank': 3, 'strength': 1, 'challenges': 0, 'lastchallenge': 'none', 'totalnumgames': 0, 'firstplacestreak': 0},
# ]

# playerRankHistory = [
#     {'name': 'player1', 'rank': [1]},
#     {'name': 'player2', 'rank': [2]},
#     {'name': 'player3', 'rank': [3]}   
# ]

# playerList = ['player1','player2','player3']

dieRoll = range(0,10)
numberOfchallenges=rounds
winbonus=10
playbonus=1

def build_player(id):
  return {
    'name':'player{}'.format(id),
    'rank': id,
    'strength': 1,
    'challenges': 0,
    'lastchallenge': 'none',
    'totalnumgames': 0,
    'firstplacestreak': 0
  }

def generatePlayers(numberOfPlayers):
    return [build_player(x) for x in range(1, numberOfPlayers + 1)]


def generatePlayerList():
    plist = []
    for i in players:
        plist.append(i['name'])
    return plist

def build_rank_history(id):
    return{
    'name': 'player{}'.format(id),
    'rank': [id]
    }

def generatePlayerRankHistory(numberOfPlayers):
    return [build_rank_history(x) for x in range(1, numberOfPlayers + 1)]

def getName(name):
    for p in players:
        if p['name'] == name:
            return p['name']

def getRank(name):
    for p in players:
        if p['name'] == name:
            return p['rank']

def updateRank(name,newRank):
    for p in players:
        if p['name'] == name:
            p['rank'] = newRank

def updateLastChallenge(name,challenged):
    for p in players:
        if p['name'] == name:
            p['lastchallenge'] = challenged

def getLastChallenge(name):
    for p in players:
        if p['name'] == name:
            return p['lastchallenge']

def updatePlayerRankHistory(name):
    for p in playerRankHistory:
        if p['name'] == name:
            myRank=getRank(name)
            p['rank'].append(myRank)

def getPlayerRankHistory(name):
    for p in playerRankHistory:
        if p['name'] == name:
            return p['rank']

def updatechallenges(name):
    for p in players:
        if p['name'] == name:
            p['challenges'] = p['challenges']+1

def getchallenges(name):
    for p in players:
        if p['name'] == name:
            return p['challenges']

def updatetotalnumgames(name):
    for p in players:
        if p['name'] == name:
            p['totalnumgames'] = p['totalnumgames']+1

def gettotalnumgames(name):
    for p in players:
        if p['name'] == name:
            return p['totalnumgames']

def getFirstPlaceStreak(name):
    for p in players:
        if p['name'] == name:
            return p['firstplacestreak']

def updateFirstPlaceStreak(name):
    for p in players:
        if p['name'] == name:
            p['firstplacestreak'] = p['firstplacestreak']+1

def getStrength(name):
    for p in players:
        if p['name'] == name:
            return p['strength']

def updateStrength(name,newStrength):
    for p in players:
        if p['name'] == name:
            p['strength'] = newStrength

def getNextStrongest(name):
    listOfBeefcakes = []
    myStrength = 1
    for p in players:
        if p['rank'] == 1:
            numberone = p['name']
    myStrength = getStrength(name)
    for p in players:
        if p['strength'] > myStrength:
            listOfBeefcakes.append(p['name'])
    if listOfBeefcakes != []:
        return sorted(listOfBeefcakes)[0]
    else:
        return numberone

def getPlayerOfRank(rank):
    for p in players:
        if p['rank'] == rank:
            return p['name']


def fight(ch,de):
    challengerRoll = random.choice(dieRoll)
    defenderRoll = random.choice(dieRoll)
    challengerStrength = getStrength(ch)
    defenderStrength = getStrength(de)
    challengerScore = challengerStrength*challengerRoll
    defenderScore = defenderStrength*defenderRoll
    if challengerScore > defenderScore:
        winner = ch
    else:
        winner = de
    results = [winner,challengerRoll,defenderRoll,challengerScore,defenderScore]
    return results

def make_an_attempt(challenge,defend):
    # print "--------------------"
    # print challenge,"vs.",defend
    challenger = getName(challenge)
    defender = getName(defend)
    challengerRank = getRank(challenger)
    defenderRank = getRank(defender)
    challengerStartStrength = getStrength(challenger)
    defenderStartStrength = getStrength(defender)

    challengeResults = fight(challenger,defender)
    winner = challengeResults[0]
    challengerRoll = challengeResults[1]
    defenderRoll = challengeResults[2]
    challengerScore = challengeResults[3]
    defenderScore = challengeResults[4]

    if verbose3 == True:
        print "--------------------"
        print challenger+"(rank "+str(challengerRank)+") vs.",defender+"(rank "+str(defenderRank)+")"
    if winner == challenger:
        newChallengerStrength = getStrength(challenger)+winbonus
        updateStrength(challenger,newChallengerStrength)
        updateRank(challenger,defenderRank)
        updateRank(defender,challengerRank)
        if verbose3 == True:
            print "CHALLENGER WON"
            print challenger,"won with a score of",challengerScore
            print defender,"lost with a score of",defenderScore
            print challenger+"'s strength is now",getStrength(challenger)
            print challenger+"'s rank was",challengerRank,"but is now",getRank(challenger)
    else:
        if verbose3 == True:
            print "DEFENDER WON"
            print defender,"won with a score of",defenderScore
            print challenger,"lost with a score of",challengerScore
            print defender+"'s strength is now",getStrength(defender)
    if verbose3 == True:
        print "defender strength was",defenderStartStrength,"and is now",getStrength(defender)
        print "challenger strength was",challengerStartStrength,"and is now",getStrength(challenger)
    post_game_updates(challenger,defender)

def post_game_updates(challenger,defender):
    newDefenderStrength = getStrength(defender)+playbonus # everyone gets stronger no matter what
    newChallengerStrength = getStrength(challenger)+playbonus # everyone gets stronger no matter what
    updateStrength(defender,newDefenderStrength)
    updateStrength(challenger,newChallengerStrength)
    updatechallenges(challenger)
    updateLastChallenge(challenger,defender)
    updatetotalnumgames(challenger)
    updatetotalnumgames(defender)
    finalchallengerRank = getRank(challenger)
    finaldefenderRank = getRank(defender)
    if finalchallengerRank == 1:
        updateFirstPlaceStreak(challenger)
    if finaldefenderRank == 1:
        updateFirstPlaceStreak(defender)
    updatePlayerRankHistory(challenger)
    updatePlayerRankHistory(defender)

# This is standard ladder challenge rules
def ladder_challenge_rules(c,d):
    while getRank(c) < getRank(d) or d == c or getLastChallenge(c) == d: 
        c = random.choice(playerList)
        d = random.choice(playerList)
    vettedChallenge = [c,d]
    return vettedChallenge

# This is a basic ladder challenge, but challengers always gun for first if they can
def challenge_numero_uno(c,d):
    d =  getPlayerOfRank(1)
    while getRank(c) < getRank(d) or d == c or getLastChallenge(c) == d: 
        c = random.choice(playerList)
        d = random.choice(playerList)
    vettedChallenge = [c,d]
    return vettedChallenge

# This ladder allows rematches back-to-back
def looser_ladder(c,d):
    while getRank(c) < getRank(d) or d == c: 
        c = random.choice(playerList)
        d = random.choice(playerList)
    vettedChallenge = [c,d]
    return vettedChallenge

# This allows anyone to challenge anyone regardless of rank
def wild_west(c,d):
    whocares = [c,d]
    return whocares

# This forces players to challenge only directly above them, no jumping
def next_best(c,d):
    d = getNextStrongest(c)
    chosen = [c,d]
    return chosen

def initiate():
    c = random.choice(playerList)
    d = random.choice(playerList)
    while c == d or getRank(c) == 1:
        c = random.choice(playerList)
    # validPlayer = ladder_challenge_rules(c,d)
    validPlayer = challenge_numero_uno(c,d)
    # validPlayer = looser_ladder(c,d)
    # validPlayer = wild_west(c,d)
    # validPlayer = next_best(c,d)
    make_an_attempt(validPlayer[0],validPlayer[1])


#initialize players
players = generatePlayers(numPlayers)
playerList = generatePlayerList()
playerRankHistory = generatePlayerRankHistory(numPlayers)

for _ in range(numberOfchallenges):
    initiate()


if verbose2 == True:
    print "******************************************************************"
    print " "
    print "Ranking history:"
    toprank = 1
    while toprank != 9:
        for player in playerList:
            pname = getName(player)
            prank = getRank(player)
            rankhistory = getPlayerRankHistory(player)
            if prank == toprank:
                print pname+":",rankhistory
        toprank+=1
    print " "

# newlist = sorted(players, key=lambda k: k['rank']) 

print " "
print "******************************************************************"
print " "
toprank = 1
while toprank < numPlayers+1:
    for item in playerList:
        pname = getName(item)
        pstr = getStrength(item)
        prank = getRank(item)
        pchallenges = getchallenges(item)
        plc = getLastChallenge(item)
        tot = gettotalnumgames(item)
        firsts = getFirstPlaceStreak(item)
        if prank == toprank:
            print pname," -- Final strength:"+str(pstr)," -- Final rank:"+str(prank)," -- # of times initiated challenges:"+str(pchallenges)," -- Total rounds played:"+str(tot)," -- # of rounds ended in 1st place:"+str(firsts)
    toprank+=1
print " "

if verbose1 == True:
    print " "
    print "******************************************************************"
    print " "
    print "Ladder Competition Simulation Summary"
    print " "
    print "Rules:"
    print "The game is played over",numberOfchallenges,"rounds."
    print "A random challenger is chosen each round."
    print "Challengers can only challenge players ranked higher than them (first place player can't challenge anyone)."
    print "A challenger may not challenge the same defender two times in a row."
    print "If a challenger defeats a defender, they swap ranks (ties go to the defender)."
    print "Both players roll a",len(dieRoll),"sided die ("+str(dieRoll[0])+"-"+str(dieRoll[-1])+") then multiply that value by their current strength value to determine their fight value."
    print "Challenger gains",winbonus,"strength for winning."
    print "Both challenger and defender always gain",playbonus,"strength for match participation."
    print " "

