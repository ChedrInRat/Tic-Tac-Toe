"""
Наша игра почти готова! Теперь давайте объединим то, что мы узнали на предыдущих этапах,
чтобы создать игру в крестики-нолики, в которую два игрока могут играть от начала (с пустой сеткой) до конца
(пока не будет ничья или один из игроки выигрывают).
Первый игрок должен играть за X, а его противник - за O.
Цели
На этом этапе вы должны написать программу, которая:
Печатает пустую сетку в начале игры.
Создает игровой цикл, в котором программа просит пользователя ввести координаты ячейки,
анализирует ход на предмет правильности и показывает сетку с изменениями, если все в порядке.
Завершает игру, когда кто-то выигрывает или ничья.
Окончательный результат нужно вывести в конце игры.
Удачи!

Проект был изменен. Теперь координаты начинаются с верхнего левого угла. Посмотрите внимательно на примеры.
"""
"""
---------
|       |
|       |
|       |
---------

"""


def PrintField(field):
    print(f"---------\n"
          f"| {field[0][0]} {field[0][1]} {field[0][2]} |\n"
          f"| {field[1][0]} {field[1][1]} {field[1][2]} |\n"
          f"| {field[2][0]} {field[2][1]} {field[2][2]} |\n"
          f"---------\n")


def UserInput(field, player):
    inp = input("Enter the coordinates: ")
    data = inp.split(' ')

    if data[0].isdigit() and data[1].isdigit():
        if (3 >= int(data[0]) >= 1) and (3 >= int(data[1]) >= 1):
            if field[int(data[0]) - 1][int(data[1]) - 1] == '_':
                field[int(data[0]) - 1][int(data[1]) - 1] = player
                if player == 'X':
                    player = 'O'
                else:
                    player = 'X'
            else:
                print("This cell is occupied! Choose another one!")
        else:
            print("Coordinates should be from 1 to 3!")
    else:
        print("You should enter numbers!")

    return player, field


def Status(field):

    def Win(field):
        win = False
        winplayer = '_'

        if ((field[0][0] == field[1][1] == field[2][2])
            or (field[0][2] == field[1][1] == field[2][0])) \
                and (field[1][1] != '_'):

            win = True
            winplayer = field[1][1]

        else:
            for i in range(3):
                if field[i][0] != '_' \
                        and (field[i][0] == field[i][1] == field[i][2]):

                    win = True
                    winplayer = field[i][0]

                elif field[0][i] != '_' \
                        and (field[0][i] == field[1][i] == field[2][i]):

                    win = True
                    winplayer = field[0][i]

        if win:
            print(f"{winplayer} wins")

        return win

    def Draw(field):
        draw = False
        countN = 0
        for i in range(3):
            for j in range(3):
                if field[i][j] == '_':
                    countN += 1

        if countN == 0:
            draw = True
            print("Draw")

        return draw

    return Win(field) or Draw(field)


field = [['_' for j in range(3)] for i in range(3)]
player = 'X'

while True:
    PrintField(field)
    if Status(field):
        break
    player, field = UserInput(field, player)

