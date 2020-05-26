# '''
# Algorithm

# define swap function (lakes a list)

# take the indice numbers of the array and swap them

# initiate variable for unsorted: unsorted : len - 1 (int)

# initiate no swap counter: sorted : 0 (int): 

# while unsorted is greater than 0

#     start a for loop (run till unsorted)

#         compare the adjacent elements, 
#         if first greater, 

#         swap numbers, rest counter to zero

#         else 

#         add one to counter

#     subtract sorted from unsorted

# print the sorted list

# return the sorted list


# '''

def bubble_sort(lst):

# '''
# Does the bubble sort

# input: lst (list)
# output: lst (list)

# '''
#defining our swap function
    def swap(i,j):
        '''
        Swap funtion
        '''

        temp = lst[j]
        lst[j] = lst[i]
        lst[i] = temp

    print('The unsorted list is:')
    print(lst)

    #give the range uptile where the sorting loop runs
    unsorted = len(lst) - 1

    #counter of how many elemts at the end have been sorted
    sorted_ = 0

    #counter of number of iterations passed
    iterations = 0

    while unsorted > 0:

        for i in range(unsorted):

            # condition for greater than
            if lst[i] > lst[i+1]:
                
                #calling the swapping function
                swap(i,i+1)
                sorted_ = 0

            else:

                sorted_ += 1

            iterations += 1

        unsorted -= sorted_

    print('The listt was sorted in ' + str(iterations) + ' iterations' )
    print('The sorted list is:')
    print(lst)

    return lst

#[2, 4, 3, 5, 1]

def test():

    lst = []

    n = int(input('Enter number of elements'))

    for j in range(n):

        if j == n-1:
            print('enter the last element')

        ele = int(input())

        lst.append(ele)

    lst = bubble_sort(lst)

test()
    
