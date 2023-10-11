money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов
months = 0 #counter
while money_capital >= 0:
    money_capital += salary - spend
    spend *= (1 + increase)
    months += 1
    if money_capital < 0:  # Если в последнем цикле подушка стала отрицательной
        months -= 1  # значит этот месяц уже не учитывается

print("Количество месяцев, которое можно протянуть без долгов:", months)
