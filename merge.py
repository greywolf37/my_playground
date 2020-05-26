'''
algorithm

introduce a splitting function

introduce merge function

    takes two lists

    ind_1 and ind_2 as indexes for the two lists (initial at 0)

    while both are smaller tahn length

    the smaller one is appended to a new list, and that counter in increases

    when on index reaches its lenth -1, append and asing it inf

    return merged list

split the list

while length of array > 1

    initiate empty list 

    Take length divide by 2 and find number of pairs (if odd inividual append the last element)

    loop through the number of pairs

        merge and append to empty list

        assign empty list to lst

lst = lst[0]


'''
def split(arr):
    '''
    takes in a list and makes it a list of lists
    '''

    emt = []
    for i in range(len(arr)):
        emt.append([arr[i]])

    return emt

def merge(arr_1, arr_2):
    '''
    Merges two lists in accending order
    '''

    #initializing both indexes and empty list
    ind_1 = 0
    ind_2 = 0

    emt = []
        
    #appending infinity to the list
    arr_1.append(float('inf'))
    arr_2.append(float('inf'))

    while ind_1 < len(arr_1) -1 or ind_2 < len(arr_2) -1:

        if arr_1[ind_1] < arr_2[ind_2]:

            emt.append(arr_1[ind_1])
            ind_1 += 1

        else:
            emt.append(arr_2[ind_2])
            ind_2 += 1

    return emt








def merge_sort(lst):

    print('The unsorted list is:')
    print(lst)

    #counter of number of iterations passed
    iterations = 0

    lst = split(lst)

    #when the are still splits in the list
    while len(lst) > 1:

        print("length", len(lst))

        #Initiating an empty list
        emt = []

        #Iterating through each pair
        for i in range((len(lst)//2)):

            #appending to empty list
            emt.append(merge(lst[2*i],lst[2*i+1]))

            iterations += 1

        if len(lst)%2 != 0:

            emt.append(lst[-1])

        lst = emt
     
    lst = lst[0]







    print('The list was sorted in ' + str(iterations) + ' iterations' )
    print('The sorted list is:')
    print(lst)

    return lst


def test():

    lst = []

    n = int(input('Enter number of elements'))

    for j in range(n):

        if j == n-1:
            print('enter the last element')

        ele = int(input())

        lst.append(ele)

    lst = merge_sort(lst)

test()
    
