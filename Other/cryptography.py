# Python Crash Course
# cryptography.py
# Created by Mauro J. Pappaterra on 07 of April 2019.
import hashlib as h
import random as r
import string as s

# Generate random Nonce
nonce = ''.join(r.choices(s.ascii_letters + s.digits, k=r.randint(1, 20)))

# Hash it!
hash = h.sha256(("something" + nonce).encode()).hexdigest()