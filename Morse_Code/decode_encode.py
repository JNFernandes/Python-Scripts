from morse_dict import MORSE_CODE_DICT, inv_morse_code

def encoding(message):
  listed_message=list(message)
  list_encoded=[]
  for i in range(len(listed_message)):
    if listed_message[i] in MORSE_CODE_DICT.keys():
      list_encoded.append(MORSE_CODE_DICT[listed_message[i]])
    else:
      list_encoded.append('/')
  print(''.join(list_encoded).lower())

def decoding(message, list_encoded):
  list_decoded=[]
  for i in range(len(list_encoded)):
    if list_encoded[i] in inv_morse_code.keys():
      list_decoded.append(inv_morse_code[list_encoded[i]])
    else:
      list_decoded.append(' ')
  print(''.join(list_decoded).lower())