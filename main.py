list = [1,5,8,10,25,37,46,55,63,72,81,93,100]
question = int(input("What number are you searching for? "))

def binary_search(n):
    low = 0
    high = len(list)-1
    while low <= high:
        medium = (low + high)//2
        if n < list[medium]:
            high = medium-1
        elif n > list[medium]:
            low = medium + 1
        else:
            print("Number is in index {}".format(medium))
            return
    else:
        print("Number is not in list")

binary_search(question)