import string
import random
from pyargon2 import hash
def id_generator(size=8, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

salt = id_generator()
pepper = id_generator()
passowrd = "hello"
print(hash(hash(hash(passowrd, salt), salt), salt, pepper))