import os

class Corpus:

    def __init__(self, path=0):
        self.path = path
    def emails(self, path=0):
        directory = os.listdir(self.path)
        
        for i in directory:
            if i.startswith("!"):
                continue
            else:
                adress = os.path.join(self.path, i)
                with open(adress, "r", encoding="utf-8") as file:
                    txt = file.read()
        
        
            yield i, txt
