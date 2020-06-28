def get_formatted_name(first, last, otch= ''):
    """Возвращает правильно созданное имя человека"""
    if otch:
        full_name = f"{first.title().strip()} {last.title().strip()} {otch.title().strip()}"
    else:
        full_name = f"{first.title().strip()} {last.title().strip()}"
    return full_name
