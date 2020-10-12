pupils = [
    'Бутылкин Василий',
    'Петров Борис',
    'Чашкина Василиса',
    'Зайцев Макар',
    'Яблоков Геннадий',
    'Заборчиков Михаил',
    'Котовасин Роман',
    'Забывакина Раиса']

vasya_butylkin_optional_courses = [
    'вышивание крестиком',
    'рисование мелками на парте',
    'настольный керлинг',
]
vasilisa_chashkina_optional_courses = [
    'настольный керлинг',
    'кухня африканского племени ужасмай',
    'тяжелая атлетика',
    'таракановедение',
]
visited_optional_courses = set()

for course in vasya_butylkin_optional_courses:
    visited_optional_courses.add(course)

for course in vasilisa_chashkina_optional_courses:
    visited_optional_courses.add(course)

print(visited_optional_courses)
