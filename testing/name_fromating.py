def get_formated_name(first_name, last_name, middle_name=""):
    """"format first and last name as a single name"""
    if middle_name:
        return f"{first_name} {middle_name} {last_name}".title()
    return f"{first_name} {last_name}".title()
