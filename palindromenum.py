def is_palindrome(x):

    if x < 0 or (x % 10 == 0 and x != 0):
        return False

    reverted_number = 0
    while x > reverted_number:
        reverted_number = reverted_number * 10 + x % 10
        print(reverted_number)
        x //= 10

    print(x, reverted_number)
    return x == reverted_number or x == reverted_number // 10

is_palindrome(864212468)

#the other way to solve is divide it by 10, 100 etc..
#Finding the initial 10 power requires another loop
#while(x >= 10*div) div *=10  (div=1 initially) 
