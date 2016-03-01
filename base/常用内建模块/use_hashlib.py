import hashlib

sha1 = hashlib.sha1()

sha1.update('how to use sha1 in python hashlib?'.encode('utf-8'))
print(sha1.hexdigest())