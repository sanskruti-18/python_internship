d = []
t = []

n = int(input("Enter size of d: "))
m = int(input("Enter size of t: "))

for dist in range(n):
    dist = int(input("Enter values: "))
    d.append(dist)

for time in range(m):
    time = int(input("Enter values: "))
    t.append(time)

if n == m:
    speed = [dl/tl for dl,tl in zip(d,t)]

print(speed)