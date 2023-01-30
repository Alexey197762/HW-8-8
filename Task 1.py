alphabet = "абвгдежзийклмнопрстуфхцчшщъыьэюяабвгдежзийклмнопрстуфхцчшщъыьэюя"
encrypt = input("Введите сообщение: ")
key = int(input("Введите ключ(Номер от 1-32): "))
encrypt = encrypt.lower()
encrypted =""
for letter in encrypt:
    position = alphabet.find(letter)
    newPosition = position + key
    if letter in alphabet:
        encrypted = encrypted + alphabet[newPosition]
    else:
        encrypted = encrypted + letter
print("Ваш шифр - это: ", encrypted)            
    