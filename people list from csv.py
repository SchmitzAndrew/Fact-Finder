from csv import reader

with open('people_list.csv', 'r') as read_obj:
    csv_reader = reader(read_obj)
    people_list_with_initials = list(map(tuple, csv_reader))
    print(people_list_with_initials)


