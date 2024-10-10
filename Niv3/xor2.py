secret = bytes.fromhex("1d0811130f1749150d0003195a1d1315080e5a0017081314")
key = "pizzapizzapizzapizzapizz"

# Function to XOR bytes with key
def xor(secret, key):
    return bytes([x ^ ord(key[i % len(key)]) for i, x in enumerate(secret)])

# Apply XOR and print the result as a string
result = xor(secret, key)
print(f"La reponse est : {result.decode('utf-8')}")
