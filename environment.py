# %%
import numpy as np

dirs = [np.array([1,0]), np.array([1,1]), np.array([0,1])]

def all_same(list, mat):
    (a0, a1), (b0,b1), (c0,c1), (d0,d1) = list
    return (mat[a0, a1] == mat[b0,b1] == mat[c0, c1] == mat[d0,d1])

class Board():
    def __init__(self, x = 7, y = 6):
        self.width = x
        self.height = y
        self.pieces = [[], []]
        self.mat = np.zeros((self.height, self.width))
        self.over = False
        self.winner = None
        self.n_pieces = 0

    def add_piece(self, player, j):
        i0 = 0
        while i0 < self.height and self.mat[i0, j] != 0:
            #print(i0, j)
            i0 += 1
        if i0 >= self.height:
            self.over = True
            self.winner = 1 - player
            return False
        if self.n_pieces == self.height * self.width:
            self.over = True
            self.winner = None
        else:
            self.pieces[player].append((i0,j))
            self.mat[i0,j] += player * 2 - 1
            self.n_pieces += 1
            return self.is_won(player, i0, j)

    def is_won(self, player, i, j):
        check = []
        for dir in dirs:
            for k in range(4):
                try:
                    if all_same([np.array([i,j]) - k * dir + l * dir  for l in range(4)], self.mat):
                        self.over = True
                        self.winner = player
                        return True
                except Exception as e:
                    #print(e)
                    pass
        return False

    def __str__(self):
        string = ""
        for i in range(self.height):
            string += "|"
            for j in range(self.width):
                if self.mat[self.height - 1 -i, j] == -1:
                    string += "x"
                elif self.mat[self.height - 1 -i, j] == 1:
                    string += "o"
                else:
                    string += "-"
            string += "|\n"
        return string
# %%
