def symbol_counter(text, symbol):
    counter = 0
    for t in text:
        if t == symbol:
            counter += 1
    return counter
