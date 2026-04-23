import hashlib as h
import sys
import time
import random
import string 

def SAC(n):
    word = gen_word(n)
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

    print("BITS CHANGED:", counter / 256 * 100, "%")


def coll(n):
    # sha256
    d = {}
    counter = 0

    while True:
        word = gen_word(n)
        hashed = h.sha256(word.encode()).hexdigest()

        bits = hashed[:3]

        if bits in d:
            print(f"COLLISION: {d[bits]} | {word} | {bits}")
            print("ATTEMPT:", counter)
            break
        else:
            d[bits] = word

        counter+=1

def gen_word(n):
    return ''.join(random.choice(string.ascii_lowercase) for _ in range(n))

def main():
    word = sys.argv[1]

    #word = sys.stdin.readline()

    if word == "coll":
        n = int(sys.argv[2])
        coll(n)
        exit(0)
    if word == "sac":
        n = int(sys.argv[2])
        SAC(n)
        exit(0)
    word = word.encode()
    md5_start = time.perf_counter()
    md5 = h.md5(word).hexdigest()
    md5_stop = time.perf_counter()
    md5_time = md5_stop - md5_start

    sha1_start = time.perf_counter()
    sha1 = h.sha1(word).hexdigest()
    sha1_stop = time.perf_counter()
    sha1_time = sha1_stop - sha1_start

    sha2_224_start = time.perf_counter()
    sha2_224 = h.sha224(word).hexdigest()
    sha2_224_stop = time.perf_counter()
    sha2_224_time = sha2_224_stop - sha2_224_start

    sha2_256_start = time.perf_counter()
    sha2_256 = h.sha256(word).hexdigest()
    sha2_256_stop = time.perf_counter()
    sha2_256_time = sha2_256_stop - sha2_256_start

    sha2_384_start = time.perf_counter()
    sha2_384 = h.sha384(word).hexdigest()
    sha2_384_stop = time.perf_counter()
    sha2_384_time = sha2_384_stop - sha2_384_start

    sha2_512_start = time.perf_counter()
    sha2_512 = h.sha512(word).hexdigest()
    sha2_512_stop = time.perf_counter()
    sha2_512_time = sha2_512_stop - sha2_512_start

    sha3_224_start = time.perf_counter()
    sha3_224 = h.sha3_224(word).hexdigest()
    sha3_224_stop = time.perf_counter()
    sha3_224_time = sha3_224_stop - sha3_224_start
    
    sha3_256_start = time.perf_counter()
    sha3_256 = h.sha3_256(word).hexdigest()
    sha3_256_stop = time.perf_counter()
    sha3_256_time = sha3_256_stop - sha3_256_start

    sha3_384_start = time.perf_counter()
    sha3_384 = h.sha3_384(word).hexdigest()
    sha3_384_stop = time.perf_counter()
    sha3_384_time = sha3_384_stop - sha3_384_start

    sha3_512_start = time.perf_counter()
    sha3_512 = h.sha3_512(word).hexdigest()
    sha3_512_stop = time.perf_counter()
    sha3_512_time = sha3_512_stop - sha3_512_start

    print(f"MD5: {md5}\nTIME: {md5_time:.2e}\n---")
    
    print(f"\nSHA1: {sha1}\nTIME: {sha1_time:.2e}\n---")
    
    print(f"\nSHA2_224: {sha2_224}\nTIME: {sha2_224_time:.2e}\n---")
    print(f"\nSHA2_256: {sha2_256}\nTIME: {sha2_256_time:.2e}\n---")
    print(f"\nSHA2_384: {sha2_384}\nTIME: {sha2_384_time:.2e}\n---")
    print(f"\nSHA2_512: {sha2_512}\nTIME: {sha2_512_time:.2e}\n---")

    print(f"\nSHA3_224: {sha3_224}\nTIME: {sha3_224_time:.2e}")
    print(f"\nSHA3_256: {sha3_256}\nTIME: {sha3_256_time:.2e}")
    print(f"\nSHA3_384: {sha3_384}\nTIME: {sha3_384_time:.2e}")
    print(f"\nSHA3_512: {sha3_512}\nTIME: {sha3_512_time:.2e}")

if __name__ == "__main__":
    main()
