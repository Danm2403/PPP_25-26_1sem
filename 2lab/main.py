

if __name__ == "__main__":
    def convert_currency():
    # Ввод данных
    rates_input = input("Введите курсы валют (например: рубль доллар 0.01, доллар евро 1): ")
    conversion_input = input("Введите конверсию (например: 1000 рубль доллар евро): ")
    
    # Разбираем курсы валют
    rates = {}
    for rate_pair in rates_input.split(','):
        parts = rate_pair.strip().split()
        if len(parts) == 3:
            from_curr, to_curr, rate = parts
            rates[(from_curr, to_curr)] = float(rate)
    
    # Разбираем запрос на конверсию
    parts = conversion_input.split()
    amount = float(parts[0])
    currencies = parts[1:]
    
    # Проверяем, достаточно ли валют для конверсии
    if len(currencies) < 2:
        print("Ошибка: нужно указать хотя бы две валюты для конверсии")
        return
    
    # Выполняем конверсию пошагово
    result = []
    current_amount = amount
    
    for i in range(len(currencies) - 1):
        from_curr = currencies[i]
        to_curr = currencies[i + 1]
        
        # Прямой курс
        if (from_curr, to_curr) in rates:
            rate = rates[(from_curr, to_curr)]
            new_amount = current_amount * rate
            result.append(f"{current_amount} {from_curr} -> {new_amount} {to_curr}")
            current_amount = new_amount
        
        # Обратный курс
        elif (to_curr, from_curr) in rates:
            rate = 1 / rates[(to_curr, from_curr)]
            new_amount = current_amount * rate
            result.append(f"{current_amount} {from_curr} -> {new_amount} {to_curr}")
            current_amount = new_amount
        
        else:
            print(f"Ошибка: не найден курс конверсии из {from_curr} в {to_curr}")
            return
    print("Результат конверсии:")
    for step in result:
        print(step)
    print(f"Итоговая сумма: {current_amount} {currencies[-1]}")

convert_currency()
