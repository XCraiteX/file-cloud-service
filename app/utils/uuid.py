from random import randint
import string 

from app.data.config import UUID_LEN, SYMBOLS

async def generate_uuid():
    letters = [SYMBOLS[randint(0, len(SYMBOLS))] for x in range(len(SYMBOLS))]
    key = ''.join(letters)

    return key 