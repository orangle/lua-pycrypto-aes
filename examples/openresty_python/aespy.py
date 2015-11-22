# -*- coding=utf-8 -*-
# author: orangleliu
# lua python 无缝加密解密

from Crypto.Cipher import AES
import base64

class AESCipher(object):
    def __init__(self, key, mode , iv, pad="{", size=16):
        self.key = key
        self.mode = mode
        self.pad = pad
        self.size = size
        self.iv = iv

    def encrypt(self, raw):
        cipher = AES.new(self.key, self.mode, self.iv)
        return base64.b64encode(cipher.encrypt(self.addpad(raw)))

    def decrypt(self, enc):
        enc = base64.b64decode(enc)
        cipher = AES.new(self.key, self.mode, self.iv)
        return self.cleanpad(cipher.decrypt(enc))

    def addpad(self, raw):
        n = self.size - len(raw)%self.size
        return raw + self.pad*n

    def cleanpad(self, raw):
        return raw.rstrip(self.pad)


if __name__ == '__main__':
    iv = "--(i_love_niu)--"
    key = "--(i_love_niu)--"
    plain = "iloveniu"

    mode = AES.MODE_CBC
    aes = AESCipher(key, mode, iv)
    cipher = aes.encrypt(plain)
    print cipher
    print aes.decrypt(cipher)

    mode = AES.MODE_CFB
    aes = AESCipher(key, mode, iv)
    cipher = aes.encrypt(plain)
    print cipher
    print aes.decrypt(cipher)

    mode = AES.MODE_OFB
    aes = AESCipher(key, mode, iv)
    cipher = aes.encrypt(plain)
    print cipher
    print aes.decrypt(cipher)
