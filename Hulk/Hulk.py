n=int(input())
output=""
for i in range(n):
    if i%2==0:
        output+="I love it "
    else:
        output+="I hate that "
print(output)