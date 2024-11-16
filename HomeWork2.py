# Список строк для первой операции
first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
# Список строк для второй операции
second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']

# Результат первой операции:
# Получаем список длин слов из first_strings, если длина слова >= 5
first_result = [
    len(word)  # Добавляем длину каждого слова
    for word in first_strings  # Проходим по каждому слову из first_strings
    if len(word) >= 5  # Добавляем слово, если его длина >= 5
]
print(first_result)  # Печатаем получившийся список длин слов

# Результат второй операции:
# Формируем список кортежей из слов из first_strings и second_strings, если их длина одинаковая
second_result = [
    (word_1, word_2)  # Создаем кортеж из двух слов
    for word_1 in first_strings  # Проходим по каждому слову из first_strings
    for word_2 in second_strings  # Проходим по каждому слову из second_strings
    if len(word_1) == len(word_2)  # Добавляем пару, если длина слов одинаковая
]
print(second_result)  # Печатаем результат — список кортежей

# Результат третьей операции:
# Создаем словарь из слов из обоих списков, если длина слова четная
third_result = {
    word: len(word)  # Добавляем слово как ключ, а его длину как значение
    for word in first_strings + second_strings  # Проходим по всем словам из обоих списков
    if len(word) % 2 == 0  # Добавляем слово, если его длина четная
}
print(third_result)  # Печатаем результат — словарь с словами и их длинами
