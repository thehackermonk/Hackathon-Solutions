n=int(input())
geometry=[]
face=0
for i in range(n):
    geometry.append(input())

for geo in geometry:
    if geo=='Tetrahedron':
        face+=4
    if geo=='Cube':
        face+=6
    if geo=='Octahedron':
        face+=8
    if geo=='Dodecahedron':
        face+=12
    if geo=='Icosahedron':
        face+=20

print(face)