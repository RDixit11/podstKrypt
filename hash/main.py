import hashlib as h
import sys
import time
import random
import string 

def SAC():
    word = gen_word()
    en = word.encode()
    hashed = h.sha256(en).hexdigest()
    
    f_bit = en[0]
    if f_bit & 1 == 0:
        ch_bit = f_bit | 1
    else:
        ch_bit = f_bit & 0b11111110
    
    w_ch = bytes([ch_bit]) + en[1:]

    hashed_w_ch = h.sha256(w_ch).hexdigest()
    
    word_bin = bin(int(hashed, 16))[2:].zfill(256)
    w_ch_bin = bin(int(hashed_w_ch, 16))[2:].zfill(256)
    
    counter = 0

    for i in range(len(word_bin)):
        if word_bin[i] != w_ch_bin[i]:
            counter += 1

    print("BITS CHANGED: ", counter / 256 * 100, "%")


def coll():
    # sha256
    d = {}
    counter = 0

    while True:
        word = gen_word()
        hashed = h.sha256(word.encode()).hexdigest()

        bits = word[:3]

        counter+= 1

        if bits in d:
            print("COLLISION")
            print(d[bits], word)
            print("ATTEMPT: ", counter)
            break
        else:
            d[bits] = word

def gen_word():
    return ''.join(random.choice(string.ascii_lowercase) for _ in range(5))

def main():
    word = sys.argv[1]
    if word == "coll":
        coll()
        exit(0)
    if word == "sac":
        SAC()
        exit(0)
    word = word.encode()
    md5_start = time.time()
    md5 = h.md5(word).hexdigest()
    md5_stop = time.time()
    md5_time = md5_stop - md5_start

    sha1_start = time.time()
    sha1 = h.sha1(word).hexdigest()
    sha1_stop = time.time()
    sha1_time = sha1_stop - sha1_start

    sha256_start = time.time()
    sha256 = h.sha256(word).hexdigest()
    sha256_stop = time.time()
    sha256_time = sha256_stop - sha256_start

    print(f"MD5: {md5}\nTIME: {md5_time}\n---")
    print(f"\nSHA1: {sha1}\nTIME: {sha1_time}\n---")
    print(f"\nSHA256: {sha256}\nTIME: {sha256_time}\n---")

if __name__ == "__main__":
    main()
