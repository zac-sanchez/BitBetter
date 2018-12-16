# Initial Setup:
Able to read in a .csv file or similar format of EPL games into a pandas table and pickle it for later.

# Phase 1:

Build a basic set of functions:
- Form of teams in a fixture 
- Likely goalscorers for each team
- Anecdotal goals conceded vs goals scored in a fixture
- Likelihood of each team scoring
- Anecdotal final outcomes

#Phase 2:

Add a feature to read in a team sheet and adjust predictions.

This involves tracking the form of each player, both on a fixture level and on a recent form level.
Hence the system must store a database for the players.

Goals:

- Store two databases: one for the team and one for the players.

Add in the following functions:
- Form of player recently.
- Form of player vs certain team.

Difficulties:
- Very hard to accurately determine whether a player is good if they debut for first time in EPL.
For example, if Messi joined the premier league, you would expect any team to perform better.
If you document this according to transfer fee, you get the issue of the player being a flop,
or perhaps the player is good but comes on a free transfer.

You could instead prioritise on wage, however wage statistics are sparse.

#Phase 3:

Web interface:

Would be nice to learn how to build a nice web interface that serves out the statistics.

#Phase 4:

Advanced Statistics:

One thing the above stats don't tell us is whose fault it was at any point in time for performance.

It is often true that player mismatches on the pitch can decide games. Slow defender vs fast winger etc.
We could perhaps store data that tracks who scored and detract points from the player on the other team in the same position.

E.g if the RW of Team A scores, detract from the LB of Team B.

Issue: how do you deal with multiple formations?

More to come.

#Phase 5:

Machine Learning:

Way down the track when we are sure the interface works nicely, we can use it to perhaps build a neural network or ML system that can learn outcomes.











