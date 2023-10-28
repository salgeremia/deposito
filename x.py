def x(text):
    step = 1
    for i in range(len(text)):
        print(text[i:step+i])
        step += 1

x('water')