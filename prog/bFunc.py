import random

class bBullsCows:
    ''' main class '''
    def __init__(self, iDigit):
        # количество цифр
        self.iDigit = iDigit
        # задуманный код
        self.sCode  = []
        # введенный код пользователем
        self.sInput = []
        # количество быков
        self.iBulls = 0
        # количество коров
        self.iCows  = 0

    def genCode(self):
        i = 0
        while i < self.iDigit:
            igenNum = random.randint(0,9)
            self.sCode.append(igenNum) 
            i += 1

    def getUserCode(self):
        sTmp = input('input '+str(self.iDigit)+' digit:')
        self.sInput.clear()
        i = 0
        while i < self.iDigit:
             self.sInput.append(int(sTmp[i:(i+1)])) 
             i += 1
            
    def compareCodes(self):
        bFlag = True
        self.iBulls = 0
        self.iCows  = 0
        i=0
        while i<self.iDigit:
            if self.sCode[i] == self.sInput[i]:
                self.iBulls += 1
            else:
                bFlag = False
            j=0
            while j<self.iDigit:
                if self.sCode[i] == self.sInput[j]:
                    self.iCows += 1
                j += 1
            i += 1
        return bFlag

    def run(self):
        self.genCode()
        self.getUserCode()
        itry = 1
        while self.compareCodes() == False:
            print ('№',itry, 'Bulls:', self.iBulls, 'Cows', self.iCows)
            print(' code: ',self.sCode,'user:',self.sInput)
            itry += 1
            self.getUserCode()
        else:
            print('winner!!!  ', itry)