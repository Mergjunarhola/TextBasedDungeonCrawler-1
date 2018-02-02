from random import randint

def search():
    while True:
        ran1=randint(1,99)
        ran2 = randint(1, 99)
        if ground[ran1][ran2]==".":
            break
    return [ran1,ran2]

loops= 40#hvað margar einigar eru settar inn
startloop=loops
maxwidth=100 #bæði eru max hæðin og breiddin á gridinu
maxheigt=100
ground=[] #carry-er fyrir gridið

textfile="Map_1.txt"#file-ið sem þetta verður ritað sem

rh=0
rw=0
work=False
#ef ég vill setja hluti á mapið að handahófi
Hlutir=True
En=5
It=20
for x in range(maxwidth):
    ground.append([])
    for y in range(maxheigt):
        ground[x].append(" ")
while True:
    star= randint(3,4)
    if startloop == loops:
        rh=5
        rw=maxwidth//2
        work=True
    else:
        while True:
            rh=randint(1+star,99-star)
            rw=randint(1+star,99-star)
            if ground[rh][rw]==".":
                #if ground[rh+1][rw]=="#" or ground[rh-1][rw]=="#" or ground[rh][rw-1]=="#" or ground[rh][rw+1]=="#":
                if (ground[rh + 1][rw] + ground[rh - 1][rw] + ground[rh][rw - 1] + ground[rh][rw + 1]).count("#")>0 :
                    work=True
                    break



    if work:
        for x in range(rh-star-1,rh+star+1):
            for y in range(rw-star-1,rw+star+1 ):
                if ground[x][y]!="S" and ground[x][y]!=".":#verður ansi merkilegt ef maður tekur testið fyrir punkti
                    ground[x][y] = "#"
        for x in range(rh-star,rh+star):
            for y in range(rw-star,rw+star):
                if ground[x][y]!="S":
                    ground[x][y] = "."
        if startloop == loops:
            ground[rh][rw]="S"
        loops=loops-1
        work=False
    if loops==0:
        if Hlutir:
            for x in range(En):
                S=search()
                ground[S[0]][S[1]]="E"
            for x in range(It):
                S=search()
                ground[S[0]][S[1]]="I"
        break



skra = open(textfile, "w", encoding="UTF-8")
skra.write("\n".join(list(map("".join ,ground))))
skra.close()

