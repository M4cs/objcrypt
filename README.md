# objcrypt
easily encrypt and decrypt python object and JSON objects with AES CBC 32 Block Encryption

planning on adding more encryption algos

# installation

```
pip install objcrypt

or

python3 setup.py install
```

# usage

```
import objcrypt, json

crypter = objcrypt.Crypter('key', 'cbc')
dictionary = {
  'test': 'test value'
}
encrypted_dict = crypter.encrypt_object(dictionary)

# encrypted_dict now has encrypted values

json_dict = json.loads(dictionary)
enc_json = crypter.encrypt_json(json_dict)

# enc_json is now encrypted

dec_dict = crypter.decrypt_object(encrypted_dict)

# decoded now

dec_json = crypter.decrypt_json(enc_json)

# decoded json object now
```
