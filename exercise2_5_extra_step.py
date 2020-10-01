import numpy as np
import matplotlib.pyplot as plt

average_reward = []
percent_optimal = []
total_reward = 0.0
total_optimal = 0
curr_step = 0

def main():
    # change this for testing
    total_runs = 200
    total_steps = 10000
    num_bandits = 10
    epsilon = 0.1
    std = 0.01

    global average_reward
    global percent_optimal
    global total_reward
    global total_optimal
    global curr_step

    for i in range (0, total_runs):

        print("RUN: ", i)
        
        # reset global variables after each run
        average_reward.append([])
        percent_optimal.append([])
        total_reward = 0.0
        total_optimal = 0
        curr_step = 0

        # init 10 bandits
        bandits = []
        for j in range(0, num_bandits):
            bandits.append(Bandit(0.0, std, 0, 5.0, 0.0))


        for j in range(0, total_steps):
            # default values:
            action_index = 0
            action_bandit = bandits[0]

            greedy = np.random.choice([True, False], None, False, [1 - epsilon, epsilon])

            if greedy:
                max = bandits[0].curr_q
                max_indices = [0]
                for k in range(1, num_bandits):
                    if bandits[k].curr_q > max:
                        max = bandits[k].curr_q
                        max_indices.clear()
                        max_indices.append(k)
                    elif bandits[k].curr_q == max:
                        max_indices.append(k)
                
                # randomly chooses one between the equal maxes
                action_index = np.random.choice(max_indices, None, False, None)

            else:
                #randomly choose a bandit
                action_index = np.random.choice([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], None, False, None)

            # get the bandit at index and pull it
            action_bandit = bandits[action_index]
            bandits[action_index] = action_bandit.pull_arm(i)

            # update number of times optimal choice was chosen
            max_mean = bandits[0].mean
            for bandit in bandits:
                if bandit.mean > max_mean:
                    max_mean = bandit.mean

            if bandits[action_index].mean == max_mean:
                total_optimal += 1
            percent_optimal[i].append(total_optimal / float(total_steps))
            
            bandits = random_walk_gradual(bandits)

    plot_figures(total_runs, total_steps)

# makes the plots for average reward and percent optimal action at
# the end of the runs
def plot_figures(total_runs, total_steps):
    global average_reward
    global percent_optimal

    avg_reward_averages = []
    avg_percent_optimal = []

    for i in range(0, total_steps):
        sum_reward = 0
        sum_percent = 0
        for j in range(0, total_runs):
            sum_reward += average_reward[j][i]
            sum_percent += percent_optimal[j][i]
        
        avg_reward_averages.append(sum_reward / total_runs)
        avg_percent_optimal.append(sum_percent / total_runs)

    np.savetxt("sample_avg_reward_optimistic_step.csv", avg_reward_averages, delimiter=",")
    np.savetxt("sample_avg_percent_optimistic_step.csv", avg_percent_optimal, delimiter=",")

    plt.figure(0)
    plt.plot(avg_reward_averages)
    plt.xlabel('Steps')
    plt.ylabel('Average Reward')

    plt.figure(1)
    plt.plot(avg_percent_optimal)
    plt.xlabel('Steps')
    plt.ylabel('Percent Optimal Action')

    plt.show()

# updates the mean with a normally distributed increment with mean = 0
# and std = 0.01
def random_walk_gradual(bandits):
    for bandit in bandits:
        bandit.mean += np.random.normal(0, 0.01, 1)[0]
    return bandits

# updates the mean with a normally distributed increment with mean = 0
# and std = 0.1
def random_walk_sudden(bandits):
    for bandit in bandits:
        bandit.mean += np.random.normal(0, 0.1, 1)[0]
    return bandits

class Bandit:
    def __init__(self, mean, std, times_picked, curr_q, total_reward):
        self.mean = mean
        self.std = std
        self.times_picked = times_picked
        self.curr_q = curr_q
        self.total_reward = total_reward

    def pull_arm(self, curr_run):
        reward = np.random.normal(self.mean, self.std, 1)[0]
        self.times_picked += 1
        self.total_reward += reward
        self.curr_q = self.constant_step_size_param(reward)
        # self.curr_q = self.sample_average(reward)

        global total_reward
        global curr_step
        global average_reward
        
        total_reward += reward
        curr_step += 1
        average_reward[curr_run].append(total_reward / curr_step)

        return self
    
    # incrementally computed
    def sample_average(self, reward):
        return (self.curr_q + (1.0 / self.times_picked) * (reward - self.curr_q))

    def constant_step_size_param(self, reward):
        return (self.curr_q + (0.1) * (reward - self.curr_q))


if __name__ == "__main__":
    main()