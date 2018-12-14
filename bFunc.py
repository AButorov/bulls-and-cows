import random

class bBullsCows:
    ''' main class '''
    def __init__(self, iDigit):
        self.iDigit = iDigit
        self.sCode  = []
        self.sInput = []
    
    def genCode(self):
        i = 0
        while i < self.iDigit:
            igenNum = random.randint(0,9)
            self.sCode.append(igenNum) 
            i += 1

    def getUserCode(self):
        sTmp = input('input '+str(self.iDigit)+' digit:')
        i = 0
        while i < self.iDigit:
             self.sInput.append(int(sTmp[i:(i+1)])) 
             i += 1
            

    def run(self):
        self.genCode()
        self.getUserCode()
        print('code: ',self.sCode,'user:',self.sInput)