candidates = [
    {"name": "Vasya",  "scores": {"math": 58, "russian_language": 62, "computer_science": 48}, "extra_scores":0},
    {"name": "Fedya",  "scores": {"math": 33, "russian_language": 85, "computer_science": 42},  "extra_scores":2},
    {"name": "Petya",  "scores": {"math": 92, "russian_language": 33, "computer_science": 34},  "extra_scores":1}
]

def find_top_20(data):
    summ = 0
    extra = 0
    output =[]
    """
    find the total number of points and output the top 20 by "name"
    """
    for i in candidates:
        summ = i['scores']['math']+i['scores']['russian_language']+i['scores']['computer_science']
        extra = i['extra_scores']
        row = i['name'], summ + extra
        output.append(row)
        sorted_output = sorted(output, key=lambda x: x[1], reverse=True)[:3]
        result = [i[0] for i in sorted_output]
    return result

t20=find_top_20(candidates)

print(t20)