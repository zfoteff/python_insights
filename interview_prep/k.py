def multiply(a, b):
    isNegative = False
    result = 0
    count = 0

    if int(a) == 0 or int(b) == 0:
        print(str(result))
        return result

    if (a[0] == '-' or b[0] == '-'):
        isNegative = True

    while (count < int(b)):
        result += int(a)
        count += 1

    if isNegative:
        print(str(result))
        return (result - (2 * result))

    print(str(result))
    
    return result

def main():
    multiply("1", "2")
    multiply("6", "7")
    multiply("2", "0")
    multiply("0", "11")
    multiply("-3", "7")
    multiply("-5", "-5")
    multiply("6", "-2")

main()
    
