import numpy as np
from .game import Game

out_shape = (4,4)
CAND = 16
map_table = {2**i:i for i in range(1,CAND)}
map_table[0]=0

def NB_board(arr):
    ret = np.zeros(shape=out_shape+(CAND,),dtype=bool)
    for r in range (out_shape[0]):
        for c in range (out_shape[1]):
            ret[r,c,map_table[arr[r,c]]]=1
    ret=ret.reshape(1,4,4,16)
    return ret

