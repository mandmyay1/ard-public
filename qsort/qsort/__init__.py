def quicksort(list_to_sort):
    if len( list_to_sort ) is 0: return list_to_sort
    pivot = list_to_sort.pop(int(len( list_to_sort )/2))
    less_than_list, greater_than_list = [], []
    for element in list_to_sort: 
        if element < pivot: less_than_list.append(element) 
        else: greater_than_list.append(element)
    return quicksort( less_than_list ) + [pivot] + quicksort( greater_than_list )

from random import randint
import datetime

randomlist = [randint(0,1000) for _ in range(500)]
print( randomlist )
time1 = datetime.datetime.now()
#quicksort(randomlist)
print( quicksort( randomlist ) )
time2 = datetime.datetime.now()
d = time2 - time1
print(d.seconds,d.microseconds)