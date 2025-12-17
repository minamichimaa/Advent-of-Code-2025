def prettyPrint(array: list[str]):
    for i in array:
        print(i.strip())

def parseInput(input: str) -> list:
    banks = []
    for line in input:
        banks.append(tuple([int(x) for x in line.strip()]))
    return banks

# don't look
def findMaximumJoltage(bank: tuple[int]) -> int:
    activatedBatteries = []

    aPos = 0
    aVal = bank[aPos]
    
    for a in range(1, len(bank) - 11):
        # print(a)
        if bank[a] > aVal:
            aVal = bank[a]
            aPos = a

    activatedBatteries.append(aVal)
    bPos = aPos + 1
    bVal = bank[bPos]
    
    for b in range(bPos + 1, len(bank) - 10):
        # print(b)
        if bank[b] > bVal:
            bVal = bank[b]
            bPos = b

    activatedBatteries.append(bVal)
    cPos = bPos + 1
    cVal = bank[cPos]

    for c in range(cPos + 1, len(bank) - 9):
        # print(c)
        if bank[c] > cVal:
            cVal = bank[c]
            cPos = c

    activatedBatteries.append(cVal)
    dPos = cPos + 1
    dVal = bank[dPos]

    for d in range(dPos + 1, len(bank) - 8):
        if bank[d] > dVal:
            dVal = bank[d]
            dPos = d

    activatedBatteries.append(dVal)
    ePos = dPos + 1
    eVal = bank[ePos]

    for e in range(ePos + 1, len(bank) - 7):
        if bank[e] > eVal:
            eVal = bank[e]
            ePos = e
    
    activatedBatteries.append(eVal)
    fPos = ePos + 1
    fVal = bank[fPos]

    for f in range(fPos + 1, len(bank) - 6):
        if bank[f] > fVal:
            fVal = bank[f]
            fPos = f

    activatedBatteries.append(fVal)
    gPos = fPos + 1
    gVal = bank[gPos]

    for g in range(gPos + 1, len(bank) - 5):
        if bank[g] > gVal:
            gVal = bank[g]
            gPos = g

    activatedBatteries.append(gVal)
    hPos = gPos + 1
    hVal = bank[hPos]

    for h in range(hPos + 1, len(bank) - 4):
        if bank[h] > hVal:
            hVal = bank[h]
            hPos = h

    activatedBatteries.append(hVal)
    iPos = hPos + 1
    iVal = bank[iPos]

    for i in range(iPos + 1, len(bank) - 3):
        if bank[i] > iVal:
            iVal = bank[i]
            iPos = i

    activatedBatteries.append(iVal)
    jPos = iPos + 1
    jVal = bank[jPos]

    for j in range(jPos + 1, len(bank) - 2):
        if bank[j] > jVal:
            jVal = bank[j]
            jPos = j

    activatedBatteries.append(jVal)
    kPos = jPos + 1
    kVal = bank[kPos]

    for k in range(kPos + 1, len(bank) - 1):
        if bank[k] > kVal:
            kVal = bank[k]
            kPos = k

    activatedBatteries.append(kVal)
    lPos = kPos + 1
    lVal = bank[lPos]

    for l in range(lPos + 1, len(bank) - 0):
        if bank[l] > lVal:
            lVal = bank[l]
            lPos = l

    activatedBatteries.append(lVal)

    return int(''.join(str(x) for x in activatedBatteries))


def findMaximumJoltageNew(bank: tuple[int], numOfBatteries: int) -> int:
    activatedBatteries = []
    count = 0

    lastPos = -1
    
    while count != numOfBatteries:
        aPos = lastPos + 1
        aVal = bank[aPos]
        for a in range(aPos + 1, len(bank) - (numOfBatteries - count - 1)):
            if bank[a] > aVal:
                aVal = bank[a]
                aPos = a
        
        lastPos = aPos
        activatedBatteries.append(aVal)

        count += 1

    return int(''.join(str(x) for x in activatedBatteries))


def main() -> int:
    ## input
    with open("input.txt", "r") as f:
        textIn = f.readlines()

    banks = parseInput(textIn)

    totalJoltage = 0
    for bank in banks:
        totalJoltage += findMaximumJoltageNew(bank, 12)
    
    return totalJoltage

if __name__ == '__main__':
    print(f'The answer is: {main()}')

