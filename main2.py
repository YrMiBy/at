def count_vowels(s):
    # Определяем список гласных букв
    vowels = 'аеоАЕИОeiouyIOUY'
    count = 0

    # Проходим по каждому символу в строке
    for char in s:
        if char in vowels:
            count += 1

    return count


