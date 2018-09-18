class Cipher(object) :

    ''' Main Cipher class that all Cipher classes will inherit from in this
        implementation includes methods for char to int and int to char 
        conversion this was adapted from the work of Jameslyons in his 
        library pycipher and can be found at 
        https://github.com/jameslyons/pycipher/blob/master/pycipher/base.py
        methods encyrpt and decrypt will raise implementation errors if not 
        implemented by child cipher classes
        '''
        
    def encrypt(self):
        raise NotImplementedError()

    def decrypt(self):
        raise NotImplementedError()

    def chartoint(self, char):

        char = char.upper()
        conversiondict = {'A':0,'B':1,'C':2,'D':3,'E':4,'F':5,'G':6,'H':7,
                          'I':8,'J':9,'K':10,'L':11,'M':12,'N':13,'O':14,
                          'P':15,'Q':16,'R':17,'S':18,'T':19,'U':20,'V':21,
                          'W':22,'X':23,'Y':24,'Z':25}
        return conversiondict[char]

    def inttochar(self, i):

        i = i%26
        conversiondict = {'A','B','C','D','E','F','G','H','I','J','K','L','M',
                          'N','O','P','Q','U','R','S','T','U','V','W','X', 'Y',
                          'Z'}
        return conversiondict[i]

