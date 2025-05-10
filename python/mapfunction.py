'''
The map() function in python applies any given function to all items of an iterable object such as a list, and returns a map object. 
This is particularly useful for transorming data in iterables comprehensively.
We can use lambda functions, regular functions or even built in method with map.
A lambda function is a small and anonymous function that can have any number of arguments but only one expression.
'''

#a userdefined function to sqaure each item of a list
def sqlist(nums):
  numsq = []
  for i in nums:
    numsq.append(i**2)
    
  return numsq

#sqaure each element in a list with map and lambda
nums = [1,2,3,4,5]
numss = [5,6,7,8,9,10]
sqaures = list(map(lambda x : x**2, nums))
print(sqaures)

#add adjacent elements of 2 lists with map and lambda
adjacents = list(map(lambda x,y : x+y, nums, numss))
print(adjacents)

#extract values from a list of dictionary using map and lambda
users = [
  {'username':'siddhant', 'nickname':'comicsid'},
  {'username':'nitinxpundir', 'nickname':'nix'}
  ]
  
nicknames = list(map(lambda usr : usr['nickname'], users))
print(nicknames)
