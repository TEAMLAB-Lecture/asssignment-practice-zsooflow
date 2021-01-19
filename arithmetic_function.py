def addition(a, b):

    # Output:
    #   두 값의 합
    result = a + b

    return result


def minus(a, b):

    # Output:
    #   두 값의 차
    result = a - b

    return result


def multiplication(a, b):

    # Output:
    #   두 값의 곱
    result = a * b

    return result


def division(a, b):

    # Output:
    #   a를 b로 나눈 값
    result = a / b

    return result


def main():
    print ("Addition Test")
    print (addition(3,5)) # Expected Result: 8
    print (addition(10,5) == 15) # Expected Result: True
    print ("Addition Test Closed \n")


    print ("Minus Test")
    print (minus(3,5)) # Expected Result: -2
    print (minus(10,5) == 5) # Expected Result: True
    print (minus(10,15) == 5) # Expected Result: False
    print ("Addition Test Closed \n")

    print ("Multiplication Test")
    print (multiplication(3,5)) # Expected Result: 15
    print (multiplication(10,5) == 50) # Expected Result: True
    print (multiplication(10,-3) == 20) # Expected Result: False
    print ("Addition Test Closed \n")

    print ("division Test")
    print (division(5,5)) # Expected Result: 1
    print (division(5,4)) # Expected Result: 1.25
    print (division(10,5) == 2) # Expected Result: True
    print (division(10,-3) == 0.33333) # Expected Result: False
    print ("division Test Closed \n")


if __name__ == "__main__":
    main()
