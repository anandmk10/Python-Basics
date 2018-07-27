#ciphers- Caesar Substitution Platfair

cipher_scheme = input("Select Cipher: \n-->1 - Caesar Cipher \n-->2 - Substitution Cipher \n-->3 - PlayFair Cipher\n")
"""Selecting cipher."""

encryption_type = input("Select Encryption/Decryption:\n-->E - Encryption \n-->D - Decryption\n")
"""Selecting encryption/decryption."""

message = input("Enter Message:\n")
"""Message to encrypt/decrypt."""

from pycipher import Caesar, Playfair

if cipher_scheme == '1':
    """Caesar cipher."""
    if encryption_type == "E":
        e_msg = Caesar(key=-3).encipher(message)
        print("Encrypted Message: ",e_msg)

    elif encryption_type == "D":
        d_msg = Caesar(key=-3).decipher(message)
        print("Decrypted Message: ",d_msg)

if cipher_scheme == '2':
    """Substitution cipher."""
    off =int(input("Enter Key: "))
    if encryption_type == "E":
        e_msg = Caesar(key=off).encipher(message)
        print("Encrypted Message: ",e_msg)

    elif encryption_type == "D":
        d_msg = Caesar(key=off).decipher(message)
        print("Decrypted Message: ",d_msg)

if cipher_scheme == '3':
    """Playfair cipher"""
    if encryption_type == "E":
        e_msg = Playfair(key='HELOWRDABCFGIJKMNPSTUVXYZ').encipher(message)
        print("Encrypted Message: ", e_msg)

    elif encryption_type == "D":
        d_msg = Playfair(key='HELOWRDABCFGIJKMNPSTUVXYZ').decipher(message)
        print("Decrypted Message: ",d_msg)
