import string
from ciphers import Cipher 

class Atbash(Cipher):
    """docstring for Atbash"""
    def __init__(self):
        super (Atbash, self).__init__()
        self.key = ('Z','Y','X','W','V','U','T','S','R','Q','P','O','N','M',
                    'L','K','J','I','H','G','F','E','D','C','B','A'
                    )
    def encrypt(self, text):
        x = [self.chartoint(char) for char in text]
        cipher =[self.key[i] for i in x]
        print(''.join(cipher))
        
    def decrypt(self, text):
        x