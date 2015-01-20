# mapping state to abbrv
states = {
    'Oregon' : 'OR',
    'Florida' : 'FL',
    'California' : 'CA',
    'New York' : 'NY',
    'Michigan' : 'MI'
}

cities = {
    'CA': 'San Francisco',
    'MI': 'Detroit',
    'FL': 'Jacksonville'
}

#add to dict
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

print '-' * 10
print 'NY State has: ', cities['NY']
print 'OR State has :', cities['OR']

#states
print '-' * 10
print "Michigan's abbreviation is: ", states['Michigan']
print "Florida's abbreviation is: ", states['Florida']

print '-' * 10
print "Michigan's has: ", cities[states['Michigan']]
print "Florida has: ", cities[states['Florida']]

# all states abbrv
print '-' * 10
for state, abbrv in states.items():
    print "%s is abbreviated %s" % (state, abbrv)

print '-' * 10
for abbrv, city in cities.items():
    print '%s has the city %s' % (abbrv, city)

#both
print '-' * 10
for state, abbrv in states.items():
    print "%s state is abbreviated %s and has city %s" % (state, abbrv, cities[abbrv])

print '-' * 10
state = states.get('Texas')    

if not state:
    print "Sorry, no Texas"

city = cities.get('TX', 'Does not exist')
print "the city for the state of 'TX' is: %s" % city
   