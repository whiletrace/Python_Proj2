import string

from ciphers import Cipher

class Keyw(Cipher):
    """docstring for Keyw"""
    def __init__(self):
        super (Keyw, self).__init__()
        self.alpha = ['A','B','C','D','E','F','G','H','I','J','K','L','M',
                      'N','O','P','Q','R','S','T','U','V','W','X', 'Y','Z']
        


    def scrub_duplicates(self, list):
        ciphertext= [] 
        for char in list[:]: 
            if char not in ciphertext: 
                ciphertext.append(char)
        return ciphertext

    

    def encrypt(self, text, keyword):
        
        key = list(keyword)

        X = [key.append(char) for char in self.alpha]

        chartoi = [self.chartoint(char)for char in text]
        
        cipher = self.scrub_duplicates(key)

        ciphert =[cipher[i] for i in chartoi]

        print(''.join(ciphert))

    

    def decrypt(self, text, keyword):

        key = list(keyword)

        X = [key.append(char) for char in self.alpha]

        cipher = self.scrub_duplicates(key)

        cipherdict = dict(zip(cipher, list(range(26))))

        ciphertoi =[cipherdict[i] for i in text]

        plaintext =[self.inttochar(i) for i in ciphertoi]

        print(''.join(plaintext))

