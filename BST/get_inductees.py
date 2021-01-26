names = ["Vasya", "Alice", "Petya", "Jenny", "Fedya", "Viola", "Mark", "Chris", "Margo"]
birthday_years = [1962, 1995, 2000, None, None, None, None, 1998, 2001]
genders = ["Male", "Female", "Male", "Female", "Male", None, None, None, None]


def get_inductees(names, birthday_years, genders):
    """
    Returns the names of men, from 18 years old to 30 years old in 2021
    :param names:
    :param birthday_years:
    :param genders:
    :return:a tuple containing a list of conscripts and a list of undefined ones containing.
    """
    unidentified = []
    result = []
    for i in range(0, len(names)):
        if not birthday_years[i] or not genders[i] or genders[i] == "Female":
            row = names[i]
            unidentified.append(row)
        elif 18 <= 2021 - birthday_years[i] < 30:
            row = names[i]
            result.append(row)
    return result, unidentified


s = get_inductees(names, birthday_years, genders)
print(type(s))
