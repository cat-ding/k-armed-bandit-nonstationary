import matplotlib.pyplot as plt
import csv

sample_avg_reward_optimistic = []
sample_avg_percent_optimistic = []
sample_avg_reward_optimistic_step = []
sample_avg_percent_optimistic_step = []

#avg rewards:
with open('sample_avg_reward_optimistic.csv','r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        sample_avg_reward_optimistic.append(float(row[0]))

with open('sample_avg_percent_optimistic.csv','r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        sample_avg_percent_optimistic.append(float(row[0]))
        
with open('sample_avg_reward_optimistic_step.csv','r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        sample_avg_reward_optimistic_step.append(float(row[0]))

with open('sample_avg_percent_optimistic_step.csv','r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        sample_avg_percent_optimistic_step.append(float(row[0]))


x = list(range(0, 10000))

plt.figure(0)
plt.plot(x, sample_avg_reward_optimistic, label='Sample-average, optimistic')
plt.plot(x, sample_avg_reward_optimistic_step, label='Constant step-size parameter, optimistic')
plt.xlabel('Steps')
plt.ylabel('Average Reward')
plt.legend()

plt.figure(1)
plt.plot(x, sample_avg_percent_optimistic, label='Sample-average, optimistic')
plt.plot(x, sample_avg_percent_optimistic_step, label='Constant step-size parameter, optimistic')
plt.xlabel('Steps')
plt.ylabel('% Optimal Action')
plt.legend()

plt.show()