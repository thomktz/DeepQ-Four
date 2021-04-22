# %%
from environment import Board
import numpy as np
import torch
import torch.nn as nn
import torch.nn.functional as F

hidden_size = 128
population_size = 50
n_matchs = 10

class Player(nn.Module):
    def __init__(self):
        super(Player, self).__init__()
        self.fc1 = nn.Linear(6*7, hidden_size)
        self.fc2 = nn.Linear(hidden_size, hidden_size)
        self.fc3 = nn.Linear(hidden_size, 7)
    
    def forward(self, x):
        x = torch.Tensor(x.reshape(1, -1))
        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        x = F.relu(self.fc3(x))
        return x

def game(player0, player1):
    b = Board()
    while not b.over:
        #print(b)
        move0 = int(torch.argmax(player0(b.mat)))
        b.add_piece(0, move0)
        if b.over:
            break
        move1 = int(torch.argmax(player1(b.mat)))
        b.add_piece(1, move0)
    return b.winner
# %%

def evolution(n_epochs):
    population = [Player() for i in range(population_size)]
    for n in range(n_epochs):
        matchs = np.zeros((population_size, population_size))
        for i in range(population_size):
            print("player ", i)
            for j in range(i):
                for k in range(n_matchs//2):
                    matchs[i,j] += game(population[i], population[j]) # matchs[i,j] = # of victories of j over i (can be < 0)
                    matchs[i,j] -= game(population[j], population[i]) # 
                matchs[j,i] = - matchs[i,j]
        print(matchs)
        break
    
        


# %%
