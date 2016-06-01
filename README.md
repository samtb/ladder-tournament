# ladder-tournament
Simulation of a ladder tournament

optional arguments:
  -h, --help            show this help message and exit
  -v                    verbose (level1)
  -vv                   verbose (level2)
  -vvv                  verbose (level3)
  -p PLAYERS, --players PLAYERS
                        Number of players
  -r ROUNDS, --rounds ROUNDS
                        Number of rounds

Example default run: 
./ranking.py

******************************************************************

player1  -- Final strength:18  -- Final rank:1  -- # of times initiated challenges:1  -- Total rounds played:7  -- # of rounds ended in 1st place:6
player3  -- Final strength:31  -- Final rank:2  -- # of times initiated challenges:2  -- Total rounds played:10  -- # of rounds ended in 1st place:4
player5  -- Final strength:15  -- Final rank:3  -- # of times initiated challenges:3  -- Total rounds played:4  -- # of rounds ended in 1st place:0
player6  -- Final strength:15  -- Final rank:4  -- # of times initiated challenges:2  -- Total rounds played:4  -- # of rounds ended in 1st place:0
player8  -- Final strength:16  -- Final rank:5  -- # of times initiated challenges:5  -- Total rounds played:5  -- # of rounds ended in 1st place:0
player4  -- Final strength:5  -- Final rank:6  -- # of times initiated challenges:3  -- Total rounds played:4  -- # of rounds ended in 1st place:0
player7  -- Final strength:4  -- Final rank:7  -- # of times initiated challenges:3  -- Total rounds played:3  -- # of rounds ended in 1st place:0
player2  -- Final strength:4  -- Final rank:8  -- # of times initiated challenges:1  -- Total rounds played:3  -- # of rounds ended in 1st place:0


Example run with 10 'players' and 100000 total 'games':
./ranking.py -p 10 -r 10000 -v

******************************************************************

player1  -- Final strength:7527  -- Final rank:1  -- # of times initiated challenges:957  -- Total rounds played:2186  -- # of rounds ended in 1st place:1038
player9  -- Final strength:6791  -- Final rank:2  -- # of times initiated challenges:1001  -- Total rounds played:1990  -- # of rounds ended in 1st place:758
player7  -- Final strength:7218  -- Final rank:3  -- # of times initiated challenges:1012  -- Total rounds played:2067  -- # of rounds ended in 1st place:857
player5  -- Final strength:4428  -- Final rank:4  -- # of times initiated challenges:1094  -- Total rounds played:1607  -- # of rounds ended in 1st place:326
player6  -- Final strength:7390  -- Final rank:5  -- # of times initiated challenges:938  -- Total rounds played:2139  -- # of rounds ended in 1st place:1009
player4  -- Final strength:6818  -- Final rank:6  -- # of times initiated challenges:973  -- Total rounds played:1987  -- # of rounds ended in 1st place:795
player10  -- Final strength:7141  -- Final rank:7  -- # of times initiated challenges:950  -- Total rounds played:2050  -- # of rounds ended in 1st place:899
player3  -- Final strength:6596  -- Final rank:8  -- # of times initiated challenges:1006  -- Total rounds played:1915  -- # of rounds ended in 1st place:692
player8  -- Final strength:6427  -- Final rank:9  -- # of times initiated challenges:1045  -- Total rounds played:1906  -- # of rounds ended in 1st place:637
player2  -- Final strength:7524  -- Final rank:10  -- # of times initiated challenges:1024  -- Total rounds played:2153  -- # of rounds ended in 1st place:922


******************************************************************

Ladder Competition Simulation Summary

Rules:
The game is played over 10000 rounds.
A random challenger is chosen each round.
Challengers can only challenge players ranked higher than them (first place player can't challenge anyone).
A challenger may not challenge the same defender two times in a row.
If a challenger defeats a defender, they swap ranks (ties go to the defender).
Both players roll a 10 sided die (0-9) then multiply that value by their current strength value to determine their fight value.
Challenger gains 10 strength for winning.
Both challenger and defender always gain 1 strength for match participation.


