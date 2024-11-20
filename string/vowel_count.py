def vowel_count(text: str) -> int:
    count = 0
    vowels = list('aeiouAEIOU')
    for char in text:
        if char in vowels:
            count += 1
    return count

def vowels_percentage(text: str) -> float:
    return vowel_count(t) * 100 / len(t)


t = input('Inserisci il testo: ')
n_vowel = vowel_count(t)
print(f'Numero di vocali presenti nel testo "{t}" = {n_vowel}')
p_vowels = vowels_percentage(t)
print(f'La percetuale di vocali presenti nel testo è {p_vowels:.2f}%')