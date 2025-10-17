from itertools import combinations as comb

def findSteps(Start,End) -> int:
    starti=wheel.index(Start)
    endi=wheel.index(End)
    temp=abs(endi-starti)
    temp2=26-abs(starti-endi)
    return temp if temp<temp2 else temp2


list=["R","I","T","A","N","G","L","E"]
wheel=[]
for x in  range(65,91):
    wheel.append(chr(x))

combinations=comb(list,len(list))
totals=[]
for x in combinations:
    total=0
    for y in range(len(x)-1):
        total+=findSteps(x[y-1],x[y])
    totals.append(total)

maximum=max(totals)
minimum=min(totals)
print(maximum*minimum)
