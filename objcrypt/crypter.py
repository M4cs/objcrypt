import base64
import hashlib
import json
from Crypto import Random
from Crypto.Cipher import AES

class Crypter(object):
    def __init__(self, key):
        self.bs = 32
        self.key = hashlib.sha256(key.encode()).digest()

    def encrypt_object(self, python_obj):
        new_obj = {}
        for key, value in python_obj.items():
            raw_value = self._pad(value)
            iv = Random.new().read(AES.block_size)
            cipher = AES.new(self.key, AES.MODE_CBC, iv)
            new_obj[key] = base64.b64encode(iv + cipher.encrypt(raw_value)).decode('utf-8')
        return new_obj
    
    def encrypt_json(self, json_obj):
        new_obj = {}
        py_obj = json.loads(json_obj)
        for key, value in py_obj.items():
            raw_value = self._pad(str(value))
            iv = Random.new().read(AES.block_size)
            cipher = AES.new(self.key, AES.MODE_CBC, iv)
            new_obj[key] = base64.b64encode(iv + cipher.encrypt(raw_value)).decode('utf-8')
        return json.dumps(new_obj)
    
    def decrypt_object(self, enc_python_obj):
        dec_obj = {}
        for key, value in enc_python_obj.items():
            enc_value = base64.b64decode(value)
            iv_value = enc_value[:AES.block_size]
            cipher_value = AES.new(self.key, AES.MODE_CBC, iv_value)
            dec_obj[key] = self._unpad(cipher_value.decrypt(enc_value[AES.block_size:])).decode('utf-8')
        return dec_obj
    
    def decrypt_json(self, enc_json_obj):
        dec_obj = {}
        enc_python_obj = json.loads(enc_json_obj)
        for key, value in enc_python_obj.items():
            enc_value = base64.b64decode(value)
            iv_value = enc_value[:AES.block_size]
            cipher_value = AES.new(self.key, AES.MODE_CBC, iv_value)
            dec_obj[key] = self._unpad(cipher_value.decrypt(enc_value[AES.block_size:])).decode('utf-8')
        return json.dumps(dec_obj)

    def _pad(self, s):
        return s + (self.bs - len(s) % self.bs) * chr(self.bs - len(s) % self.bs)

    @staticmethod
    def _unpad(s):
        return s[:-ord(s[len(s)-1:])]
