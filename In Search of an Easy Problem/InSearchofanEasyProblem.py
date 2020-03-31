n=int(input())
responses=[]
responses=list(map(int,input().strip().split(' ')[:n]))

opinion='EASY'

for response in responses:
    if response==1:
        opinion='HARD'

print(opinion)