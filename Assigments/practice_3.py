#1) Create a list of “person” dictionaries with a name, age and list of hobbies for each person. Fill in any data you want.
persons = [
    {
        'name': 'Pamela', 
        'age': 23, 
        'hobbies': ['Movies', 'Series', 'Cooking']
    },
    {
        'name': 'Carlos',
        'age': 22,
        'hobbies': ['Series', 'Videogames', 'Puzzels']
    },
    {
        'name': 'Pamlos',
        'age': 21,
        'hobbies': ['Dancing', 'Programing', 'Sports']
    }
    ]

#2) Use a list comprehension to convert this list of persons into a list of names (of the persons).
persons_name = [person['name'] for person in persons]
print(persons)
print(persons_name)

#3) Use a list comprehension to check whether all persons are older than 20.
are_older = all([person['age'] > 20 for person in persons])
print(are_older)

#4) Copy the person list such that you can safely edit the name of the first person (without changing the original list).
#copied_persons = persons[:]
copied_persons = [person.copy() for person in persons]
copied_persons[0]['name'] = 'Shirley'
print(copied_persons)
print(persons)

#5) Unpack the persons of the original list into different variables and output these variables.
p1, p2, p3 = persons
print(p1)
print(p2)
print(p3)