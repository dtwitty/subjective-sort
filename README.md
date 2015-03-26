# subjective-sort
Utility for ranking items using heuristics on pairwise preferences. Originally developed to sort the 
coursework on my resume in order of importance/impressiveness. 

Current algorithm (which does not yet have a main method) is as follows:
  1. Ask the user for some number of randomized questions of the form "which is better: this or that" until
     some connectivity criterion is reached.
  2. Try to perform a topological sort on these preferences.
  3. If this fails, use a heuristic solver for Feedback Arc Set to remove all cycles from the graph and try again.
  
As it stands currently, the algorithm itself has been implemented, but there is no UI. A stopping heuristic for asking
questions also needs to be implemented, as asking for all pairs of items becomes tedious even for small numbers of itemss.
