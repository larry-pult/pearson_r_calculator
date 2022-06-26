# kalkulator pearson r by larrypult
# biar ngisi tabelnya lebih cepet
# sama ngecek jawaban akhirnya bener apa nggak

import math

n = int(input("jumlah baris: "))
i = 0
list_x = [0]*n
list_y = [0]*n

print("input bilangan x dan y space-separated, contohnya '1 2'")

while i < n:
    try:
        x, y = input("x y: ").split()
        list_x[i] = int(x) if float(x) == int(float(x)) else float(x)
        list_y[i] = int(y) if float(y) == int(float(y)) else float(y)

        i += 1
    except ValueError:
        print("error, input ulang baris barusan")

sigma_x = 0
sigma_y = 0
sigma_xy = 0
sigma_x2 = 0
sigma_y2 = 0

print("  i  |       x        |       y        |       xy       |      x^2       |      y^2       |")
print("-----|----------------|----------------|----------------|----------------|----------------|")

for i in range(n):
    x = list_x[i]
    y = list_y[i]
    xy = round(x*y, 2)
    x2 = round(x*x, 2)
    y2 = round(y*y, 2)

    sigma_x += x
    sigma_y += y
    sigma_xy += xy
    sigma_x2 += x2
    sigma_y2 += y2

    print(str(i+1).center(5) + "|"
          + str(x).center(16) + "|"
          + str(y).center(16) + "|"
          + str(xy).center(16) + "|"
          + str(x2).center(16) + "|"
          + str(y2).center(16) + "|")

print("-----|----------------|----------------|----------------|----------------|----------------|")
print("  S  |"
      + str(round(sigma_x, 2)).center(16) + "|"
      + str(round(sigma_y, 2)).center(16) + "|"
      + str(round(sigma_xy, 2)).center(16) + "|"
      + str(round(sigma_x2, 2)).center(16) + "|"
      + str(round(sigma_y2, 2)).center(16) + "|")

r = (n*sigma_xy - sigma_x*sigma_y) / math.sqrt((n*sigma_x2 - sigma_x*sigma_x)*(n*sigma_y2 - sigma_y*sigma_y))

print("pearson r:", round(r, 4))
input("press enter to exit")
