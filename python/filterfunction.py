'''
The filter() function in python constructs an iterator from elements of an iterable for which a specified function is true.
It is used to filter out items from an iterable based on given condition.
'''

users = [
  {'username':'comicsid', 'age':21, 'gender':'M'},
  {'username':'nitinxpundir', 'age':23, 'gender':'M'},
  {'username':'wakeupsanjhi', 'age':16, 'gender':'F'},
  {'username':'shreyaweeps', 'age':22, 'gender':'F'}
  ]
  
nums = [1,2,3,4,5,6,7,8,9,10]

#construct a new list of only even numbers
evens = list(filter(lambda n : n%2==0, nums))
print(evens)

#get a new list with users above age 18
validusers = list(filter(lambda u : u['age']>=18, users))
print(validusers)

#get valid and female users
validfemaleusers = list(filter(lambda u : u['age']>=18 and u['gender']=='F',users))
print(validfemaleusers)
