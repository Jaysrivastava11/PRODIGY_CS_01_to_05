path = r' C:\Users\SOOSAI\Download\encry\python.jpg'
key = int(input('Enter Key for encryption of image : '))
print('The path of file : ' , path)
print('Key for envryption :' , key)
fin = open(path, 'rb')
image = fin.read()
fin.close()
image = bytearray(image)
for index, values in enumerate (image):
        image [index] = values ^ key
        fin = open(path, 'wb')
        fin. write(image)
        fin.close()
        print('Encryption Done... ')
        
