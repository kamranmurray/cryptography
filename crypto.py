# Caesar Cipher
# Arguments: string, integer
# Returns: string
import random
import math
def encrypt_caesar(plaintext, offset):
	encryption = ""
	for element in plaintext:
		if not element.isalpha():
			new_unicode = ord(element)
		else:
			newunicode = ((ord(element) - 65 + offset) % 26) + 65
		encryption = encryption + chr(newunicode)
	return encryption


# Arguments: string, integer
# Returns: string
def decrypt_caesar(ciphertext, offset):
	encryption = ""
	for element in ciphertext:
		if not element.isalpha():
			encryption = encryption + element
		else
			if ord(element) - offset < 0:
				newunicode = ord(element) - offset + 26
				encryption = encryption + chr(newunicode)
			else:
				newunicode = ord(element) - offset
				encryption = encryption + chr(newunicode)
	return encryption

# Vigenere Cipher
# Arguments: string, string
# Returns: string
def encrypt_vigenere(plaintext, keyword):
	encryption = ""
	counter = 0
	while len(keyword) < len(plaintext):
		keyword = keyword + keyword
	for element in plaintext:
		newunicode = ord(keyword[counter]) - 65
		ogunicode = ord(element) - 65
		encryption = encryption + chr((newunicode + ogunicode) % 26 + 65)
		counter = counter + 1
	return encryption

# Arguments: string, string
# Returns: string
def decrypt_vigenere(ciphertext, keyword):
	encryption = ""
	counter = 0
	while len(keyword) < len(ciphertext):
		keyword = keyword + keyword
	for element in ciphertext:
		originalunicode = ord(element) - 65
		keyunicode = ord(keyword[counter]) - 65
		if ord(element) - 65 - keyunicode < 0:
			newunicode = ord(element) - 65 + 26 - keyunicode + 65
			encryption = encryption + chr(newunicode)
		else:
			newunicode = ord(element) - 65 - keyunicode + 65
			encryption = encryption + chr(newunicode)
		counter = counter + 1
	return encryption

# Merkle-Hellman Knapsack Cryptosystem
# Arguments: integer
# Returns: tuple (W, Q, R) - W a length-n tuple of integers, Q and R both integers
def generate_private_key(n=8):
	W = (1,)
	counter = 0
	while counter < n - 1:
		total = sum(list(W))
		addition = random.randint(total + 1, total*2)
		W = W + (addition,)
		counter = counter + 1
	Q = random.randint(sum(list(W))+1, 2 * sum(list(W)))
	R = 0
	while (math.gcd(Q,R) != 1):
		R= random.randint(2, Q -1)
	private_key = (W, Q, R)
	return private_key

# Arguments: tuple (W, Q, R) - W a length-n tuple of integers, Q and R both integers
# Returns: tuple B - a length-n tuple of integers
def create_public_key(private_key):
	W = private_key [0]
	Q = private_key [1]
	R = private_key [2]
	B = ()
	for x in W:
		B = B + ((x*R) % Q,)
	return B

# Arguments: string, tuple (W, Q, R)
# Returns: list of integers
def encrypt_mhkc(plaintext, public_key):
	encryption = ()
	for element in plaintext:
		bits_form = byte_to_bits(ord(element))
		C = 0
		counter = 0
		for x in bits_form:
			C = C + x*public_key[counter]
			counter = counter + 1
		encryption = encryption + (C,)
	return encryption

# Arguments: list of integers, tuple B - a length-n tuple of integers
# Returns: bytearray or str of plaintext
def decrypt_mhkc(ciphertext, private_key):
	C = ()
	C = ciphertext
	c_prime = ()
	for x in C:
		S = find_S(private_key[1], private_key[2])
		c_prime = c_prime + ((S*x % private_key[1]),)
	W = private_key[0]
	array_of_bytes = ()
	for x in c_prime:
		bits = [0, 0, 0, 0, 0, 0, 0, 0]
		counter = 7
		while counter >= 0:
			if (x -W[counter]) >= 0:
				x = x - W[counter]
				bits[counter] = 1
			counter = counter - 1
		bits_tuple = tuple(bits)
		array_of_bytes = array_of_bytes + (bits_to_byte(bits_tuple),)
	return array_of_bytes_to_string(array_of_bytes)

def find_S (Q, R):
	S = 0
	while S * R % Q != 1:
		S = S + 1
	return S

def byte_to_bits(value):
	bits = [0, 0, 0, 0, 0, 0, 0, 0]
	counter = 7
	holder = 0
	while counter >= 0:
		holder = 2**counter
		if (value - (holder)) >= 0:
			value = value - holder
			bits[counter] = 1
		counter = counter - 1
	bits_tuple = tuple(bits)
	return bits_tuple[::-1]

def bits_to_byte(bits):
	byte = 0
	counter = 0
	holder = 0
	while counter < 8:
		holder = 2**(7 - counter)
		if bits [counter] == 1:
			byte = byte + holder
		counter = counter + 1
	return byte

def array_of_bytes_to_string(array_of_bytes):
	final_string = ""
	for x in array_of_bytes:
		final_string = final_string + chr(x)
	return final_string

if __name__ == "__main__":
    str = "A,ONEINPUT,O"
    listo = str.split (",")
    lis = []
    for element in listo:
        if element.isdigit():
            lis.append(int(element))
        else:
            lis.append(element)
    if lis[1].isdigit():
        caesarEncryption = encrypt_caesar(lis[0], lis[1])
        caesarDecryption = decrypt_caesar(caesarEncryption, lis[1])
        if (caesarDecryption == lis[0]) & (caesarEncryption == lis[2]):
            print("caesar true")
    doubleone = encrypt_vigenere(lis[0], lis[1])
    zero = decrypt_vigenere(doubleone, lis[1])
    if (zero == lis[0]) & (doubleone == lis[2]):
        print ("vigenere true")
    privatekey = ((1, 2, 5, 13, 36, 93, 162, 397), 1043, 2)
    publickey = (2, 4, 10, 26, 72, 186, 324, 794)
    encryption = encrypt_mhkc("A", publickey)
    print(encryption)
    outcome = decrypt_mhkc([798], privatekey)
    print (outcome)