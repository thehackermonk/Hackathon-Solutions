n=int(input())
output=""
for i in range(1,n):
    if i%2==1:
        output+="I hate that "
    else:
        output+="I love that "
if n%2==0:
    output+="I love it"
if n%2==1:
    output+="I hate it"
print(output)