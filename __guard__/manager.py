#!/Python36_64/python

'''
Sublime Notebook Manager
v0.2.1
'''

import os
import sys
from cryptlib import get_file_list, encode, update_file, get_key, decode

FLAG = 'FLAG_FILE'


def createFlagFile():
	fptr = open(FLAG, 'w')
	fptr.write('')
	fptr.close()


if __name__ == '__main__':

	if sys.version_info < (3, 4):
		sys.stderr.write("You need python 3.4 or later to run this script\n")
		sys.exit(1)

	if not os.path.exists(FLAG):
		# new case
		# or decrypted state in power fail
		print('Not encrypted, encrypting....')
		key = get_key()
		print('Re-enter key')
		key2 = get_key()
		if key != key2:
			print('Keys don\'t match, exiting')
			sys.exit(1)
		update_file(encode, get_file_list(), key2)
		createFlagFile()
	else:
		# encrypted already
		print('Encrypted, give key to unlock')
		key = get_key()
		failStatus = update_file(decode, get_file_list(), key)
		if failStatus:
			print('You entered wrong key. FO')
			sys.exit(2)
		os.remove(FLAG)
		# decoded, wait to close
		print('Notes have been decrypted')
		ans = ''
		while ans != 'e':
			ans = input('Press e to encrypt again > ')
		# encrypt
		update_file(encode, get_file_list(), key)
		createFlagFile()
