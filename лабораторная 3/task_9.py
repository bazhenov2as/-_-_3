salary = 5000  # зарплата
spend = 6000  # траты
months = 10  # количество месяцев
increase = 0.03  # рост цен

need_money = 0  # количество денег, чтобы прожить 10 месяцев
month = 1
# TODO Оформить решение
while month <= months:
    need_money = need_money + spend * (1 + increase) ** (month - 1) - salary
    month = month + 1
print(round(need_money))
