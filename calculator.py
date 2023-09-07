a = int(input("Arithemetic(0) or Trigonometric(1)? "))
if a == 0:
    print("Arithemetic is chosen")
    b=  float(input("enter number #1 "))
    c=  float(input("enter number #2 "))
    print(f"sum is",{b+c})
    print(f"differnce is",{b-c})
    print(f"multiplication is",{b*c})
    print(f"division is",{b/c})

elif a == 1:
    print("Trigonometric is chosen")
    def fact(num):
        if num in [0,1]:
            return 1
        else:
            return (num * fact(num-1))
    
    x = float(input("What is x? "))
    x = x * 3.141592653589793238462643383279502884197 / 180
    sinx = 0
    cosx = 0
    for i in range (1,86):
        sign = pow(-1 , i+1)
        sinx += sign * (pow(x,(2*i-1))) / fact(2*i-1)
        cosx += sign*(pow(x,(2*i-2)))/fact(2*i-2)
    print(f"sin of given x is",{sinx})
    print(f"cos of given x is",{cosx})
    print(f"tan of given x is",{sinx/cosx})
    print(f"cosec of given x is",{1/sinx})
    print(f"sec of given x is",{1/cosx})
    print(f"cot of given x is",{cosx/sinx})

    









    