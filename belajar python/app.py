import os

def header():
    os.system("clear")
    print(f"{'PROGRAM FOR CALCULATION THE AREA':^40}")
    print(f"{'AND PRIMETER OF RECTANGLES':^40}")
    print(f"{'-'*40:^40}")

def inputValue():
    width = int(input("Insert width value = "))
    length = int(input("Insert length value = "))

    return width, length

def countAr(width, length):
    return width*length

def countAd(width, length):
    return 2*(width+length)

def display(message, value):
    print(f"{message} calculation result = {value}")

while True:
    header()
    WIDTH, LENGTH = inputValue()
    display("Around", countAd(length=LENGTH, width=WIDTH))
    display("Area", countAr(length=LENGTH, width=WIDTH))

    isContinue = input("Do you want continue (y/n)? ")
    if(isContinue == 'n'):
        break

print("Program complated, thank you")