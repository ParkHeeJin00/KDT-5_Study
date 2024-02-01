# [연습문제] 12.4
camille = {
    'health': 575.6,
    'health_regen': 1.7,
    'mana': 338.8,
    'mana _regen': 1.63,
    'melee': 125,
    'attack_damage': 60,
    'attack speed': 0.625,
    'armor': 26,
    'magic_resistance': 32.1,
    'movement speed': 340}
print(camille['health'])
print(camille['movement speed'])

# [문제] 12.5
twoData = input()
keys, valuse = twoData.split(',')
keys = keys.split()
veluse = valuse.split()

if (len(keys) == 4 and len(veluse) == 4 ) or (len(keys) == 5 and len(veluse) == 5):
    print("입력 OK")
    dataDict = {}
    if len(keys) ==4:
        dataDict[keys[0]] = veluse[0]
        dataDict[keys[1]] = veluse[1]
        dataDict[keys[2]] = veluse[2]
        dataDict[keys[3]] = veluse[3]
    else:
        dataDict[keys[0]] = veluse[3]
        dataDict[keys[1]] = veluse[1]
        dataDict[keys[2]] = veluse[2]
        dataDict[keys[3]] = veluse[3]
        dataDict[keys[4]] = veluse[4]
else:
    print("입력된 데이터가 정확하지않습니다.")
