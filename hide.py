from stegano import lsb # steganography lib
import sys # just for check first argument
import argparse # arguments lib



# Caesar Cipher implementation ---------------
def caesarify(msg, encoded=True): # encode an decode
    caesar_msg = '' # init var
    for c in msg: # for each char in string do
        if encoded == True:
            newChar = ord(c) - 93 # get the ord number of char and subtract 93
        else:
            newChar = ord(c) + 93 # get the ord number of char and sum 93
        newChar = chr(newChar) # convert to new char
        caesar_msg = caesar_msg + newChar # put chars together
    return caesar_msg # return new string var
#-------------------------------------------
# ENCODING EXAMPLE
def encode(meme_path, msg):
	if (meme_path == ''):
		meme_path = "meme.png"
	secret = lsb.hide(meme_path, caesarify(msg, encoded=False)) # join our message and meme pic
	secret.save("meme-secret.png") # save our new meme pic
	exit()
#-------------------------------------------
# DECODING EXAMPLE
def decode(meme_path):
	if (meme_path == ''):
		meme_path = "meme-secret.png"
	clear_msg = lsb.reveal("meme-secret.png") # get the secret message
	print(caesarify(clear_msg)) # convert to normal text
	exit()
#-------------------------------------------
# ARGUMENTS USING
def argload():
	if(len(sys.argv) == 1):
		sys.argv[1:] = ["-G"]
	parser = argparse.ArgumentParser()
	parser.add_argument ( '-G', '--graph', action='store_const', const='1', help='Interactive menu')
	parser.add_argument ( '-d', '--decode', help='Path to decode meme, if no using meme-secret.png')
	parser.add_argument ( '-e', '--encode',  help='Path to encode meme, if no using meme.png')
	parser.add_argument ( '-c', '--command', help='Comman to encode, use only with --encode')
	arg = parser.parse_args()
	if(str(format(arg.graph)) == '1'):
		print("[1] - Decode")
		print("[2] - Encode")
		shoose = input("Input here: ")
		if (shoose == '1'):
			meme_path = input('Insert secret-meme path, if no using ./meme-secret.png: ')
			decode(meme_path)

		if (shoose == '2'):
			msg = input('Insert your command: ')
			meme_path = input('Insert meme path, if no using ./meme.png: ')
			encode(meme_path, msg)
	str_command = str(format(arg.command))
	str_encode = str(format(arg.encode))
	str_decode = str(format(arg.decode))

	if(str_command != '' and str_encode != '' and str_decode == 'None'):
		encode(str(format(arg.encode)), str(format(arg.command)))
	elif(str_command == 'None' and str_encode == 'None' and str_decode != ''):
		decode(str(format(arg.decode)))
	else:
		exit("Error, please read help first")






	

if __name__ == '__main__':
	try:
		argload()
	except KeyboardInterrupt:
		exit("Exit...") 
