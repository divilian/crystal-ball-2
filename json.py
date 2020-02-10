import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats
import seaborn as sns

crew = ["Ed", "Kelly", "Alara", "Bortus", "John", "Claire"]

print(len(crew)) 
print("Captain {}.".format(crew[0]))
for member in crew[1:len(crew)-1]:
    print("{} reporting for duty, sir!".format(member))
print(crew[0])

alter_egos = { 'Bruce':'Batman', 'Dick':'Robin', 'Diana':'Wonder Woman',
    'Clark':'Superman' }

caped_crusaders = [ alter_egos['Bruce'], alter_egos['Dick'] ]
alter_egos['Clark'] = 'Man of Steel'
alter_egos['Victor'] = 'Cyborg'

print("There are now {} heroes, {} of which are the caped crusaders.".format(
    len(alter_egos), len(caped_crusaders)))
print("The dynamic duo is: {} and {}!".format(caped_crusaders[0],
    caped_crusaders[1]))
for key, value in alter_egos.items():
    print("Psssst, {} is really {}...".format(key,value))


a = [ 7, 1, [9, 5], 6 ]
print("a[1] is {}".format(a[1]))
print("len(a) is {}".format(len(a)))
print("a[3] is {}".format(a[3]))
print("len(a[2]) is {}".format(len(a[2])))
print("a[2][1] is {}".format(a[2][1]))

b = { "apple": 54, "banana": [14, 67], "cherry": { "bing": [ 13, 17, 21],
"rainier": { "sweet": "yes", "juicy": "yes" } } }

print(len(b))
print("b['apple'] is {}".format(b['apple']))
print("b['banana'] is {}".format(b['banana']))
print("len(b['banana']) is {}".format(len(b['banana'])))
print("len(b['cherry']) is {}".format(len(b['cherry'])))
print("len(b['cherry']['bing']) is {}".format(len(b['cherry']['bing'])))
print("b['cherry']['bing'][0]) is {}".format(b['cherry']['bing'][0]))
print("b['cherry']['rainier']['sweet']) is {}".format(b['cherry']['rainier']['sweet']))

print("b['apple'] is a {}".format(type(b['apple'])))
print("b['banana'] is a {}".format(type(b['banana'])))
print("b['cherry'] is a {}".format(type(b['cherry'])))
print("b['cherry']['rainier']['juicy'] is a {}".format(type(b['cherry']['rainier']['juicy'])))

c = [ { 'x': 5 }, [ 14, 'bob', [ 11, { 'duck': 'donuts', 'five':
'guys' }, [ 17, 6 ] ] ] ]

print("len(c) is {}".format(len(c)))
print("c[0]['x'] is {}".format(c[0]['x']))
print("c[1][1] is {}".format(c[1][1]))
print("c[1][2][1]['five'] is {}".format(c[1][2][1]['five']))
print("c[1][2][2][1] is {}".format(c[1][2][2][1]))



import json

with open("courses.json") as f:
    c = json.load(f)

for student in c[16]['roster']: 
    print("{} {} is in {} {}.".format(student['first'], 
        student['last'], c[16]['prefix'], c[16]['num'])) 


for course in c:
    roster = course['roster']
    for student in roster:
        if 'last' in student:
            print("{} {} is in {} {}.".format(student['first'], 
                student['last'], course['prefix'], course['num'])) 
        else:
            print("{} is in {} {}.".format(student['first'], 
                course['prefix'], course['num'])) 
