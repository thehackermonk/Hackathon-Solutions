cardOnTable=input()
cardInHand=input().split()

output='NO'

for letter in cardInHand:
    if cardOnTable[0]==letter[0]:
        output='YES'
    if cardOnTable[1]==letter[1]:
        output='YES'

print(output)