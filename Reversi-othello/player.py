import random
 
class MyPlayer:
    """Less is more"""
    def __init__(self, my_color, opponent_color):
        self.name = "hereldav"
        self.my_color = my_color
        self.opponent_color = opponent_color
 
         
    def move(self, board):
        direction = [[0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1]]
        remaining_moves=[]
        flip = 0
        maxi = -100
        mini = 10000
        me = MyPlayer
      
        for r in range(0, 8):
            for c in range(0,8):
                if (board[r][c] == -1):
                    remaining_moves.append(r)
                if (board[r][c]==self.my_color):  
                    for i in range(0, 8):
                        op_stone = me.opponents_stone(r, direction, c, board, i)
      
                        if (op_stone == self.opponent_color):       
                                counter = 1
                                counter2 = 0
                                while counter<9:
                                    counter = counter + 1
                                    counter2 = counter2 +1                        
                                    if me.possible_move(mini, r, c, counter, direction, i, counter2, self.my_color, maxi, flip, board):
  
                                        if (flip>maxi):
                                            maxi = flip
                                            e = r+ counter*direction[i][0]
                                            f = c + counter*direction[i][1]
                                            best_move = (e, f)
                                        if (mini>flip):
                                            mini = flip
                                            e1 = r+ counter*direction[i][0]
                                            f1 = c + counter*direction[i][1]
                                            worst_move = (e1, f1)
   
                                    elif me.not_possible_move(r, c, counter, direction, i, counter2, self.my_color, board):
                                        break
                                        
        if ((len(remaining_moves))> 43):                    
            return worst_move
        if ((len(remaining_moves))<44):
            return best_move
 
 
    def opponents_stone(r, direction, c, board, i):
        if ((r+direction[i][0])<8) and ((r+direction[i][0])>-1) and ((c + direction[i][1])<8) and ((c + direction[i][1])>-1):
            return board[r+ direction[i][0]][c + direction[i][1]]
            
    def possible_move(mini, r, c, counter, direction, i, counter2, my_color, maxi, flip, board):
        if ((r+ counter*direction[i][0])<8) and ((r+ counter*direction[i][0])>-1) and ((c + counter*direction[i][1])<8) and ((c + counter*direction[i][1])>-1) and ((board[r+ counter*direction[i][0]][c + counter*direction[i][1]]) == -1) and ((board[r+ counter2*direction[i][0]][c + counter2*direction[i][1]]) != my_color):
            return True
            
    def not_possible_move(r, c, counter, direction, i, counter2, my_color, board):
        if (((r+ counter*direction[i][0])<8) and ((r+ counter*direction[i][0])>-1) and ((c + counter*direction[i][1])<8) and ((c + counter*direction[i][1])>-1) and((board[r+ counter*direction[i][0]][c + counter*direction[i][1]]) == my_color)):
            return True

        
        

