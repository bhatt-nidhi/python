num=int(input("enter any number : "))
for i in range(num):
    if(num%2==0):
        print(f"the number {num} is even:")
        break
    else:
        print("the number is odd")
        break