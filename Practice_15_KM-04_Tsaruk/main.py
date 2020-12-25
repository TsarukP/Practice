from factorial import factorial
from exp_root import exponentiation, root
from logarithm import logarithm

def main():
    print("MENU:")
    print("- enter 1 if you want to find factorial")
    print("- enter 2 if you want to find exponentiation(2 degree)")
    print("- enter 3 if you want to find exponentiation(3 degree)")
    print("- enter 4 if you want to find root(2 degree)")
    print("- enter 5 if you want to find root(3 degree)")
    print("- enter 6 if you want to find log")
    print("- enter 7 if you want to find ln")
    print("- enter 8 if you want to find lg")
    print()
    while True:
        variant = input()
        if variant == "1":
            print("enter the integer, which >= 0")
            while True:
                a = input()
                try:
                    a = int(a)
                    if a < 0:
                        print("invalid number")
                        continue
                    else:
                        result = factorial.fact(a)
                        print()
                        print("result:", result)
                        return result
                except ValueError:
                    print("invalid number")
        elif variant == "2":
            print("enter the number")
            while True:
                a = input()
                try:
                    a = float(a)
                    result = exponentiation.exp2(a)
                    print()
                    print("result:", result)
                    return result
                except ValueError:
                    print("invalid number") 
        elif variant == "3":
            print("enter the number")
            while True:
                a = input()
                try:
                    a = float(a)
                    result = exponentiation.exp3(a)
                    print()
                    print("result:", result)
                    return result
                except ValueError:
                    print("invalid number")   
        elif variant == "4":
            print("enter the number >= 0")
            while True:
                a = input()
                try:
                    a = float(a)
                    if a < 0:
                        print("invalid number")
                        continue
                    else:
                        result = root.root2(a)
                        print()
                        print("result:", result)
                        return result
                except ValueError:
                    print("invalid number")
        elif variant == "5":
            print("enter the number")
            while True:
                a = input()
                try:
                    a = float(a)
                    result = root.root3(a)
                    print()
                    print("result:", result)
                    return result
                except ValueError:
                    print("invalid number")         
        elif variant == "6":
            print("enter the base")
            while True:
                a = input()
                try:
                    a = float(a)
                    if a <= 0:
                        print("incorrect base")
                    elif a == 1:
                        print("incorrect base")
                    else:
                        break
                except ValueError:
                    print("incorrect base")
            print("enter the number")
            while True:
                b = input()
                try:
                    b = float(b)
                    if b <= 0:
                        print("incorrect number")
                    else:
                        result = logarithm.log(a, b)
                        print()
                        print("result:", result)
                        return result
                except ValueError:
                    print("incorrect number")    
        elif variant == "7":
            print("enter the number")
            while True:
                a = input()
                try:
                    a = float(a)
                    if a <= 0:
                        print("incorrect number")
                    else:
                        result = logarithm.ln(a)
                        print()
                        print("result:", result)
                        return result
                except ValueError:
                    print("incorrect number")                    
        elif variant == "8":
            print("enter the number")
            while True:
                a = input()
                try:
                    a = float(a)
                    if a <= 0:
                        print("incorrect number")
                    else:
                        result = logarithm.lg(a)
                        print()
                        print("result:", result)
                        return result
                except ValueError:
                    print("incorrect number")   
        else:
            print("incorrect")

if __name__ == "__main__":
    main()