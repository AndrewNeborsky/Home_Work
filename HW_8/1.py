from random import randint
from PIL import Image
from threading import *


def calc(array, h_start, h_stop, w_start, w_stop):
    for i in range(h_start, h_stop):
        for j in range(w_start, w_stop):
            dist = [((point[1] - j) ** 2 + (point[0] - i) ** 2) ** 0.5 for point in points]
            dist.sort()
            array[i][j] = dist[0]


n = int(input('n = '))
width = 512
height = 512
points = []

noise = [[0 for w in range(width)] for h in range(height)]

for i in range(n):
    x = randint(0, width - 1)
    y = randint(0, height - 1)
    points.append([x, y])

thread1 = Thread(target=calc, args=(noise, 0, int(height / 4), 0, width))
thread2 = Thread(target=calc, args=(noise, int(height / 4), int(height / 2), 0, width))
thread3 = Thread(target=calc, args=(noise, int(height / 2), int(3 * height / 4), 0, width))
thread4 = Thread(target=calc, args=(noise, int(3 * height / 4), height, 0, width))

thread1.start()
thread2.start()
thread3.start()
thread4.start()

thread1.join()
thread2.join()
thread3.join()
thread4.join()

maxDist = 0
for i in range(height):
    for j in range(width):
        if maxDist < noise[i][j]:
            maxDist = noise[i][j]

image = Image.new('L', (width, height), 0)
for y in range(height):
    for x in range(width):
        image.putpixel((x, y), int(255 * noise[y][x] / maxDist))

image.save("noise.png", "png")
