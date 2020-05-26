'''
algorithm

loop running from 0 to length(i)

    loop running from currnt loc backwards (j)

        compare i with j

        if j > i
         j swapped with j +1

        else
         BREAK

'''

def insert_sort(lst):

    print('The unsorted list is:')
    print(lst)

    #counter of number of iterations passed
    iterations = 0

    length = len(lst)

    for i in range(length):

        tem = lst[i]

        for j in range(i-1, -1, -1):

            iterations += 1

            if lst[j] >= tem:
                lst[j+1] , lst[j] = lst[j] , lst[j+1]

            else:
                break





    print('The listt was sorted in ' + str(iterations) + ' iterations' )
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

    lst = insert_sort(lst)

test()
    
