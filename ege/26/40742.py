f = open("26 (6).txt")
n = int(f.readline())
start = 1633305600
end = start + 604800
count = 0
time = [0 for i in range(0, 604801)]
for i in f:
    startP, endP = i.split()
    if startP < start and (endP > start or endP == 0):
        count = count + 1

