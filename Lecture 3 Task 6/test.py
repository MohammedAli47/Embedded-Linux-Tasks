import time
for i in range(5):
    print(i)
    if i == 2:
        i = 1
        print(i)
        time.sleep(1)