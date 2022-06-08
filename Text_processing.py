import binascii
text = "Simply Easy Learning"

# Converting binary to ascii
data_b2a = binascii.b2a_uu(text)
print("**Binary to Ascii ** \n")
print (data_b2a)