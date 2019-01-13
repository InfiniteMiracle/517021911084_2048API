from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten, Conv2D, MaxPooling2D
from .game import Game
from .board import NB_board
from keras.models import load_model
       
class the_model_512:
    def __init__(self):
        self.model=load_model('./game2048/final.h5')
    def predict(self,board):
        Real_board = NB_board(board)
        direction = self.model.predict(Real_board)
        move = direction.argmax()
        return move