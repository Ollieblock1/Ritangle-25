from itertools import combinations
from itertools import combinations_with_replacement

dice=[1,2,3,4,5,6]
perms=combinations_with_replacement(dice,5)
temp=list(perms)
combinationNum=len(temp)
count=0
totalCount=0
for x in temp:
    possible=False
    temp2=list(x)
    for y in combinations(temp2,5):
        string=""
        for z in y:
            string=string+str(z)
            if int(string)%25==0:
                possible=True
                count+=1
                break
        if possible:
            break
    totalCount+=1
    if totalCount%100000==0:
        print(f"Checked: {totalCount}, Working: {count}, ToDo: {combinationNum-totalCount}")
print(count/combinationNum)
