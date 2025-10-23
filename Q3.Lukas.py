number=int("11110",7)
count=0
while number<int("100000",7):
    number+=int("1",7)
    string=str(number)
    if "0" not in str(number):
        temp=int(string)
        if temp%25==0:
            count+=1
            print("Added count",number)
        else:
            print("skipped not div",number)
    else:
        print("Skipped 0")