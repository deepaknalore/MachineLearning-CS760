import random
import math

table = [[0,0],[0,0]]
current_state = 0 # 0- A 1 - B
action = 0 # 1 - Stay, 0 - Move
actions = [0,1]

alpha = 0.5
gamma = 0.9

def transition():
    global current_state
    global action
    next_action = random.choices(actions)[0]
    if next_action == 0:
        next_state = ((current_state+1)%2)
        r = 0
    else:
        next_state = current_state
        r = 1
    table[next_action][current_state] = (1 - alpha) * table[next_action][current_state] + alpha*(r + gamma*max(table[0][next_state], table[1][next_state]))

    current_state = next_state
    action = next_action

for i in range(200):
    transition()

print(table)