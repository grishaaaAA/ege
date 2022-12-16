f = open('26 (643456.txt')
n = int(f.readline())
frequencies = [0]*100
for _ in range(n):
    basket_size = int(f.readline())
    frequencies[basket_size] += 1
box_amount = 0
for basket_size in range(1, 49 + 1):
    box_amount +=\
        min(frequencies[basket_size], frequencies[100 - basket_size])
box_amount += frequencies[50] // 2
print(box_amount)
