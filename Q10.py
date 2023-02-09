try :
    print(" file open")
    try:
        a=int(input())
        b=0
        c=a//b
    except ValueError:
        print(" enter the correct data type value ")
except ArithmeticError:
    print(" dividion is not possilbe")
    