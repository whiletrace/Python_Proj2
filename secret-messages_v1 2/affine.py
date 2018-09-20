import string
from ciphers import Cipher


class Affine(Cipher):
    """docstring for AFFine"""
    
    def __init__(self):
        super(Affine, self).__init__()
        self.mod = 26
        
    def encrypt(self, text, key_a, keyb):
        text = text.replace(' ','')
        # convert user text to corresponding integers
        x = [self.chartoint(char) for char in text]
        # implement ((key_a)x + keyb)
        step2= [(key_a * i) + keyb for i in x]
        # to complete cyper take result of step 2 and use modelo of the char length of alphabet
        mod = [i % self.mod for i in step2]
        # now to convert int from mod to char to complete the cipher
        cypher = [self.inttochar(i) for i in mod]

        print(''.join(cypher))