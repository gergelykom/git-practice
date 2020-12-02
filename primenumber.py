def prime():
    print('Check if your number is prime')
    prnum = int(input('Enter the number you would like to check: '))
    if prnum > 1:
        for i in range(2,prnum):
            if (prnum % i) == 0:
                print('Your number is not prime, sorry:(')
                break
        else:
            print('Your number is a prime, Nice:)')

prime()