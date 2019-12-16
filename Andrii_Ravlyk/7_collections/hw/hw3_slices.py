'''3. List slices:
    * Use a slice to print the first three items from that program’s list.
    * Use a slice to print three items from the middle of the list.
    * Reverse your list from first index to the end.
    * Use a slice to print the last three items in the list.'''

lists = [1,2,3,4,5,6,7,8]

print (lists[0:3])
print (lists[int(len(lists)/2) : int(len(lists)/2) + 3])
print (lists[::-1])
print (lists[-3:])
