from time import sleep
n = 11
while True:
    n -= 1
    print(n)
    sleep(1)
    if n == 0:
        break
