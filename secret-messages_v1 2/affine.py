import string
from ciphers import Cipher


class Affine(Cipher):
    """docstring for AFFine"""
    
    def __init__(self):
        super(Affine, self).__init__()
        self.mod = 26
        
    def encrypt(self, text, key_a, key_b):
        text = text.replace(' ','')
        # convert user text to corresponding integers
        x = [self.chartoint(char) for char in text]
        # implement ((key_a)x + keyb)
        step2= [(key_a * i) + key_b for i in x]
        # to complete cyper take result of step 2 and use modelo of the char length of alphabet
        mod = [i % self.mod for i in step2]
        # now to convert int from mod to char to complete the cipher
        cypher = [self.inttochar(i) for i in mod]

        print(''.join(cypher))

    def decrypt(self, text, key_a, key_b):
        text = text.replace(' ', '')
        y = [self.chartoint(char) for char in text]
        rtwentysix = list(range(26))

        multiinverse = [x for x in rtwentysix if (x * key_a) % self.mod == 1]

        decode =[multiinverse[0] * (i - key_b) for i in y]

        plaintext = [self.inttochar(i) for i in decode]

        print(''.join(plaintext))

