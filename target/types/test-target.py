from hashlib import sha256
from secrets import token_hex

# the solver needs to brute the 4 char hash, good for testing time to solve and a testing suite
def generate(mod):
    key = token_hex(3)
    print(key)
    return ("data:,"+sha256(key.encode("ascii")).hexdigest(), key)