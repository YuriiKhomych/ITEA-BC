# 3. List slices:
#     * Use a slice to print the first three items from that program’s list.
#     * Use a slice to print three items from the middle of the list.
#     * Reverse your list from first index to the end.
#     * Use a slice to print the last three items in the list.

entered_list = [1,2,3,4,5,6,7]
# entered_list = input(f'Enter please list of items separeted by , : ')
def list_slice(my_list):
    print(my_list[:3])
    print(my_list[len(my_list)//2-1:len(my_list)//2+2])
    print(my_list)
    my_list.reverse()
    print(my_list)
    print(my_list[-3:])

list_slice(entered_list)