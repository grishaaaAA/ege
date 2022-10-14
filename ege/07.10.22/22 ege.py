def parser_to_dict():
    f = open('22_1.csv')
    database = []
    for _ in range(15):
        x = [int(x) for x in f.readline().replace('"', '').split(';')]
        database.append({'process b': x[0], 'time': x[1], 'process a': x[2:]})
    return database


class process:
    def __init__(self, process_a, time, process_b):
        self.process_a = process_a
        self.time = time
        self.process_b = process_b

    def __str__(self):
        return str(self.process_a) + ' ' + str(self.time) + \
               ' ' + str(self.process_b)

    def __ge__(self, other):
        return other.process_a in self.process_b


def parser_to_class():
    f = open('22_1.csv')
    database = []
    for _ in range(15):
        x = [int(x) for x in f.readline().replace('"', '').split(';')]
        database.append(process(x[0], x[1], x[2:]))
    return database


database = parser_to_class()
for step in range(len(database)):
    for i in range(len(database) - 1):
        if database[i] >= database[i + 1]:
            database[i], database[i + 1] = database[i + 1], database[i]


for i in range(len(database)):
    maxtime = 0
    for j in range(i):
        if database[i] >= database[j]:
            maxtime = max(database[j].time, maxtime)
    database[i].time += maxtime

print(max([p.time for p in database]))
