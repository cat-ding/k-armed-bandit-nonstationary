import matplotlib.pyplot as plt
import csv

testsamp1 = []
teststep1 = []
testsamp2 = []
teststep2 = []

testsamp1percent = []
teststep1percent = []
testsamp2percent = []
teststep2percent = []

#avg rewards:
with open('testsamp1.csv','r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        testsamp1.append(float(row[0]))
with open('teststep1.csv','r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        teststep1.append(float(row[0]))
with open('testsamp2.csv','r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        testsamp2.append(float(row[0]))
with open('teststep2.csv','r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        teststep2.append(float(row[0]))

#percent optimal actions:
with open('testsamp1percent.csv','r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        testsamp1percent.append(float(row[0]))
with open('teststep1percent.csv','r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        teststep1percent.append(float(row[0]))
with open('testsamp2percent.csv','r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        testsamp2percent.append(float(row[0]))
with open('teststep2percent.csv','r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        teststep2percent.append(float(row[0]))


x = list(range(0, 10000))

plt.figure(0)
plt.plot(x, testsamp1, label='Sample-average gradual')
plt.plot(x, teststep1, label='Constant step-size parameter gradual')
plt.plot(x, testsamp2, label='Sample-average sudden')
plt.plot(x, teststep2, label='Constant step-size parameter sudden')
plt.xlabel('Steps')
plt.ylabel('Average Reward')
plt.legend()

plt.figure(1)
plt.plot(x, testsamp1percent, label='Sample-average gradual')
plt.plot(x, teststep1percent, label='Constant step-size parameter gradual')
plt.plot(x, testsamp2percent, label='Sample-average sudden')
plt.plot(x, teststep2percent, label='Constant step-size parameter sudden')
plt.xlabel('Steps')
plt.ylabel('% Optimal Action')
plt.legend()

plt.show()