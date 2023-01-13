import sys
countTicket = int(input("Введите кол-во билетов: "))
s = 0
tickets = []

if countTicket <= 0:
    print("Укажите 1 или более билетов")
    sys.exit()

for i in range(countTicket):
    total = 0
    age = int(input("Введите возраст: "))
    if age >=0 and age < 18:
        total = 0
    elif age >= 18 and age <= 25:
        total = 990
    elif age > 25:
        total = 1390
    else:
        print("Укажите правильный возраст")
        sys.exit()
    
    tickets.append(total)

if countTicket > 3:
    s = sum(tickets) - sum(tickets)/100*10
else:
    s = sum(tickets)

if countTicket == 1:
    print("Стоимость вашего билета:", s)
else:
    print("Стоимость ваших билетов:", s)