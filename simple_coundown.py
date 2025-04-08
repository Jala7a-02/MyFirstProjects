import time

n = int(input("how much time do you want the computer to sleep"))

for x in (range(n ,0 ,-1)):
    second = x % 60
    minutes = int(x / 60) % 60
    hours = int(x / 3600) 
    print(f"{hours:02}:{minutes:02}:{second:02}")
    time.sleep(1)


print("time's up")