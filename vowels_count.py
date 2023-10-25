import doctest

def vowels_count(text):
    '''
    >>> vowels_count('fratta')
    2
    >>> vowels_count('Ombrelli')
    3
    >>> vowels_count('pAppagallO')
    4
    >>> vowels_count('vrtkz')
    0
    '''
    counter = 0
    vowels = ['a', 'e', 'i', 'o', 'u']
    for t in text.lower():
        if t in vowels:
            counter += 1
    return counter

print(doctest.testmod())