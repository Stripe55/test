year = str(1978)

first_y = int(input())
second_y = int(input())

with open("perepis.txt", 'r', encoding='UTF-8') as file:
    file_content = file.read()
    print(file_content)
    list_of_people = list()
    num_of_people = file_content.count('\n')+1
    plist = file_content.split()
    for i in range(num_of_people):
        fio = [plist[i*4], plist[i*4+1], plist[i*4+2]]
        age = plist[i*4+3]
        lst = [fio, age]
        list_of_people.append(lst)
    people_under_year=0
    for i in range(len(list_of_people)):
        if list_of_people[i][1][6:10] < year:
            print(list_of_people[i][0][0])
            people_under_year+=1
    print("Общее число жителей, родившихся раньше", year, "года:", people_under_year)
    for i in range(len(list_of_people)):
        if str(second_y) > list_of_people[i][1][6:10] > str(first_y):
            print(list_of_people[i])

