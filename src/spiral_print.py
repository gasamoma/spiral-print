def print_spiral(matrix):
    x_len = len(matrix)
    if x_len == 0:
        return
    y_len = len(matrix[0])
    direction = 'r'
    x = 0
    y = 0
    # r right means x+1
    # l left means x-1
    # u up means y-1
    # d down means y+1

    max_top = 0
    max_bot = y_len - 1
    max_left = 0
    max_right = x_len - 1

    # r max_top + 1
    # l max_bot - 1
    # u max_left + 1
    # d max_right - 1
    answer = ""
    while max_top <= max_bot and max_left <= max_right:
        answer += str(matrix[x][y])+" "
        if direction == 'r':
            x += 1
            if x == max_right:
                direction = 'd'
                max_top += 1
        if direction == 'l':
            x -= 1
            if x == max_left:
                direction = 'u'
                max_bot -= 1

        if direction == 'u':
            y -= 1
            if y == max_top:
                direction = 'r'
                max_left += 1

        if direction == 'd':
            y += 1
            if y == max_bot:
                direction = 'l'
                max_right -= 1
    return answer
