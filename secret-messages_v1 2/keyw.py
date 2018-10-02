from ciphers import Cipher


class Keyw(Cipher):
    """Keyw class encrypts and decrypts messages using the keyword cipher

       from Cipher class inherits methods encrypt, decrypt, chartoint,
       intochar:attr self.alpha = char A-> Z, method:scrub_duplicates
    """
    def __init__(self):
        super(Keyw, self).__init__()
        self.alpha = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K',
                      'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
                      'W', 'X', 'Y', 'Z'
                      ]

    def scrub_duplicates(self, list):
        """creates list from keyword and text with no duplicate chars"""

        ciphertext = []
        for char in list[:]:
            if char not in ciphertext:
                ciphertext.append(char)
        return ciphertext

    def encrypt(self, text, keyword):
        """encrypt method uses keyword method to encrypyt user message:

            takes keyword as arguement creates list of char from keyword
            appends self.alpha to list != to char in keyword then scrub \
            duplicate char from list list -> chartoint, int -> cipher char
        """

        # keyword to list of char
        key = list(keyword)
        text = text.replace(' ', '')

        # append self.alpha to key char list
        X = [key.append(char) for char in self.alpha]
        # convert text to to int
        chartoi = [self.chartoint(char)for char in text]
        # create new list != duplicate char
        cipher = self.scrub_duplicates(key)
        # convert int to char using scrubbed key
        ciphert = [cipher[i] for i in chartoi]
        # output cipher text
        print('here is your encrypted text: {}'.format(''.join(ciphert)))

    def decrypt(self, text, keyword):
        """decrypt method decrypts user message encrypted by keyword cipher:

            takes keyword as arguement creates list of char from keyword
            appends self.alpha to list != to char in keyword then scrub
            duplicate char from list  creates dict with keyword + alpha !=
            duplicates char as key and value is index position. text-> int for
            then int to char using self.inttochar(i) method output cleartext
            and cypher text index as value
        """
        # keyword to list of char
        key = list(keyword)
        text = text.replace(' ', '')
        # append self.alpha to key char list
        X = [key.append(char) for char in self.alpha]
        # create new list != duplicate char
        cipher = self.scrub_duplicates(key)
        # dict {cipherkeychar: index range 26}
        cipherdict = dict(zip(cipher, list(range(26))))
        # message char ->int
        ciphertoi = [cipherdict[i] for i in text]
        # int ->plain text char
        plaintext = [self.inttochar(i) for i in ciphertoi]
        # output result
        print('here is your decrypted text: {}'.format(''.join(plaintext)))
