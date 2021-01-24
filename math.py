numbers = []
does = []
i = 0
while i < 2 :
    number = int(input('Введите число : '))
    numbers.append(number)
    do = input('Введите знак : ')
    does.append(do)
    i = i + 1



if does[0] == '+':
    answer = numbers[0] + numbers[1]
    print(f'{numbers[0]} + {numbers[1]} = {answer}')
elif does[0] == '-':
    answer = numbers[0] - numbers[1]
    print(f'{numbers[0]} - {numbers[1]} = {answer}')
elif does[0] == '*':
    answer = numbers[0] * numbers[1]
    print(f'{numbers[0]} * {numbers[1]} = {answer}')
elif does[0] == '/':
    answer = numbers[0] / numbers[1]
    print(f'{numbers[0]} / {numbers[1]} = {answer}

