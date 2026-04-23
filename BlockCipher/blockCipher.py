from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
import time

def test(key, data):

    ecb = AES.new(key, AES.MODE_ECB)
    ecb_start = time.time()
    ecb_ciphertext = ecb.encrypt(pad(data, AES.block_size))
    ecb_time = time.time() - ecb_start

    ecb_dec = AES.new(key, AES.MODE_ECB)
    ecb_start_dec = time.time()
    ecb_plain = unpad(ecb_dec.decrypt(ecb_ciphertext), AES.block_size)
    ecb_time_dec = time.time() - ecb_start_dec
    
    iv = get_random_bytes(16)
    cbc = AES.new(key, AES.MODE_CBC, iv=iv)
    cbc_start = time.time()
    cbc_ciphertext = cbc.encrypt(pad(data, AES.block_size))
    cbc_time = time.time() - cbc_start

    cbc_dec = AES.new(key, AES.MODE_CBC, iv=iv)
    cbc_start_dec = time.time()
    cbc_plain = unpad(cbc_dec.decrypt(cbc_ciphertext), AES.block_size)
    cbc_time_dec = time.time() - cbc_start_dec

    ctr = AES.new(key, AES.MODE_CTR)
    ctr_start = time.time()
    ctr_ciphertext = ctr.encrypt(data)
    ctr_time = time.time() - ctr_start

    ctr_dec = AES.new(key, AES.MODE_CTR, nonce=ctr.nonce)
    ctr_start_dec = time.time()
    ctr_plain = ctr_dec.encrypt(ctr_ciphertext)
    ctr_time_dec = time.time() - ctr_start_dec

    return ecb_time,ecb_time_dec,cbc_time,cbc_time_dec,ctr_time,ctr_time_dec


def error(key, data):
    
    iv = get_random_bytes(16)

    ecb = AES.new(key, AES.MODE_ECB)
    ctr1 = AES.new(key, AES.MODE_CTR)
    ctr2 = AES.new(key, AES.MODE_CTR, nonce=ctr1.nonce)

    ecb_cipher = ecb.encrypt(pad(data, AES.block_size))
    cbc_cipher = AES.new(key, AES.MODE_CBC, iv=iv).encrypt(pad(data, AES.block_size))
    ctr_cipher = ctr1.encrypt(data)

    f_bit = data[0]
    if f_bit & 1 == 0:
        ch_bit = f_bit | 1
    else:
        ch_bit = f_bit & 0b11111110
    
    w_ch = bytes([ch_bit]) + data[1:]

    ecb_cipher_w_ch = ecb.encrypt(pad(w_ch, AES.block_size))
    cbc_cipher_w_ch = AES.new(key, AES.MODE_CBC, iv=iv).encrypt(pad(w_ch, AES.block_size))
    ctr_cipher_w_ch = ctr2.encrypt(w_ch)

    print(f"ECB CIPHER: {ecb_cipher}")
    print(f"ECB CIPHER CHANGED BIT: {ecb_cipher_w_ch}\n---\n")

    print(f"CBC CIPHER: {cbc_cipher}")
    print(f"CBC CIPHER CHANGED BIT: {cbc_cipher_w_ch}\n---\n")

    print(f"CTR CIPHER: {ctr_cipher}")
    print(f"CTR CIPHER CHANGED BIT: {ctr_cipher_w_ch}\n---\n")
### Deszyforwanie
    print("DECIPHER:")
    ecb_dec = AES.new(key, AES.MODE_ECB)
    ecb_plain = unpad(ecb_dec.decrypt(ecb_cipher), AES.block_size)
    ecb_plain_w_ch = unpad(ecb_dec.decrypt(ecb_cipher_w_ch), AES.block_size)

    cbc_dec = AES.new(key, AES.MODE_CBC, iv=iv)
    cbc_plain = unpad(cbc_dec.decrypt(cbc_cipher), AES.block_size)
    cbc_plain_w_ch = cbc_dec.decrypt(cbc_cipher_w_ch)
   
    ctr_dec1 = AES.new(key, AES.MODE_CTR, nonce=ctr1.nonce)
    ctr_dec2 = AES.new(key, AES.MODE_CTR, nonce=ctr1.nonce)
    ctr_plain = ctr_dec1.decrypt(ctr_cipher)
    ctr_plain_w_ch = ctr_dec2.decrypt(ctr_cipher_w_ch)

    print(f"ECB DECIPHER: {ecb_plain}")
    print(f"ECB DECIPHER CHANGED BIT: {ecb_plain_w_ch}\n---\n")

    print(f"CBC DECIPHER: {cbc_plain}")
    print(f"CBC DECIPHER CHANGED BIT: {cbc_plain_w_ch}\n---\n")

    print(f"CTR DECIPHER: {ctr_plain}")
    print(f"CTR DECIPHER CHANGED BIT: {ctr_plain_w_ch}\n---\n")


def cbc(key,data):
    
    iv = get_random_bytes(16)

    padded_data = pad(data, 16)

    chunks = [padded_data[i:i+16] for i in range(0,len(padded_data),16)]
    
    aes = AES.new(key, AES.MODE_ECB)
    res = []
    for i in range(len(chunks)):
        if i == 0:
            xor = bytes(x^y for x,y in zip(chunks[i], iv))
        else:
            xor = bytes(x^y for x,y in zip(chunks[i], res[i-1]))
        enc = aes.encrypt(xor)
        res.append(enc)
    
    aes_dec = AES.new(key, AES.MODE_ECB)
    res_dec = []
    for i in range(len(res)):
        dec = aes_dec.decrypt(res[i])
        if i == 0:
            xor = bytes(x^y for x,y in zip(dec, iv))
        else:
            xor = bytes(x^y for x,y in zip(dec, res[i-1]))
        res_dec.append(xor)
    return b"".join(res), unpad(b"".join(res_dec),16)
