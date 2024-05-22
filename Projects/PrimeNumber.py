import os
# prime(number): iterates number % (2 to number-1).
# if module != 0 for all, no divisors, number is prime. 
# else, its not and divisors are printed.
def prime(number):
    number = int(number)
    if number == 0: 
        print('0 is undefined.')
    elif number < 0:
        print(f'{number} excluded. Negatives don\'t count')
    else:
        divisors = []
        for i in range(2, number):
            if number % i == 0: 
                divisors.append(i)
        if len(divisors) == 0:
            print(f'{number} is prime.')
        else: 
            divisors_string = ', '.join(str(i) for i in divisors)
            print(f'{number} is not prime. Its divisible by 1, {divisors_string} and itself.')
        

while True:
    input_list = input("Enter integers separated by spaces: ").split()
    if not all(i.isdigit() for i in input_list):
        os.system('cls')
        print(f'Enter only integers. Entered {([i for i in input_list if not i.isdigit()])}.')
        continue
    if len(input_list) not in range(1, 15):
        os.system('cls')
        print(f'Max of 15 integers. Entered {(len(input_list) if len(input_list) > 0 else 'nothing')}.')
        continue
    sorted_list = sorted((set(int(i) for i in input_list)))
    os.system('cls')
    for i in sorted_list:
        prime(i)

