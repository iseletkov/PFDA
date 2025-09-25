
count = 0
 
def move(player, number):
    """
        принимает имя игрока и его число, обновляет общий счёт
    """
    global count

    if number <= 0:
        return

    if player == 'Петя':
        count += number
    if player == 'Ваня':
        count -= number


def game_over():
    """
        возвращает результат: 'Петя', 'Ваня' или 'Ничья'.
    """
    global count

    if count < 0:
        return 'Ваня'
    if count > 0:
        return 'Петя'
    
    return 'Ничья'


move('Петя', 3)
move('Ваня', 4)
print(game_over())