import os
import binascii


def generate_session_id():
    return binascii.hexlify(os.urandom(16))
