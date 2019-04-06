class MyPlayer:
    ''' Zacne tim co je pro neho vyhodnejsi.Pote se prizpusobuje protivnikovu hrani'''
    def __init__(self, payoff_matrix, number_of_iterations=0):
        self.payoff_matrix = payoff_matrix
        self.number_of_iterations = number_of_iterations
        self.memory =memory = []      #vytvori seznam

    def move(self):
        COOPERATE = False
        DEFECT = True
        if ((self.memory)==[]):
            if ((self.payoff_matrix[COOPERATE][COOPERATE][0]) > (self.payoff_matrix[DEFECT][DEFECT][0])):
            #pokud pro mne bude vyhodnejsi zacit coop pak zacnu kooperaci
                return COOPERATE
            else:
            #pokud ne tak zacnu podvadenim
                return DEFECT
        
        elif ((self.memory[-1]) == DEFECT):#pokud protivnik podvadi zacnu taky
            return DEFECT
        elif ((self.memory[-1])==COOPERATE):#pokud spolupracuje taky spolupracuji
            return COOPERATE
            
    def record_opponents_move(self, opponent_move):
        self.memory.append(opponent_move)#prida tah do seznamu memory

