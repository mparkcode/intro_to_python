# for a range of numbers:
#if the number is divisible by 3 return fizz
#if the number is divisible by 5 return buzz
#if the number is divisible by 3 & 5 return fizzbuzz
# if not divisible by 3 or 5 return the number
# write the basic code, then refactor it into a reusable function



def fizzBuzz(n):
    for i in range(1, n+1):
        if i % 3 == 0 and i % 5 == 0:
            print('FizzBuzz')
        elif i % 5 == 0:
            print('Buzz')
        elif i % 3 == 0:
            print('Fizz')
        else:
            print(i)
    print("==========================")

fizzBuzz(6)
fizzBuzz(10)
fizzBuzz(44)
fizzBuzz(21)