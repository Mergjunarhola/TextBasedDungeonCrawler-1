#ég var hér aðeins að fikta með print hear commandið
"""
from time import sleep
Dodilidoo="-\|/"
Tr=[]
p=0
for x in range(20):
    Tr.append([])
    for y in range(20):
        Tr[x].append(0)
        Tr[x][y]=random.randint(0, 3)
while True:
    for x in range(2,21):
        for y in range(2,21):
            Tr[x-2][y-2]=(Tr[x-2][y-2]+1)%4
            print_at(x,y,Dodilidoo[(Tr[x-2][y-2])%4])
    sleep(0.1)
"""
