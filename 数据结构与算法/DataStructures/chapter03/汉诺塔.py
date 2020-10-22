def moveTower(height, fromPole, toPole, withPole):
    if height>=1:
        moveTower(height-1, fromPole, withPole, toPole)
        moveDisk(fromPole, toPole)
        moveTower(height-1, withPole, toPole, fromPole)

def moveDisk(fp, tp):
    print(f'moving : {fp} -----> {tp}')

moveTower(3,"最初塔","目标塔","中间塔")