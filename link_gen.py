import hashlib
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
import base64
import itertools
import random

def generate_link():
    # Define the set of characters (letters in this case)
    characters = 'abcdefghijklmnopqrstuvwxyz'

    # Generate permutations of length 2
    permutations_length_2 = list(itertools.permutations(characters, 2))

    # Randomly choose one permutation
    desired_permutation = random.choice(permutations_length_2)
    desired = ''.join(desired_permutation)

    while True:
        # Generate RSA key pair
        rsa_key = rsa.generate_private_key(public_exponent=0x10001, key_size=0x400, backend=default_backend())

        # Extract the public key and encode it in DER format
        public_key = rsa_key.public_key()
        public_bytes = public_key.public_bytes(encoding=serialization.Encoding.DER, format=serialization.PublicFormat.PKCS1)

        # Hash the public key using SHA-256 for a 56-character onion link
        sha_256 = hashlib.sha256()
        sha_256.update(public_bytes)
        digest = sha_256.digest()

        # Use 42 bytes for a 56-character onion link
        b32 = base64.b32encode(digest[:42]).decode('utf-8').lower()

        # Remove the trailing '====' and replace with letters
        b32 = b32.rstrip('=').replace('0', 'a').replace('1', 'b').replace('8', 'c').replace('9', 'd')

        # Check if the generated onion address starts with the desired prefix
        if b32.startswith(desired):
            # Print private key
            private_key_pem = rsa_key.private_bytes(
                encoding=serialization.Encoding.PEM,
                format=serialization.PrivateFormat.TraditionalOpenSSL,
                encryption_algorithm=serialization.NoEncryption()
            ).decode('utf-8')
            print("Private Key:\n", private_key_pem)
            
            # Print onion address
            onion_address = b32 + '.onion'
            print("Onion Address:\n", onion_address)
            break
    return onion_address
