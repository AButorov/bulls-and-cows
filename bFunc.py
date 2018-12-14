class bBullsCows:
    ''' main class '''
    def __init__(self, iDigit):
        self.iDigit = iDigit
        self.sCode  = ('*'*iDigit)
        self.sInput = ('*'*iDigit)
    
    def genCode(self):
        self.sCode = '1234'

    def run(self):
        print(self.sCode + '  ' + self.sInput )