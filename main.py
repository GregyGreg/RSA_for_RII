import rsa

message = "Hello World!!!"

(pubKey, privKey) = rsa.generateKey()

print("Открытый ключ", pubKey)
print("Закрытый ключ", privKey)
