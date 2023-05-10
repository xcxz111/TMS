# При помощи функции filter() из кортежа слов отфильтровать только те,
# которые являются полиндромами (которые читаются одинаково в обе стороны).

dromes = ("demigod", "rewire", "madam", "freer", "anutforajaroftuna", "kiosk")

palindromes = list(filter(lambda word: word == word[::-1], dromes))

print(palindromes)
