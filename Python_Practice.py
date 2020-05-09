#if the second county in the list is Denver, the second county will print
counties = ["Arapahoe","Denver","Jefferson"]
if counties[1] == 'Denver':
    print(counties[1])

#if El Paso is in the list of counties, an affirmative statement will print, if not, a negative statement will print
counties = ["Arapahoe","Denver","Jefferson"]
if "El Paso" in counties:
    print("El Paso is in the list of counties.")
else:
    print("El Paso is not the list of counties.")

#if both Arapahoe and El Paso are in the list of counties, an affirmative statement will print, else, negative
if "Arapahoe" in counties and "El Paso" in counties:
    print("Arapahoe and El Paso are in the list of counties.")
else:
    print("Arapahoe or El Paso is not in the list of counties.")

#if either Arapahoe and El Paso are in the list of counties, an affirmative statement will print, else, negative
if "Arapahoe" in counties or "El Paso" in counties:
    print("Arapahoe or El Paso is in the list of counties.")
else:
    print("Arapahoe and El Paso are not in the list of counties.")

#if Arapahoe is in the list of counties and El Paso is not, print statement, else
if "Arapahoe" in counties and "El Paso" not in counties:
   print("Only Arapahoe is in the list of counties.")
else:
    print("Arapahoe is in the list of counties and El Paso is not in the list of counties.")

#for loop that iterates through and prints the counties list
for county in counties:
    print(county)

#creation of counties dictionary 
counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}

#for loop that prints the keys from a dictionary 
for county in counties_dict:
    print(county)

#for loop that prints the keys from a dictionary, using the keys() method
for county in counties_dict.keys():
    print(county)

#for loop that prints the values from a dictionary, using the values() method
for voters in counties_dict.values():
    print(voters)

#for loop using the dictionary_name[key] format to print the values by referencing the key
for county in counties_dict:
    print(counties_dict[county])

#for loop using the get() method to pring the values by referencing the key
for county in counties_dict:
    print(counties_dict.get(county))

#for loop that prints the key-value pairs of a dictionary
for county, voters in counties_dict.items():
    print (county , " has " , voters , " registered voters.")

#a list of dictionaries
voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]

#for loop that prints the dictionaries from a list
for county_dict in voting_data:
    print(county_dict)

#for loop that prints the dictionaries from a list using range() method
for i in range(len(voting_data)):
    print(voting_data[i])

#prints each value from each ket of each dictionary
for county_dict in voting_data:
    for value in county_dict.values():
        print(value)

#prints the registered voters from each dictionary
for county_dict in voting_data:
     print(county_dict['registered_voters'])

#prints the county names from each dictionary
for county_dict in voting_data:
    print(county_dict['county'])

#f-strings
my_votes = int(input("How many votes did you get in the election? "))
total_votes = int(input("What is the total votes in the election? "))
print(f"I received {my_votes / total_votes * 100}% of the total votes.")

counties_dict = {"Arapahoe": 369237, "Denver":413229, "Jefferson": 390222}
for county, voters in counties_dict.items():
    print(county + " county has " + str(voters) + " registered voters.")

for county, voters in counties_dict.items():
    print(f"{county} county has {voters} registered voters.")

#f-strings
candidate_votes = int(input("How many votes did the candidate get in the election? "))
total_votes = int(input("What is the total number of votes in the election? "))
message_to_candidate = (
    f"You received {candidate_votes} number of votes. "
    f"The total number of votes in the election was {total_votes}. "
    f"You received {candidate_votes / total_votes * 100:.2f}% of the total votes.")

print(message_to_candidate)