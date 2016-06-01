# ladder-tournament
Simulation of a ladder tournament<br />
<br />
optional arguments:<br />
  -h, --help            show this help message and exit<br />
  -v                    verbose (level1)<br />
  -vv                   verbose (level2)<br />
  -vvv                  verbose (level3)<br />
  -p  Number of players<br />
  -r Number of rounds<br />
<br />
<br />
Example default run: <br />
./ranking.py<br />
<br />
<br />
player1  -- Final strength:18  -- Final rank:1  -- # of times initiated challenges:1  -- Total rounds played:7  -- # of rounds ended in 1st place:6<br />
player3  -- Final strength:31  -- Final rank:2  -- # of times initiated challenges:2  -- Total rounds played:10  -- # of rounds ended in 1st place:4<br />
player5  -- Final strength:15  -- Final rank:3  -- # of times initiated challenges:3  -- Total rounds played:4  -- # of rounds ended in 1st place:0<br />
player6  -- Final strength:15  -- Final rank:4  -- # of times initiated challenges:2  -- Total rounds played:4  -- # of rounds ended in 1st place:0<br />
player8  -- Final strength:16  -- Final rank:5  -- # of times initiated challenges:5  -- Total rounds played:5  -- # of rounds ended in 1st place:0<br />
player4  -- Final strength:5  -- Final rank:6  -- # of times initiated challenges:3  -- Total rounds played:4  -- # of rounds ended in 1st place:0<br />
player7  -- Final strength:4  -- Final rank:7  -- # of times initiated challenges:3  -- Total rounds played:3  -- # of rounds ended in 1st place:0<br />
player2  -- Final strength:4  -- Final rank:8  -- # of times initiated challenges:1  -- Total rounds played:3  -- # of rounds ended in 1st place:0<br />
<br />
<br />
Example run with 10 'players' and 10000 total 'games':<br />
./ranking.py -p 10 -r 10000 -v<br />
<br />

player1  -- Final strength:7527  -- Final rank:1  -- # of times initiated challenges:957  -- Total rounds played:2186  -- # of rounds ended in 1st place:1038<br />
player9  -- Final strength:6791  -- Final rank:2  -- # of times initiated challenges:1001  -- Total rounds played:1990  -- # of rounds ended in 1st place:758<br />
player7  -- Final strength:7218  -- Final rank:3  -- # of times initiated challenges:1012  -- Total rounds played:2067  -- # of rounds ended in 1st place:857<br />
player5  -- Final strength:4428  -- Final rank:4  -- # of times initiated challenges:1094  -- Total rounds played:1607  -- # of rounds ended in 1st place:326<br />
player6  -- Final strength:7390  -- Final rank:5  -- # of times initiated challenges:938  -- Total rounds played:2139  -- # of rounds ended in 1st place:1009<br />
player4  -- Final strength:6818  -- Final rank:6  -- # of times initiated challenges:973  -- Total rounds played:1987  -- # of rounds ended in 1st place:795<br />
player10  -- Final strength:7141  -- Final rank:7  -- # of times initiated challenges:950  -- Total rounds played:2050  -- # of rounds ended in 1st place:899<br />
player3  -- Final strength:6596  -- Final rank:8  -- # of times initiated challenges:1006  -- Total rounds played:1915  -- # of rounds ended in 1st place:692<br />
player8  -- Final strength:6427  -- Final rank:9  -- # of times initiated challenges:1045  -- Total rounds played:1906  -- # of rounds ended in 1st place:637<br />
player2  -- Final strength:7524  -- Final rank:10  -- # of times initiated challenges:1024  -- Total rounds played:2153  -- # of rounds ended in 1st place:922<br />
<br />
<br />
Ladder Competition Simulation Summary<br />
<br />
Rules:<br />
The game is played over 10000 rounds.<br />
A random challenger is chosen each round.<br />
Challengers can only challenge players ranked higher than them (first place player can't challenge anyone).<br />
A challenger may not challenge the same defender two times in a row.<br />
If a challenger defeats a defender, they swap ranks (ties go to the defender).<br />
Both players roll a 10 sided die (0-9) then multiply that value by their current strength value to determine their fight value.<br />
Challenger gains 10 strength for winning.<br />
Both challenger and defender always gain 1 strength for match participation.<br />


<br />
