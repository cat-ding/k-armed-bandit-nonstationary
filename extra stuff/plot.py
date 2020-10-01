import matplotlib.pyplot as plt
import csv

# just sample avg vs step size with gradual changes
sample_avg_reward = []
step_size_reward = []
sample_avg_percent = []
step_size_percent = []

with open('sample_avg_reward.csv','r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        sample_avg_reward.append(float(row[0]))

with open('step_size_reward.csv','r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        step_size_reward.append(float(row[0]))

with open('sample_avg_percent.csv','r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        sample_avg_percent.append(float(row[0]) * 100)

with open('step_size_percent.csv','r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        step_size_percent.append(float(row[0]) * 100)

x = list(range(0, 10000))

plt.figure(0)
plt.plot(x, sample_avg_reward, label='Sample-average, std = 0.01')
plt.plot(x, step_size_reward, label='Constant step-size parameter, std = 0.01')
plt.xlabel('Steps')
plt.ylabel('Average Reward')
plt.legend()

plt.figure(1)
plt.plot(x, sample_avg_percent, label='Sample-average, std = 0.01')
plt.plot(x, step_size_percent, label='Constant step-size parameter, std = 0.01')
plt.xlabel('Steps')
plt.ylabel('% Optimal Action')
plt.legend()

plt.show()