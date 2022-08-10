n = int(input("input the number\n"))
k = input("select a range. Example: 0 12\n").rstrip().split()
divisor = []
for i in range(int(k[0]), int(k[1])+1):
    if n%i == 0:
        divisor.append(i)