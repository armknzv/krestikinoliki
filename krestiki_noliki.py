map = [1, 2, 3,
       4, 5, 6,
       7, 8, 9]
wins_cord = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]


def pole():
    for i in range(3):
        print(map[0 + i * 3], map[1 + i * 3], map[2 + i * 3])


def step(importt):
    while True:
        value = input('Куда поставить: ' + importt + ' ?')
        if not (value in '123456789'):
            print('ошибка ввода')

            continue
        if value == '':
            print('Введите число')
            continue

        value = int(value)
        if str(map[value - 1]) in 'xo':
            print('эта клетка уже занята')

            continue

        map[value - 1] = importt
        break

def chek_wins():
    for htr in wins_cord:
        if (map[htr[0] - 1] == map[htr[1] - 1] == map[htr[2] - 1]):
            return map[htr[1] - 1]
    else:
        return False


def main():
    counter = 0
    while True:
        pole()
        if counter % 2 == 0:
            step('x')
        else:
            step('0')
        if counter > 3:
            winner = chek_wins()
            if winner:
                pole()
                print(winner, ' выиграл')
                break
        counter += 1
        if counter > 8:
            pole()
            print('ничья')
            break


main()