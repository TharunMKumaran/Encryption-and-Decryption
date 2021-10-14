Python 3.9.6 (tags/v3.9.6:db3ff76, Jun 28 2021, 15:26:21) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> from cryptography.fernet import Fernet
>>> key = Fernet.generate_key()
>>> with open('filekey.key', 'wb') as filekey:
     filekey.write(key)

     
44
>>> with open('filekey.key', 'rb') as filekey:
     key = filekey.read()

     
>>> fernet = Fernet(key)
>>> with open('nba.csv', 'rb') as file:
     original = file.read()

     
>>> encrypted = fernet.encrypt(original)
>>> with open('nba.csv', 'wb') as encrypted_file:
     encrypted_file.write(encrypted)

     
43852
>>> fernet = Fernet(key)
>>> with open('nba.csv', 'rb') as enc_file:
     encrypted = enc_file.read()

     
>>> decrypted = fernet.decrypt(encrypted)
>>> with open('nba.csv', 'wb') as dec_file:
     dec_file.write(decrypted)

     
32823
>>> 