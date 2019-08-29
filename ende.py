import sys, os
#sys.path.append('./ext')

from cryptography.fernet import Fernet

class RkEnDeCipher:

    def process(self, argument):
        func = self.switcher.get(argument[1], lambda: "nothing")

        secondArgument = None
        if len(sys.argv) > 2 and argument[2] is not None:
            secondArgument = argument[2];

        return func(secondArgument)

    def __init__(self):
        self.switcher = {"--encr": self.encr, "--decr":self.dece, "--install": self.install, "--reset": self.reset}
        self.cipher_file = "__cipherkey.o"

    def encr(self, password):
        if password is None or len(password) <= 0:
            print("Please provide a valid string (password) for encryption. Syntax:  ende --encr <your-encrypted-key-jere>")
            return
        try:
            cipher_suite = Fernet(self.readInstalledKey(None))
            ciphered_text = cipher_suite.encrypt(password.encode())   #required to be bytes
            print(ciphered_text.decode("utf-8"))
        except:
            print("encr failed")
            return

        # dece(ciphered_text.decode("utf-8"))
        # install()

    def dece(self, encryptedPassword):
        if encryptedPassword is None or len(encryptedPassword) <= 0:
            print("Please provide a valid encrypted-key to decrypt. Syntax:  ende --decr <your-encrypted-key-jere>")
            return

        try:
            k = self.readInstalledKey(None)
            cipher_suite = Fernet(self.readInstalledKey(None))
            unciphered_text = ( cipher_suite.decrypt( encryptedPassword.encode() ))
            print(unciphered_text.decode("utf-8"))
        except:
            print("Invalid encryption-key")

    def install(self, argument):
        key = Fernet.generate_key()
        #print(key.decode("utf-8"))
        f = open(self.cipher_file, "wb")
        f.write(key)
        f.close()
        print("ende key installed")

    def reset(self, argument):
        if os.path.exists(self.cipher_file):
            os.remove(self.cipher_file)
            print("cypherkey reset done, all generated encryption keys now invalid")
        else:
            print("ciphekey not found or not generated yet, here is command to generate:  ende --install")

    def readInstalledKey(self, argument):
        try:
            f = open(self.cipher_file, "r")
            key = f.readline()
            f.close()
            return key.encode()
        except:
            print("Cipherkey not found. Before ecr|dcr operation, please install cipher. Command to generate: ende --install")
            exit(1)

ende = RkEnDeCipher()
if len(sys.argv) >= 2 and any(sys.argv[1] in s for s in ende.switcher.keys()):
    RkEnDeCipher().process(sys.argv)
else:
    print ("Invalid ende option provided. Value options are: {}".format(ende.switcher.keys()))



# ---------------------------------------


# cipher_file = "__cipherkey.o"
#
# def encr(password):
#     if password is None or len(password) <= 0:
#         print("Please provide a valid string (password) for encryption. Syntax:  ende --encr <your-encrypted-key-jere>")
#         return
#     try:
#         cipher_suite = Fernet(readInstalledKey(None))
#         ciphered_text = cipher_suite.encrypt(password.encode())   #required to be bytes
#         print(ciphered_text.decode("utf-8"))
#     except:
#         print("encr failed")
#         return
#
#     # dece(ciphered_text.decode("utf-8"))
#     # install()
#
# def dece(encryptedPassword):
#     if encryptedPassword is None or len(encryptedPassword) <= 0:
#         print("Please provide a valid encrypted-key to decrypt. Syntax:  ende --decr <your-encrypted-key-jere>")
#         return
#
#     try:
#         k = readInstalledKey(None)
#         cipher_suite = Fernet(readInstalledKey(None))
#         unciphered_text = ( cipher_suite.decrypt( encryptedPassword.encode() ))
#         print(unciphered_text.decode("utf-8"))
#     except:
#         print("Invalid encryption-key")
#
# def install(argument):
#     key = Fernet.generate_key()
#     print(key.decode("utf-8"))
#     f = open(cipher_file, "wb")
#     f.write(key)
#     f.close()
#     print("ende key installed")
#
# def reset(argument):
#     if os.path.exists(cipher_file):
#         os.remove(cipher_file)
#         print("cypherkey reset done, all generated encryption keys now invalid")
#     else:
#         print("ciphekey not found or not generated yet, here is command to generate:  ende --install")
#
# def readInstalledKey(argument):
#     try:
#         f = open(cipher_file, "r")
#         key = f.readline()
#         f.close()
#         return key.encode()
#     except:
#        print("Cipherkey not found. Before ecr|dcr operation, please install cipher. Command to generate: ende --install")
#        exit(1)
#
#
# switcher = {"--encr": encr, "--decr":dece, "--install": install, "--reset": reset}
#
# def process(argument):
#     func = switcher.get(argument[1], lambda: "nothing")
#
#     secondArgument = None
#     if len(sys.argv) > 2 and argument[2] is not None:
#         secondArgument = argument[2];
#
#     return func(secondArgument)
#
#
# if len(sys.argv) >= 2 and any(sys.argv[1] in s for s in switcher.keys()):
#     process(sys.argv)
# else:
#     print ("-->{}<-- Invalid ende option provided. Value options are: {}".format(sys.argv[1], switcher.keys()))



