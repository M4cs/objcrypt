import base64
import hashlib
import json
from Crypto import Random
from Crypto.Cipher import AES


class Crypter(object):
    def __init__(self, key):
        self.key = hashlib.sha256(key.encode()).digest()

    @staticmethod
    def _encrypt_object(key, obj):
        new_obj = {}
        for obj_key, value in obj.items():
            raw_value = Crypter._pad(value)
            iv = Random.new().read(AES.block_size)
            cipher = AES.new(key, AES.MODE_CBC, iv)
            new_obj[obj_key] = base64.b64encode(iv + cipher.encrypt(raw_value)).decode('utf-8')
        return new_obj

    def encrypt_object(self, python_obj):
        return Crypter._encrypt_object(self.key, python_obj)

    def encrypt_json(self, json_obj):
        py_obj = json.loads(json_obj)
        new_obj = Crypter._encrypt_object(self.key, py_obj)
        return json.dumps(new_obj)

    @staticmethod
    def _decrypt_object(key, obj):
        dec_obj = {}
        for obj_key, value in obj.items():
            enc_value = base64.b64decode(value)
            iv_value = enc_value[:AES.block_size]
            cipher_value = AES.new(key, AES.MODE_CBC, iv_value)
            dec_obj[obj_key] = Crypter._unpad(cipher_value.decrypt(enc_value[AES.block_size:])).decode('utf-8')
        return dec_obj

    def decrypt_object(self, enc_python_obj):
        return Crypter._decrypt_object(self.key, enc_python_obj)
    
    def decrypt_json(self, enc_json_obj):
        enc_python_obj = json.loads(enc_json_obj)
        dec_obj = Crypter._decrypt_object(self.key, enc_python_obj)
        return json.dumps(dec_obj)

    @staticmethod
    def _pad(s, bs=32):
        return s + (bs - len(s) % bs) * chr(bs - len(s) % bs)

    @staticmethod
    def _unpad(s):
        return s[:-ord(s[len(s)-1:])]
