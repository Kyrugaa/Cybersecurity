# simple python script for decoding hexadecimal to utf8:

hex_string = "636f6e7461696e6572"
decoded_string = bytes.fromhex(hex_string).decode('utf-8')
print(decoded_string)