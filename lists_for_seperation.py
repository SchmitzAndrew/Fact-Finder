#list_for_spereation_makes_various_lists_for_a_users_input_later_on
#lists are:
#people-list
#years-list
#locationds-dictionaries

#makes list from csv
import csv

#creaters list of tuples from .csv
with open('people_list.csv', 'r') as read_obj:
    csv_reader = csv.reader(read_obj)
    people_tuple_list_with_initials = list(map(tuple,csv_reader))

#converts tuples into a list
people_list_with_initials = [name for name_tuple in people_tuple_list_with_initials for name in name_tuple]

#takes out initials from list, crude method without range-> people_list

people_list = []
people_index = 1
for name_or_initials in people_list_with_initials:
    try:
        people_list.append(people_list_with_initials[people_index].strip().lower())
        people_index = people_index + 2
    except IndexError:
        break



# makes years list

nums = range(-1000, 2021, 1)
years = [*nums]
years.remove(0) #0 isn't in the BC/ AD system

#Negative years and positive years are sorted and gived an ending
years_BC = []
years_AC = []
for year in years:
    if year < 0:
        years_BC.append(str(abs(year)) + "BC")
    if year > 0:
        years_AC.append(str(year) + "AD")


years_list = years_BC + years_AC

#Locations: Dictionary for countries(Finds every city in a country)
#Makes a dictionary for each part
city_name_list = []
country_name_list = []
geoname_id_list = []

with open("locations-list.csv", "r", encoding="utf-8-sig") as f:
    reader = csv.DictReader(f)
    locations_list = list(reader)

for location in locations_list:
    city_name_list.append(location['name'])
    country_name_list.append(location['country'])
    geoname_id_list.append(location['geonameid'])
























