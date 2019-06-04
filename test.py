import lib, json, time

dictionary = {
    'test': 'test value',
    'test1': 'test1 value1'
}
print('Values may change but the Key Test shows that hardcoded dictionary will always be able to be decrypted with the same key.')
time.sleep(5)
print('Python Object:\n', dictionary)
print()
encrypter = lib.Crypter('test')
print('Python Obj Encryption'.center(45, '-'))
enc_dict = encrypter.encrypt_object(dictionary)
print(enc_dict)
dec_dict = encrypter.decrypt_object(enc_dict)
print(dec_dict)
print()
print('JSON Encryption'.center(45, '-'))
json_dict = json.dumps(dictionary)
print('JSON Object:\n', json_dict)
print()
enc_j = encrypter.encrypt_json(json_dict)
print(enc_j)
dec_j = encrypter.decrypt_json(enc_j)
print(dec_j)
enc_dict = {'test': '56hBuGghCcWW0r2MkHmzOzCfYr9HaLRQhIelPoCVqcPDvmNkmsRkQSIJblW22Yq9',
            'test1': '4pVnXMOf3SvYlAc2ZuTJw9ql7tZcJjYWWfwnhseZitWRq+EzZ1Hog6/i0NOoW5Fe'}
print()
print('Key Test'.center(45, '-'))
test = encrypter.decrypt_object(enc_dict)
print(test)
print()
