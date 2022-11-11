# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход.
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""


# С ботом

def Player(player, candies):
    while True:
        try:
            candy = int(
                input(f'{player}: Возьмите контфеты (не более 28 штук за один ход): '))
            if 0 < candy < 29:
                print(f'{player} взял {candy} конфент')
                if candies - candy < 0:
                    print(f'Столько конфет нет, в корзине осталось: {candies}')
                else:
                    candies -= candy
                    print(f'В корзине осталось {candies} конфет')
                    return candies
            else:
                print('Нельзя взять больше 28 конфет')
        except ValueError:
            print('Укажите значение в числовом формате')


def Computer(candies):
    candy = candies % 28
    if candy == 0:
        print(f'Компьтер взял 28 конфент')
        candies -= 28
        print(f'В корзине осталось {candies} конфет')
        return candies
    else:
        if 1 < float(candies/28) < 2:
            print(f'Компьтер взял {candy - 1} конфент')
            candies -= candy - 1
            print(f'В корзине осталось {candies} конфет')
            return candies
        else:
            print(f'Компьтер взял {candy} конфент')
            candies -= candy
            print(f'В корзине осталось {candies} конфет')
            return candies


player1 = 'Вадим'
candies = 2021
while candies > 0:
    candies = Player(player1, candies)

    if candies > 0:
        candies = Computer(candies)
        if candies == 0:
            print(f'{player1} вы проиграли!')
    else:
        print(f'{player1} вы победили!')
