import os
import sys
class Encrypter:
    __CHOOSE_MODE_MESSAGE = '''Please choose mode:
    1 for encryption;
    2 for decryption;
    0 to exit.'''

    __CHOOSE_FILE_MESSAGE = "Please enter file name (with file extension):\n"

    def main(self):
        mode = 1
        while(mode != 0):
            print(self.__CHOOSE_MODE_MESSAGE)
            mode = input()
            if(mode == 1):
                self.encrypt()
            elif(mode == 2):
                self.decrypt()
            else:
                continue
        sys.exit(0)

    def encrypt(self):
        print(self.__CHOOSE_FILE_MESSAGE)
        filename = input()
        if os.path.isfile(filename):
            file = open(filename, "r+")

        else:
            return

    def decrypt(self):
        return

runner = Encrypter()





