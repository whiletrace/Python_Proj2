import string
from ciphers import Cipher 

class Atbash(Cipher):
    """docstring for Atbash"""
    def __init__(self):
        super (Atbash, self).__init__()
        self.key = ('Z','Y','X','W','V','U','T','S','R','Q','P','O','N','M',
                    'L','K','J','I','H','G','F','E','D','C','B','A'
                    )

    def keytoint(self, char):

        keytoi= {'Z':0,'Y':1,'X':2,'W':3,'V':4,'U':5,'T':6,'S':7,'R':8,
         'Q':9,'P':10,'O':11,'N':12,'M':13,'L':14,'K':15,
         'J':16,'I':17,'H':18,'G':19,'F':20,'E':21,'D':22,
         'C':23,'B':24,'A':25}
        return keytoi[char]

    def encrypt(self, text):
        x = [self.chartoint(char) for char in text]
        cipher =[self.key[i] for i in x]
        print(''.join(cipher))
        print(self.keytoint)
        
    def decrypt(self, text):
        x = [self.keytoint(char) for char in text]
        plaintext = [self.inttochar(i) for i in x]
        print(''.join(plaintext))