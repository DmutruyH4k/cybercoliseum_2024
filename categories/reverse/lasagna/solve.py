import base64
from Cryptodome.Cipher import AES
from Cryptodome.Util.Padding import unpad
from Cryptodome.Util.strxor import strxor_c


t = b'B\xc8>\xcc,\xdc\xafA\x193\x9f\xb5Z/\x80\xa8\xa0\xaar\xacT%\xc9\xa4\x9aeg\xe4\xeb\x87\x87\xcd\xd0]\xf8\xb6\xdb/\xe0h\x0e\xc6!\xc4\x8aq\x82\xa7'


def c(t, s):
    r = ""
    for c in t:
        if c.isalpha():
            o = ord("a") if c.islower() else ord("A")
            sc = chr((ord(c) - o + s) % 26 + o)
            r += sc
        else:
            r += c
    else:
        return r


def d(i):
	a_k = b'KEYrf87ijoasd8j1'
	a_i = a_i = b'IV89jf9198fj8912'
	cipher = AES.new(a_k, AES.MODE_CBC, a_i)
	a_d = unpad(cipher.decrypt(i), AES.block_size)
	x_k = 65
	x_d = strxor_c(a_d, x_k)
	b_d = base64.b64decode(x_d).decode()
	s = 13
	c_d = c(b_d, s)
	return c_d


print(d(t))