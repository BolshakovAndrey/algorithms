know_english = ["Vasya", "Jimmy", "Max", "Peter", "Eric", "Zoi", "Felix"]
sportsmen = ["Don", "Peter", "Eric", "Jimmy", "Mark"]
more_than_20_years = ["Peter", "Julie", "Jimmy", "Mark", "Max"]


def find_athlets(know_english, sportsmen, more_than_20_years):
    """
    Returns a list of student names that fit in all the input lists
    :param know_english:
    :param sportsmen:
    :param more_than_20_years:
    :return: list of student names
    """
    result = []
    for i in range(0, len(know_english)):
        if know_english[i] in sportsmen and know_english[i] in more_than_20_years:
            result.append(know_english[i])
    return result


r = find_athlets(know_english, sportsmen, more_than_20_years)
print(r)
