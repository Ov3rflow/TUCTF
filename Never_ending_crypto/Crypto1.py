from pwn import *

## The in order list of chars being used for the encryption cipher
algorithmns_list = "ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~ !\"#$%&'()*+,-./0123456789:;<=>?@"


## Pass in the offset (shift) the program is using this run through and the encrypted text
## decrypt it
def decrypt(encrypted, index):
	global algorithmns_list
	solved = ''
	for c in encrypted:
		plain_char_posn = (algorithmns_list.index(c) - offset) % len(algorithmns_list)
		solved += algorithmns_list[plain_char_posn]

	return solved


## Find the offset (shift) being used for this run through
def find_offset(result):
	global algorithmns_list
	index = algorithmns_list.index(result)
	return index 


## connect and receive banner
conn = remote('neverending.tuctf.com', 12345)



## solve over and over until we reach 50 solves
count = 1
while True:

	banner = conn.recvuntil('text:') 

	## send an A and receive what A encrypts to
	conn.send('A\r\n')
	result = conn.recvline()
	#strip away everything but the encrypted result
	result = result[-3]

	##find the offset for this current attempt
	offset = find_offset(result)

	## receive the encrypted text to solve
	solve = conn.recvline()
	conn.recvuntil(':')

	## cut out the superfluous crap  received along with the solve string
	solve = solve[8:-12]

	## attempt to decrypt the string
	solution = decrypt(solve, offset)


	## send solution and check if its right
	print 'Sending solution: %s' %(solution)
	conn.sendline(solution)
	

	## Once we reach 50 solves, print stop and receive all text back from the server to get the flag
	if count == 50:
		result = conn.recvall()
		print result
		break

	else:
		conn.recvline()

	count += 1		


conn.close()
