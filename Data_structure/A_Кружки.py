number = int(input())
courses = []
for i in range(0, number):
    line = input().strip()
    courses.append(line)

visited_optional_courses = []
for i in courses:
    if i not in visited_optional_courses:
        visited_optional_courses.append(i)


print("\n".join(visited_optional_courses))
