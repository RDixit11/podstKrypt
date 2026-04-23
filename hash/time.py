import subprocess
import random
import string

def gen_word(length):
    return ''.join(random.choices(string.ascii_lowercase, k=length))

with open("time.csv", "w") as f:
    f.write("Dlugosc-slowa;Czas-MD5;Czas-SHA1;Czas-SHA2-224;Czas-SHA2-256;Czas-SHA2-384;Czas-SHA2-512;Czas-SHA3-224;Czas-SHA3-256;Czas-SHA3-384;Czas-SHA3-512\n")

for i in range(100000, 500001, 100000):
    for _ in range(100):
        word = gen_word(i)

        # uruchomienie main.py
        result = subprocess.run(
            ["python3", "main.py"],
            input = word,
            capture_output=True,
            text=True
        )

        # filtrowanie TIME:
        times = []
        for line in result.stdout.splitlines():
            if "TIME:" in line:
                times.append(line.split()[1])
        
        # zapis do pliku
        with open("time.csv", "a") as f:
            f.write(f"{i};" + ";".join(times) + "\n")
