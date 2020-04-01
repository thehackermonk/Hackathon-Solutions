n=int(input())
response=[]
response=list(map(int,input().strip().split(' ')[:n]))

opinion='EASY'

if 1 in response:
    opinion='HARD'

print(opinion)