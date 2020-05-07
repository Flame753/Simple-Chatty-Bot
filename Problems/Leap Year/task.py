# put your python code here
year = int(input())


def leep_check(num):
    if num % 4 == 0 and num % 100 != 0:
        return 'Leap'
    elif num % 4 == 0 and num % 400 == 0:
        return 'Leap'
    else:
        return 'Ordinary'


print(leep_check(year))

