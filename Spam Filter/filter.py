import corpus
import os
from utils import *
import random
from collections import Counter

HAM = "OK"
SPAM = "SPAM"

class MyFilter:
    
    def __init__(self):
        self.wordham = [] #slovniku slov, ktere se nejcasteji vyskytuji u hamu
        self.wordspam = [] #slovniku slov, ktere se nejcasteji vyskytuji u spamu
        self.keyspam = [] #seznam nejpouzivanejsich slov
        self.keysham = [] #seznam nejpouzivanejsich slov

    def train(self, learn):
        truth_dict = read_classification_from_file(learn + "/!truth.txt")
        for key in truth_dict: 
            if truth_dict[key] == SPAM: #naplnim wordspam slovy
                with open(learn + "/" + key, "r", encoding="utf-8") as file:
                    txt = file.read()
                txt = txt.split()
                for i in txt:
                    self.wordspam.append(i)
            else: #naplnim wordham slovy
                with open(learn + "/" + key, "r", encoding="utf-8") as file:
                    txt2 = file.read()
                txt2 = txt2.split()
                for j in txt2:
                    self.wordham.append(j)
                    
        #vyradim slova, ktere nejsou slova a slova, ktere maji delku 1                
        self.wordspam = Counter(self.wordspam)
        for item in list(self.wordspam):
            if item.isalpha() == False: 
                self.wordspam.pop(item)
            elif len(item) == 1:
                self.wordspam.pop(item)
        self.wordspam = self.wordspam.most_common(1000)
        
        #prevedu slovnik na seznam nejpouzivanejsich slov
        for keys in self.wordspam:
            self.keyspam.append(keys[0])
            
        
        #to same udelam i pro slovnik hamu 
        self.wordham = Counter(self.wordham)             
        for item in list(self.wordham):
            if item.isalpha() == False: 
                self.wordham.pop(item)
            elif len(item) == 1:
                self.wordham.pop(item)
        self.wordham = self.wordham.most_common(1000)
        
        #prevedu slovnik na seznam nejpouzivanejsich slov
        for keys in self.wordham:
            self.keysham.append(keys[0])
    
    def test(self, test):
        border = 0
        corpus1 = corpus.Corpus(test)        
        for fname, text in corpus1.emails():
            border = 0
            text = text.split()
            for letter in text:         
                if letter in self.keyspam: #odeiram body za SPAM
                    border-=1  
                if letter in self.keysham: #pridavam body za HAM
                    border+=1
                    
            #pokud body budou vetsi nez 0, oznaci jako HAM, pro mensi oznaci SPAM
            with open(os.path.join(test, "!prediction.txt"), "a+", encoding="utf-8") as file:
                if border >= 0:
                    file.write(fname + " " + HAM + "\n")               
                else:
                    file.write(fname + " " + SPAM + "\n")
