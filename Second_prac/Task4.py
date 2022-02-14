# №4
rand_positions = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']

for elements in rand_positions:
    employee = elements.split()[-1]
    phrase = employee.capitalize()
    print("Привет, " + phrase + "!")