def dpMakeChange(coinValueList, change, minCoins, coinsUsed):
    for cents in range(change+1):
        coinCount = cents
        newCoin = 1
        for j in [c for c in coinValueList if c< cents]:
            if minCoins[cents-j] + 1 < coinCount:
                coinCount = minCoins[cents-j] + 1
                newCoin = j
        minCoins[cents] = coinCount
        coinsUsed[cents] = newCoin
    return minCoins[change]


def printCoins(coinsUsed, change):
    coin = change
    while coin>0:
        thisCoin = coinsUsed[coin]
        print(thisCoin)
        coin = coin - thisCoin
l = [0]*64
m = [0]*64

print(dpMakeChange([1,5,10,21,25], 63, l, m))
printCoins(m, change=63)
print(m)