from ciphers import Cipher


class Affine(Cipher):
    """Class Affine inherits from Cipher

    attribute self.mod v 26 holds the value of mod26 which is the
    lengnth of alphabet being encoded this takes for granted that it
    being encoded is the English alphabetn26 characters. Methods that are
    inherited from Cipher: encrypt, decrypt, chartoint, intochar
    """

    def __init__(self):
        super(Affine, self).__init__()
        self.mod = 26

    def encrypt(self, text, key_a, key_b):
        """ method allows encryption of text using the affine cipher:

        method makes use of chartoint and intochar methods inherited from
        Cipher aid in the conversion of char->int->char the method takes three
        methods text= (text to encrypt) and two keys: key_a = should be prime
        to self.mod, key_b = which can be any int range 1-25 encryption
        uses formula (ax+b) mod26 a _key_a, x = cleartext char, b =key_b
        """
        # remove whitespance from message
        text = text.replace(' ', '')
        # convert user text to corresponding integers
        x = [self.chartoint(char) for char in text]
        # for each i in x ((key_a)x + keyb)
        step2 = [(key_a * i) + key_b for i in x]
        # for each i in step 2 i  medelo self.mod
        mod = [i % self.mod for i in step2]
        # int to char conversion to reveal cipher
        cipher = [self.inttochar(i) for i in mod]
        # output cipher
        print('here is your encrypted text: {}'.format(''.join(cipher)))

    def decrypt(self, text, key_a, key_b):
        """ method allows decryption of message encrypted with affine cipher:

        method makes use of chartoint and intochar methods inherited from
        Cipher aid in the conversion of char->int->char decrypt takes three
        methods text= (text to decrypt) and two keys: key_a, key_b both keys
        need to be provided for decryption to work for decryption decryption
        function is  ^a(y-b) mod 26 where a^ is multiplicative inverse of
        key_a and self.mod y is ciphertext ->int b = key_b"""

        # remove whitespance from message
        text = text.replace(' ', '')
        # convert ciphermessage char ->int
        y = [self.chartoint(char) for char in text]
        # list int 0 -> 25
        rtwentysix = list(range(26))
        # finds multiplicacative inverse formula 1=aa^-1 mod m
        multiinverse = [x for x in rtwentysix if (x * key_a) % self.mod == 1]
        # to complete deccryption  a^-1(y - b)
        decode = [multiinverse[0] * (i - key_b) for i in y]
        # selt.inttochar to convert to clear text
        plaintext = [self.inttochar(i) for i in decode]
        # output cleartext
        print('here is your decrypted text: {}'.format(''.join(plaintext)))
