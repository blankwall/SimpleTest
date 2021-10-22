# we need 2 helper mappings, from letters to ints and the inverse
L2I = dict(zip("ABCDEFGHIJKLMNOPQRSTUVWXYZ",range(26)))
I2L = dict(zip(range(26),"ABCDEFGHIJKLMNOPQRSTUVWXYZ"))


def encrypt_caesar(key,plaintext):
	ciphertext = ""
	for c in plaintext.upper():
	    if c.isalpha(): ciphertext += I2L[ (L2I[c] + key)%26 ]
	    else: ciphertext += c
	return ciphertext

def decrypt_caesar(key, ciphertext):
	# decipher
	plaintext2 = ""
	for c in ciphertext.upper():
	    if c.isalpha(): plaintext2 += I2L[ (L2I[c] - key)%26 ]
	    else: plaintext2 += c
	return plaintext2

message = "Top secret do not read"

print("My original message: {0}".format(message))
message = encrypt_caesar(3,message)
print("My encrypted message: {0}".format(message))
message = decrypt_caesar(3,message)
print("My decrypted message: {0}".format(message))