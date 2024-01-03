### Replace file names

from cryptography.fernet import Fernet

key = Fernet.generate_key()



## Encryption



## Writing the key
fernet = Fernet(key)
with open('key.key', 'wb') as filekey:
    filekey.write(key)


## Reading the key
with open('key.key', 'rb') as filekey:
    key = filekey.read()


## Read the file
with open('JavaScript Tutorial for Beginners_ Learn JavaScript in 1 Hour.mp4', 'rb') as file:
    original_file = file.read()

encrypted = fernet.encrypt(original_file)


## Writing encrypted file to a folder
with open('encrypted JavaScript Tutorial for Beginners_ Learn JavaScript in 1 Hour.mp4', 'wb') as file:
    file.write(encrypted)


## Decrypt audio

fernet = Fernet(key)

with open('encrypted JavaScript Tutorial for Beginners_ Learn JavaScript in 1 Hour.mp4', 'rb') as file:
    encrypted_file = file.read()

decrypted = fernet.decrypt(encrypted_file)

## Writing decrypted file to folder.....

with open('decrypted JavaScript Tutorial for Beginners_ Learn JavaScript in 1 Hour.mp4', 'wb') as file:
    file.write(decrypted)
