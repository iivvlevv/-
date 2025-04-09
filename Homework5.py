def convert_to_12_hour_format(hours, minutes):
    """
    Конвертирует время из 24-часового формата в 12-часовой с указанием AM или PM.
    
    :param hours: Часы в 24-часовом формате.
    :param minutes: Минуты.
    :return: Время в 12-часовом формате.
    """
    # Определяем AM или PM
    if hours == 0:
        return f"12:{minutes:02} AM"
    elif hours == 12:
        return f"{hours}:{minutes:02} PM"
    elif hours > 12:
        return f"{hours % 12}:{minutes:02} PM"
    else:
        return f"{hours}:{minutes:02} AM"

# Примеры использования
print(convert_to_12_hour_format(14, 30))  # Выводит: "2:30 PM"
print(convert_to_12_hour_format(0, 45))   # Выводит: "12:45 AM"
print(convert_to_12_hour_format(12, 0))   # Выводит: "12:00 PM"
print(convert_to_12_hour_format(6, 15))   # Выводит: "6:15 AM"

# Альтернативная реализация с использованием тернарного оператора
def convert_to_12_hour_format_alt(hours, minutes):
    period = " AM" if hours < 12 else " PM"
    if hours == 0:
        hours = 12
    elif hours > 12:
        hours %= 12
    return f"{hours}:{minutes:02}{period}"

# Примеры использования альтернативной реализации
print(convert_to_12_hour_format_alt(14, 30))  # Выводит: "2:30 PM"
print(convert_to_12_hour_format_alt(0, 45))   # Выводит: "12:45 AM"
print(convert_to_12_hour_format_alt(12, 0))   # Выводит: "12:00 PM"
print(convert_to_12_hour_format_alt(6, 15))   # Выводит: "6:15 AM"
