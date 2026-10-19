import random

def guessing_number():
    mys_num = int(random.randint(1,100))
    while True:
        try:
            n = int(input("Enter your guess: "))
            if n == mys_num:
                print("You win!")
                break
            elif n > mys_num:
                print("Your guess is too high")
            elif n < mys_num:
                print("Your guess is too low")
            else:
                print("Error: Please enter a number between 1 and 100")
        except ValueError:
            print("Error: Please enter a number not string or a character")

def demsochan():
    for x in range(1,101):
        if x%2==0:
            print(x, end=" ")

    print("\n")

def bangcuuchuong():
    while True:
        try:
            n = int(input("Enter the multiplication table you want: "))
            if 1<= n <=9:
                for x in range(1,11):
                    kq = n*x
                    print(f"{n}x{x}={kq}")
                break
            else:
                print("Error: Please enter a number between 1 and 9")
        except ValueError :
            print("Error: Please enter a number not string or a character")
if __name__ == '__main__':
    demsochan()
    bangcuuchuong()
    guessing_number()
