seats = 8

while seats > 0:
    print(f" {seats}avelabal sites ")
    booking=input("booking (yes/no)").lower()

    if booking == "yes":
        seats -=1
        print(f"awailabal")
    elif booking=="no":
        print("not booking cansal")
        break
    else:
        print("all setes or booked")

#new yer count down
i=10
while i>=1:
    x=1
    while x<=i:
        print(x,"happy new year " , end="-")
        x +=1
    print("")
    i -=1

