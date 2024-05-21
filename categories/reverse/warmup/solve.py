from Cryptodome.Cipher import AES


crypt_bytes = bytearray([90, 90, 131, 173, 3, 108, 139, 21, 101, 136, 11, 35, 101, 154, 191, 222, 178, 128, 45, 197, 220, 65, 122, 138, 18, 173, 210, 128, 16, 101, 247, 74])
key = b'CODEBY__PASSWORD'
iv = b'IV82941840912841'

cipher = AES.new(key, AES.MODE_CBC, iv)
flag = cipher.decrypt(crypt_bytes)

print(flag.decode())