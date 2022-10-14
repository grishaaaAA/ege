import enum


class State(enum.Enum):
    waitingForX = 0
    waitingForY = 1
    waitingForZ = 2


f = open('245.txt')

state = State.waitingForX
currentLength = 0
maxLength = 0

while True:
    symbol = f.read(1)
    if symbol == '':
        maxLength = max(maxLength, currentLength)
        break
    if symbol == 'X' and state == State.waitingForX:
        currentLength += 1
        state = State.waitingForY
    elif symbol == 'Y' and state == State.waitingForY:
        currentLength += 1
        state = State.waitingForZ
    elif symbol == 'Z' and state == State.waitingForZ:
        currentLength += 1
        state = State.waitingForX
    else:
        maxLength = max(maxLength, currentLength)
        currentLength = 0
        state = State.waitingForX
        if symbol == 'X':
            currentLength = 1
            state = State.waitingForY

print(maxLength)
