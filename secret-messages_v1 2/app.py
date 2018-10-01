
from caesar import Caesar
from affine import Affine
from atbash import Atbash
from keyw import Keyw


def main():
    """prints menu gathers user input and instantiates cipher objects:

        prints gerneral interface for the program first implementatio
        of print is Secret Messages and then each cipher is listed
        on its own line. 'eord' is an input meant to gather
        wehether user wants to encrypt or decyrpt a message and stores
        that response. 'cipher' is input meant to gather
        which cipher user to accomplish encryption / decryption and stores
        that response. Exception raised if user cipher input not in cipher
        listif/elif consume 'eord', 'cipher' instantiate objects:
        Caesar, Affine, Atbash, Keyw based upon input stored
        'eord' and 'cipher'.'message' input stores user message
        to encrypt or decrypt" all object instantiation calls take message
        as argument. In additionAffine object instantion takes arguments :
        key_a and key_b. both of which are inputs if key_a and key_b
        out of range  exception will be raised. KeyW object instantation takes
        key as a argument"""

    print('Secret messages: \n\n')

    eord = input('would you like to encrypt or decrypt a message: ')

    cipher = input('which cipher: \n{}\n{}\n{}\n{}'
                   .format('Affine', 'Atbash', 'Caesar', 'Keyword\n\n'))

    if cipher.lower() not in ('affine', 'atbash', 'caesar', 'keyword'):
        raise Exception('not a valid choice')
    # Caesar cipher encrypt
    elif cipher.lower() == 'caesar' and eord.lower() == 'encrypt':
        message = input('please type a message')
        A = Caesar()
        print(A.encrypt(message))
    # Caesar cipher decrypt
    elif cipher.lower() == 'caesar' and eord.lower() == 'decrypt':
        message = input('please type a message')
        A = Caesar()
        print(A.decrypt(message))
    # Affine cipher encrypt
    elif cipher.lower() == 'affine' and eord.lower() == 'encrypt':
        key_a = input('for key_a acceptable choices are,'
                      '1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25')

        if int(key_a) not in (1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25):
            raise Exception('this key would not work')
        else:
            key_b = input('for key_b choose a number 1 - 25')
            if int(key_b) not in (range(25)):
                raise Exception('This is not a valid choice')

        message = input('please type a message to encrypt ')
        A = Affine()
        A.encrypt(message, int(key_a), int(key_b))
    # Affine cipher decrypt
    elif cipher.lower() == 'affine' and eord.lower() == 'decrypt':
        key_a = input('for key_a acceptable choices are'
                      '1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25')

        if int(key_a) not in (1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25):
            raise Exception('this key would not work')
        else:
            key_b = input('for key_b choose a number 1 - 25')
            if int(key_b) not in (range(25)):
                raise Exception('This is not a valid choice')

        message = input('please type a message to encrypt')
        A = Affine()
        A.decrypt(message, int(key_a), int(key_b))
    # Attbash cipher encrypt
    elif cipher.lower() == 'atbash' and eord.lower() == 'encrypt':
        message = input('please type a message: ')
        A = Atbash()
        A.encrypt(message)
    # Attbash cipher decrypt
    elif cipher.lower() == 'atbash' and eord.lower() == 'decrypt':
        message = input('please type a message: ')
        A = Atbash()
        A.decrypt(message)
    # Keyword cipher encrypt
    elif cipher.lower() == 'keyword' and eord.lower() == 'encrypt':
        key = input('please type a keyword for encryption')
        message = input('please type a message: ')
        A = Keyw()
        A.encrypt(message, key)
    # Keyword cipher decrypt
    elif cipher.lower() == 'keyword' and eord.lower() == 'decrypt':
        key = input('please type the key: ')
        message = input('please type a message: ')
        A = Keyw()
        A.decrypt(message, key)


if __name__ == '__main__':
    main()
