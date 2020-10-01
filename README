README
Catherine Ding
COMP138 Programming Assignment #1
Exercise 2.5 from Reinforcement Learning: An Introduction by Sutton and Barto

Dependencies
- numpy
- matplotlib.pyplot
(both with python3)

Files Included:
exercise2_5.py/exercise2_5_step.py: these two files are essentially exact
    copies of each other, the only difference being that one uses the
    action-value method using sample averages and the other uses
    the method using a constant step-size parameter. Both contain code
    for the two methods, but one is commented out.
    - this code saves the averaged data for reward and percent optimal
      action over 2000 runs to a csv file which can then be displayed
      using plot_all.py
    - I manually went into the code and changed the random walks (and
      csv file names), so it may not be immediately obvious how the
      code runs both gradual and sudden random walks, because it doesn't.

plot_all.py: opens the csv data of averaged values of 2000 runs generated
    by the previous code and plots it on a graph with number of steps on
    the x-axes and either average reward or % optimal action on the y-axes

Instructions to Run:
- make sure python 3 is installed
- install the dependencies listed above
- run exercise2_5.py/exercise2_5_step.py with:
    "python3 exercise2_5.py" or
    "python3 exercise2_5_step.py"
- after csv files are generated run
    "python3 plot_all.py"