import sys, os, hashlib

def rc4(key, data):
    S = list(range(256))
    j = 0
    for i in range(256):
        j = (j + S[i] + key[i % len(key)]) % 256
        S[i], S[j] = S[j], S[i]
    i = j = 0
    out = bytearray()
    for byte in data:
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]
        out.append(byte ^ S[(S[i] + S[j]) % 256])
    return bytes(out)

key = bytes.fromhex(sys.argv[1])
src = sys.argv[2]
dst = sys.argv[3]

os.makedirs(dst, exist_ok=True)

for f in os.listdir(src):
    if f.endswith('.dll'):
        with open(os.path.join(src, f), 'rb') as fh:
            data = fh.read()
        enc = rc4(key, data)
        md5 = hashlib.md5(enc).hexdigest()
        with open(os.path.join(dst, md5), 'wb') as fh:
            fh.write(enc)
