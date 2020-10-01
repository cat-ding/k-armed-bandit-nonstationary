import matplotlib.pyplot as plt
import csv

sample_avg_reward = []
sample_avg_reward_sudden = []
sample_avg_percent = []
sample_avg_percent_sudden = []

step_size_reward = []
step_size_reward_sudden = []
step_size_percent = []
step_size_percent_sudden = []

#avg rewards:
with open('sample_avg_reward.csv','r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        sample_avg_reward.append(float(row[0]))

with open('sample_avg_reward_sudden.csv','r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        sample_avg_reward_sudden.append(float(row[0]))
        
with open('step_size_reward.csv','r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        step_size_reward.append(float(row[0]))

with open('step_size_reward_sudden.csv','r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        step_size_reward_sudden.append(float(row[0]))

#percent optimal actions:
with open('sample_avg_percent.csv','r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        sample_avg_percent.append(float(row[0]) * 100)

with open('sample_avg_percent_sudden.csv','r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        sample_avg_percent_sudden.append(float(row[0]) * 100)

with open('step_size_percent.csv','r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        step_size_percent.append(float(row[0]) * 100)

with open('step_size_percent_sudden.csv','r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        step_size_percent_sudden.append(float(row[0]) * 100)


x = list(range(0, 10000))

plt.figure(0)
plt.plot(x, sample_avg_reward, label='Sample-average, std = 0.01')
plt.plot(x, sample_avg_reward_sudden, label='Sample-average, std = 0.1')
plt.plot(x, step_size_reward, label='Constant step-size parameter, std = 0.01')
plt.plot(x, step_size_reward_sudden, label='Constant step-size parameter, std = 0.1')
plt.xlabel('Steps')
plt.ylabel('Average Reward')
plt.legend()

plt.figure(1)
plt.plot(x, sample_avg_percent, label='Sample-average, std = 0.01')
plt.plot(x, sample_avg_percent_sudden, label='Sample-average, std = 0.1')
plt.plot(x, step_size_percent, label='Constant step-size parameter, std = 0.01')
plt.plot(x, step_size_percent_sudden, label='Constant step-size parameter, std = 0.1')
plt.xlabel('Steps')
plt.ylabel('% Optimal Action')
plt.legend()

plt.show()