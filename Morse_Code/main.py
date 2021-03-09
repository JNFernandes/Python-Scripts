from decode_encode import encoding,decoding
from logo import logo

print(logo)
message = input("Type message to encode: ").upper()

decoding_msg = input("Do you want to decode? Type 'y' for yes or 'n' for no: ").lower()


if decoding_msg == 'n':
  encoding(message)
else:
  decoding(message,encoding(message))























    


