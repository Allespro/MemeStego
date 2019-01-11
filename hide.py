from stegano import lsb # steganography lib



msg = input('Insert your command: ')



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



secret = lsb.hide("meme.png", caesarify(msg, encoded=False)) # join our message and meme pic

secret.save("meme-secret.png") # save our new meme pic



#-------------------------------------------



# DECODING EXAMPLE


clear_msg = lsb.reveal("meme-secret.png") # get the secret message

print(caesarify(clear_msg)) # convert to normal text
