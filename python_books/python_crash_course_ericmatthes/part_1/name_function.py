
def get_formated_names(first,last):
    """Generate a neatly formated full name."""
    full_name = f"{first} {last}"
    return full_name.title()

def city_info(city_name,country_name):
    return f"{city_name.title()}, {country_name.title()}."
