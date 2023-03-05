import hashlib

def hash_file(filename):
   """"Bu fonksiyon, belirtilen dosyanın MD5 özetini hesaplar"""

   hasher = hashlib.md5()

   with open(filename, 'rb') as file:
       while True:
           data = file.read(65536)
           if not data:
               break
           hasher.update(data)

   return hasher.hexdigest()

filename = input("Lütfen dosya adı giriniz: ")

print("Dosyanın MD5 özeti: ", hash_file(filename))