cities = ('New Delhi', 'Mumbai', 'Pune', 'Patna', 'Varanasi', 'Kolkata', 'Chennai')

# cities[0] = 'Delhi' //TypeError: 'tuple' object does not support item assignment
print('Mumbai' in cities)

#slice a tuple
print(cities[1:7:2])

#python special assignment (works with lists too)
city1, city2, *otherCities, city3 = cities
print(city1) # New Delhi
print(city2) # Mumbai
print(otherCities) # ['Pune', 'Patna', 'Varanasi', 'Kolkata']
print(city3) # Chennai

numbers = (1, 2, 2, 3, 4, 5, 5, 5, 6, 7)
print(numbers.count(5)) # 3
print(numbers.index(6)) # 8

print(len(cities)) #7
