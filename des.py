import chilkat2
crypt = chilkat2.Crypt2()
crypt.CryptAlgorithm = "des"
crypt.CipherMode = "cbc"
crypt.KeyLength = 64
crypt.PaddingScheme = 0
crypt.EncodingMode = "hex"
ivHex = "0001020304050607"
crypt.SetEncodedIV(ivHex,"hex")
keyHex = "0001020304050607"
crypt.SetEncodedKey(keyHex,"hex")
encStr = "4759AE0081E64B5EEFD3A4E3D92C47777CDA37E8CBE374400B2F92548ED5F50D657887E5504E9D7F2B9B1EC375704841"
decStr = crypt.DecryptStringENC(encStr)
print (decStr)
