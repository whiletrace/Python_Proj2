
from ciphers import Cipher


class Atbash(Cipher):
    """Atbash class encrypts and decrypts messages using the Atbashh cipher

       from Cipher class inherits methods encrypt, decrypt, chartoint, intochar:
       attr self.key = char Z-> A, method keytoint is a char -> int conversion
    """
    def __init__(self):
        super(Atbash, self).__init__()
        self.key = ('Z', 'Y', 'X', 'W', ' V', 'U', 'T', 'S', 'R', 'Q', 'P',
                    'O', 'N', 'M', 'L', 'K', 'J', 'I', 'H', 'G', 'F', 'E',
                    'D', 'C', 'B', 'A'
                    )

    def keytoint(self, char):
        """ key to int conversion helper method to aid in decryption"""

        keytoi = {'Z': 0, 'Y': 1, 'X': 2, 'W': 3, 'V': 4, 'U': 5, 'T': 6,
                  'S': 7, 'R': 8, 'Q': 9, 'P': 10, 'O': 11, 'N': 12, 'M': 13,
                  'L': 14, 'K': 15, 'J': 16, 'I': 17, 'H': 18, 'G': 19,
                  'F': 20, 'E': 21, 'D': 22, 'C': 23, 'B': 24, 'A': 25
                  }
        return keytoi[char]

    def encrypt(self, text):
        """encrypt Atbash:text as arugument cleartext -> toint -> key(i) """
        # takes whitespace out of message
        text = text.replace(' ', '')
        # convert text -> int
        x = [self.chartoint(char) for char in text]
        # for i to char using self.key(i) completes cipher
        cipher = [self.key[i] for i in x]
        # output cipher
        print('here is your encrypted text: {}'.format(''.join(cipher)))

    def decrypt(self, text):
        """decrypt text as arugument ciphertext -> keytochar -> intotchar """
        text = text.replace(' ', '')
        # ciphertext char -> int
        x = [self.keytoint(char) for char in text]
        # int -> inttochar
        plaintext = [self.inttochar(i) for i in x]
        # output cleartext
        print('here is decrypted text: {}'.format(''.join(plaintext)))
