from Crypto import Random
from Crypto.Cipher import AES
from Crypto.PublicKey import RSA
from hashlib import md5
import base64

AES.key_size = 32

def encrypteAES(plaintext, key):
	print ('Encrypting ......')
	hkey  = md5(key.encode('utf-8')).digest()
	iv    = Random.new().read(AES.block_size)
	cip   = AES.new(hkey, AES.MODE_CFB, iv)
	ctext = iv+cip.encrypt(plaintext.encode('utf-8'))
	return base64.b64encode(ctext)


def decAES(ciphertext, text):
	print ('Decripting ....')
	hkey = md5(key.encode('utf-8')).digest()
	iv = ciphertex[AES.block_size:]
	cip =AES.new(hkey, AES.MODE_CFB , iv)
	ptext = cip.decrypt(base64.b64encode(ciphertex))[AES.block_size:]
	return ptext



def QA():
	print('1-Decrypte, 2-Encrypt')
	a1 = str(input(""))
	while a1 != '1' and a1 != '2':
		a1 = str(input(""))
	if a1 == '1' :
		print ("Enter input(1-File, 2-Console input)")
		a2 = str(input(""))
		while a2 != '1' and a2 != '2':
			a2 = str(input(""))
		if a2 == '1' :
			f = input('file: ')
			key = input('Key: ')
			res= decAES(open(f,'r').read(),key)
			open(f+'.dcrpt' , w).write(res.decode('utf-8'))
			res = 'OK'
		if a2 == '2':
			data = input(": ")
			key = input("Key: ")
			res = decAES(data, key)
	if a1 == '2':
		print ("Enter input type(1-File , 2-Console input)")
		a2 = str(input(""))
		while a2 != '1' and a2 != '2' :
			a2 = str(input(""))
		if a2 == '1':
			f = input('File : ')
			key = input('key : ')
			res = encrypteAES(open(f, 'r').read(), key)
			open(f+'.crp', 'w').write(res.decode('utf-8'))
			res = 'OK'
				
		if a2 =='2' :
			data = input('plaintext :')
			key = input('key : ')
			res = encrypteAES(data, key)
	return res
print(QA())