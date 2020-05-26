'''
algorithm

write swap definition

start loop from first element

    start another loop from current element to the end

        introduce min_pos as startinf element

        compare with other elemnts

        if other element is smaller, update min_pos

    swap position of the first element with min_pos


'''
def select_sort(lst):

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

    lenth = len(lst)

    iterations = 0

    for i in range(lenth-1):

        min_pos = i

        for j in range(i+1, lenth):

            if lst[min_pos] > lst[j]:
                min_pos = j
            iterations += 1

        swap(i,min_pos)

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

    lst = select_sort(lst)

test()