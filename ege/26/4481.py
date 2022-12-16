def task():
    f = open('26.4481.txt')
    n = int(f.readline())
    longitudes = {}
    for _ in range(n):
        latitude, longitude = [int(x) for x in f.readline().split()]
        latitude = int(latitude / 10)
        longitude /= 10
        if longitude not in longitudes.keys():
            longitudes[longitude] = []
        longitudes[longitude].append(latitude)
    maxCountOfLatitudes = 0
    maxLongitude = -200
    for longitude in sorted(longitudes.keys()):
        countOfLatitudes = len(longitudes[longitude])
        if countOfLatitudes >= maxCountOfLatitudes:
            maxCountOfLatitudes = countOfLatitudes
            maxLongitude = longitude
    print(maxLongitude * 10, len(set(longitudes[maxLongitude])))

task()



