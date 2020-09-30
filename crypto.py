# Caesar Cipher
# Arguments: string, integer
# Returns: string
import random
import math
def encrypt_caesar(plaintext, offset):
	encryption = ""
	for element in plaintext:
		newunicode = ((ord(element) - 65 + offset) % 26) + 65
		encryption = encryption + chr(newunicode)
	return encryption


# Arguments: string, integer
# Returns: string
def decrypt_caesar(ciphertext, offset):
	encryption = ""
	for element in ciphertext:
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
	return array_of_bytes 

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
	return bits_tuple

def bits_to_byte(bits):
	byte = 0
	counter = 0
	holder = 0
	while counter < 8:
		holder = 2**counter
		if bits [counter] == 1:
			byte = byte + holder
		counter = counter + 1
	return byte

def array_of_bytes_to_string(array_of_bytes):
	final_string = ""
	for x in array_of_bytes:
		final_string = final_string + chr(x)
	return final_string

def main():
    # Testing code here
	caesar_E = encrypt_caesar("ABC", 4)
	print (caesar_E)
	
	caesar_D = decrypt_caesar(caesar_E, 4)
	print (caesar_D)
	
	vigenere_E = encrypt_vigenere("ZZZ", "ABC")
	print (vigenere_E)
	
	vigenere_D = decrypt_vigenere(vigenere_E, "ABC")
	print (vigenere_D)

	private_key = generate_private_key()
	public_key = create_public_key(private_key)
	encryption = encrypt_mhkc("lil tester", public_key)
	result = decrypt_mhkc(encryption, private_key)
	print(array_of_bytes_to_string(result))	

main()