from PIL import Image
import random

def visual_secret_share(file, out1, out2):
    img = Image.open(file).convert("1")  # czarno-biały
    width, height = img.size

    # nowe obrazy będą 2x szersze
    share1 = Image.new("1", (width * 2, height))
    share2 = Image.new("1", (width * 2, height))

    pixels = img.load()
    s1 = share1.load()
    s2 = share2.load()

    for y in range(height):
        for x in range(width):
            pixel = pixels[x, y]

            pattern = random.choice([
                (0, 1),
                (1, 0)
            ])

            if pixel == 255:
                s1[2*x, y], s1[2*x+1, y] = pattern
                s2[2*x, y], s2[2*x+1, y] = pattern
            else:
                s1[2*x, y], s1[2*x+1, y] = pattern
                s2[2*x, y], s2[2*x+1, y] = pattern[::-1]

    share1.save(out1)
    share2.save(out2)
