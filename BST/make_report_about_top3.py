students_avg_scores = {'Max': 4.964,
                       'Eric': 4.962,
                       'Peter': 4.923,
                       'Mark': 4.957,
                       'Julie': 4.95,
                       'Jimmy': 4.973,
                       'Felix': 4.937,
                       'Vasya': 4.911,
                       'Don': 4.936,
                       'Zoi': 4.937}


def make_report_about_top3(students_avg_scores):
    """
    Creates a 'csv' file containing the names of the
     3 students with the highest average grade
    :param students_avg_scores:
    :return: path to 'csv' file
    """
    # calculate top-3
    list_s = list(students_avg_scores.items())
    list_s.sort(key=lambda i: i[1], reverse=True)
    top_3 = list_s[:3]
    res = [i[0] for i in top_3]

    # write to csv
    import csv
    file = open('top3.csv', 'w')
    with file:
        writer = csv.writer(file, dialect='excel-tab')
        writer.writerows(res)

    # create path to 'csv' file
    from pathlib import Path
    output_path = Path.cwd() / 'top3.csv'
    print("The recording of the 'csv' file is complete! "
          "The file is in the folder:")
    return output_path


r = make_report_about_top3(students_avg_scores)
print(r)
