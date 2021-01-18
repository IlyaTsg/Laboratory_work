import os
#Функция перевода в 3ичную с.с
def In3NumSys(digit):
    new_digit = 0
    i = 0
    while digit>0:
        new_digit += (digit%3)*10**(i)
        digit //= 3
        i += 1
    return new_digit

#Функция перевода в 3ю уравновешенную с.с
def InNew3NumSys(digit):
    digit = list(str(In3NumSys(digit)))
    for i in range(len(digit)):
        if i == len(digit)-1 and int(digit[len(digit)-(i+1)]) > 1:
            if digit[len(digit)-(i+1)] == '2':
                digit[len(digit)-(i+1)] = '#'
                digit.insert(0, '1')
            elif digit[len(digit)-(i+1)] == '3':
                digit[len(digit)-(i+1)] = '0'
                digit.insert(0, '1')
        elif digit[len(digit)-(i+1)] == '2':
            digit[len(digit)-(i+1)] = '#'
            digit[len(digit)-(i+2)] = str(int(digit[len(digit)-(i+2)]) + 1)
        elif digit[len(digit)-(i+1)] == '3':
            digit[len(digit)-(i+1)] = '0'
            digit[len(digit)-(i+2)] = str(int(digit[len(digit)-(i+2)]) + 1)
    string_d = ''
    for i in digit:
        string_d += i
    return string_d

# Чётный по индексу в 3ю уравновешенную 
def EvenToThree(array_symbols):
    for i in range(len(array_symbols)):
        if i%2 != 0:
            array_symbols[i] = InNew3NumSys(array_symbols[i])
    return array_symbols

#Ф-я нахождения кода символа в алфавите
def code_symbols(string):
    string = string.upper()
    Array_symbols = []
    for symbol in string:
        Array_symbols.append(32-(1071-ord(symbol)))
    return Array_symbols

#Ф-я перевода из 10 в P-ю с.с
def from_10_to(x, number_system):
    if number_system == 1:
        number_system += 1
    next_x = 0
    i = 0
    while x > 0:
        next_x += (x%number_system)*10**(i)
        i += 1
        x //= number_system
    return next_x

#Ф-я первода  отриц. числа в доп.код
def dopcode(digit):
    i = 0
    digit_in_2 = 0

    while digit > 0:
        digit_in_2 += (digit%2)*10**(i)
        i += 1
        digit //= 2

    digit = list(str(digit_in_2))
    len_8 = 8 - len(digit)

    for i in range(len_8):
        digit.insert(0, '0')

    for i in range(8):
        if digit[i] == '1':
            digit[i] = '0'
        else:
            digit[i] = '1'

    digit = int(''.join(digit), 2) + 1

    i = 0
    digit_in_2 = 0
    while digit > 0:
        digit_in_2 += (digit%2)*10**(i)
        i += 1
        digit //= 2
    digit = digit_in_2
    
    return digit

#Функция перевода 1-го числа в с.с 2-го, 3-го в доп.код и т.д
def change_num_syst(Array_symbols):
    flag = True
    for i in range(0, len(Array_symbols)):
        if i%2 == 0:
            if flag:
                Array_symbols[i] = from_10_to(Array_symbols[i], Array_symbols[i+1])
                flag = False
            else:
                Array_symbols[i] = dopcode(Array_symbols[i])
                flag = True
    return Array_symbols

#функция сравнения ответа пользователя с верным
def compare(enter, right, ball):
    cnt = 0
    len_mass = len(right)
    if len(enter) != len(right):
        print("К сожалению, неверно. -1 балл")
        ball -= 1
        check = False
    else:
        for i in range(len_mass):
            if right[i] == enter[i]:
                cnt += 1
        if cnt == len_mass:
            print("Верно!")
            if (ball > 4) or (ball == 0):
                print("++" + str(ball) + "баллов")
            elif ball > 1:
                print("++" + str(ball) + "балла")
            else:
                print("++" + str(ball) + "балл")
            check = True
        else:
            print("К сожалению, неверно. -1 балл")
            ball -= 1
            check = False
    return [ball, check]

#Ф-я ввода корректного слова
def correct_word():
    flag = False
    word = input("Введите любое русское слово: ")
    while flag == False:
        flag = True
        if word == "":
            flag = False
        else:
            for i in word:
                if (1040>ord(i) or ord(i)>1103) and ord(i)!=1025 and ord(i)!=1105:
                    flag = False
                    break
        if flag == False:
            os.system('cls')
            print("Вы ввели некорректное слово!!!")
            word = input("Введите любое русское слово: ")
    return word

#Основная программа
def main():
    resalt = 0
    print("Добро пожаловать! Эта игра создана для проверки знаний студентов.\nПо итогу игры Вам будет выставлена оценка. Следуйте указаниям. Успехов!")
    
    word = correct_word() #Ввод корректного слова

    os.system('cls')

    Arr = code_symbols(word)#Полученение списка кодов букв
    print("Первое задание.\nВведите номера букв по алфавиту, разделяя их пробелом, согласно их расположению в слове.")

    mass_ball_flag = [10, False]
    #Повтор, пока не будет введен верный ответ или кол-во баллов не станет 0
    while mass_ball_flag[0] != 0 and mass_ball_flag[1] == False:
        #Ввод ответа пользвателем
        enter = list(map(int,input().split()))
        mass_ball_flag = compare(enter, Arr, mass_ball_flag[0])
    resalt = resalt + mass_ball_flag[0]
    if resalt > 0:
        print("Неплохо сработано!\nА теперь реальное задание.")
    else:
        print("Вот верный ответ:", *Arr)
        print("Кажется, Вам стоит потренировать внимательность. Но это была разминка.\nА теперь реальное задание.\nНеобходимо изменить строку следующим образом:")
    
    input()
    os.system('cls')

    print("Второе задание.")
    print("a)Перевести первое число в систему счисления с основанием равному второму.")
    print("b)Умножить третье число на -1 и перевеси его в дополнительный код.")
    print("Если в Вашем слове больше 4 букв, повторяйте операцации до конца длины слова.")
    print("Если для очередного элемента отсутствует с.с, в которую его нужно перевести, то умножте его на -1 и переведите в дополнительный код.")
    print("Введите полученную последовательность, разделяя элементы пробелом.")

    Arr = change_num_syst(Arr) #Перевод 1-го числа в с.с 2-го, 3-го в доп.код и т.д

    #Повтор, пока не будет введен верный ответ или кол-во баллов не станет 0
    mass_ball_flag = [10, False]
    while mass_ball_flag[0] != 0 and mass_ball_flag[1] == False:
        #Ввод ответа пользвателем
        enter = list(map(int,input().split()))
        mass_ball_flag = compare(enter, Arr, mass_ball_flag[0])
    resalt = resalt + mass_ball_flag[0]
    if mass_ball_flag[0] > 0:
        print("Молодец!")
    else:
        print("Вот верный ответ:", *Arr)
        print("Вам стоит лучше разобраться в теме.")

    input()
    os.system('cls')

    print("Переведите элементы с четными индексами Вашей последовательности в троичную уравновешенную с.с.")
    print("Введите измененную последовательность. Элементы разделяйте пробелом.")

    Arr = EvenToThree(Arr) #Перевод всех элементов с чётными индексами в троично-уравновешенную с.с
    for i in range(len(Arr)): Arr[i] = str(Arr[i])

    #Повтор, пока не будет введен верный ответ
    mass_ball_flag = [10, False]
    while mass_ball_flag[0] != 0 and mass_ball_flag[1] == False:
        #Ввод ответа пользвателем
        enter = list(map(str, input().split()))
        mass_ball_flag = compare(enter, Arr, mass_ball_flag[0])
    resalt = resalt + mass_ball_flag[0]
    if mass_ball_flag[0] > 0:
        print("Получилось!\nЭто было последнее задание.")

    input()
    os.system('cls')

    for i in range(len(Arr)):
        Arr[i] = str(Arr[i])
    password = ""
    for i in Arr:
        for j in i:
            password += j

    print("Вот конечный правильный ответ:", password)

    resalt = (resalt*100)/30
    if resalt < 60:
        print("Очень плохо! Ваша оценка 2. В следующий раз готовьтесь тщательнее.")
    elif 60 <= resalt < 80:
        print("Так себе. Ваша оценка 3. В следующий раз готовьтесь тщательнее.")
    elif 80 <= resalt < 90:
        print("Неплохо! Ваша оценка 4. Есть, куда расти.")
    elif resalt >= 90:
        print("Отлично! Ваша оценка 5. Сегодня Вы действительно постарались. Так держать!")
    print("Проверка окончена.")
        
main()
