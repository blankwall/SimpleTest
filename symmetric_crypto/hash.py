import base64
import urllib.parse
import binascii
import hashlib

# Quick and dirty hash function to hash a string for a given table size. Based on Dan Bernstein's djb2
def quickhash(mystr, size):
    h = 3313  # arbitrary large prime number to initialize

    for char in mystr:
        # hash(i) = hash(i-1) * 33 + str[i]
        try:
        	h = ((h << 5) + h) + ord(char)
        except:
        	print("Could not handle {0}".format(char))

    #return int(long(h)%long(size))  # python 2.7 needs some overflow magic
    return h%size

query =  bytes('Hellö Wörld@Python \x89', 'utf-8')

print("My string is: {0} -- length {1}".format(query.decode(),len(query)))

print("----Encoding-----")
print("hex encoded: {0}".format(binascii.hexlify(query)))
print("URL encoded: {0}".format(urllib.parse.quote(query)))
print("Base64 encoded: {0}".format(base64.b64encode(query)))
print()
print("----Hash-----")
print("DJB2 hash: {0}".format(quickhash(query.decode("utf-8"), len(query.decode("utf-8")))))
print("MD5 poor cryptographic hash: {0}".format(hashlib.md5(query).hexdigest()))
print("Sha256 cryptographic hash: {0}".format(hashlib.sha256(query).hexdigest()))
print()

print("---Testing our hash! -----")

new_string = "ABCDEFG"
print("My string is: {0} -- length {1}".format(new_string,len(new_string)))

one_hash = hashlib.sha256(new_string.encode()).hexdigest()
print("Sha256 cryptographic hash: {0}".format(one_hash))
print()

print("Changing A to B")
print()

new_string = new_string.replace("A", "B")
print("My string is: {0} -- length {1}".format(new_string,len(new_string)))

two_hash = hashlib.sha256(new_string.encode()).hexdigest()
print("Sha256 cryptographic hash: {0}".format(two_hash))

print("Hashes are the same? {0}".format(one_hash == two_hash))

