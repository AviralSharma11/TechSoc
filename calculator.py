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
    x %= 360
    x = x * 3.141592653589793238462643383279502884197 / 180
    sinx = 0
    cosx = 0
    for i in range (1, 86):
        sign = pow(-1 , i+1)
        sinx += sign *(((pow(x,(2*i-1))) / fact(2*i-1)))
        cosx += sign*((pow(x,(2*i-2)))/fact(2*i-2))
        i += 2
        
    out_sinx = "{:.3f}".format(sinx)
    out_cosx = "{:.3f}".format(cosx)
    out_tanx = "{:.3f}".format(sinx/cosx)
    out_cosecx = "{:.3f}".format(1/sinx)
    out_secx = "{:.3f}".format(1/cosx)
    out_cotx = "{:.3f}".format(cosx/sinx)
    print(f"sin of given x is",{out_sinx})
    print(f"cos of given x is",{out_cosx})
    print(f"tan of given x is",{out_tanx})
    print(f"cosec of given x is",{out_cosecx})
    print(f"sec of given x is",{out_secx})
    print(f"cot of given x is",{out_cotx})


    









    