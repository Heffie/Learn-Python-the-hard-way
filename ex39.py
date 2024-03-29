# create a mapping of state to abbreviation
states = {
    'Oregon' : 'OR',
    'Florida' : 'FL',
    'California' : 'CA',
    'New York' : 'NY',
    'Michigan' : 'MI',
}

# creates a basic set of states and some cities in them
cities = {
    'CA' : 'San Francisco',
    'MI' : 'Detroit',
    'FL' : 'Jacksonville',
}

# add some more cities
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

# print out some cities
print('-' * 10)
print("NY State has: ", cities['NY'])
print("NY State has: ", cities['OR'])

# print some states
print('-' * 10)
print("Michigan has: ", states['Michigan'])
print("Florida has: ", states['Florida'])

# print every state abbreviation
print('-' * 10)
for state, abbrev in list(states.items()):
    print(f"{state} is abbriviated {abbrev}")

# print every city in state
print('-' * 10)
for abbrev, city in list(cities.items()):
    print(f"{abbrev} is the city {city}")

# now do both at the same times
print('-' * 10)
for state, abbrev in list(states.items()):
    print(f"{state} state is abbrivated {abbrev}")
    print(f"and has the city {cities[abbrev]}")

print('-' * 10)
# safely get abbreviation by state that migh not be there
state = states.get('Texas')

if not state:
    print("Sorry, no Texas.")

# get a city with a default value
city = cities.get('TX', 'Does not exist')
print(f"The city for the state 'TX' is: {city}")
