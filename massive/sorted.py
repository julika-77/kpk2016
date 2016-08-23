
def sort_test(my_sort):
    A = [1, 2, 3, 4, 5, 6]
    A_ans = [1, 2, 3, 4, 5, 6]
    my_sort(A)
    print ('test case #1:' + ('OK' if A == A_ans else 'Fail'))

    A = [-1, -2, -3, -4, -5, -6]
    A_ans = [-6, -5, -4, -3, -2, -1]
    my_sort(A)
    print ('test case #2:' + ('OK' if A == A_ans else 'Fail'))

    A = [-1, 2, -3, 4, -5, 6]
    A_ans = [ -5, -3, -1, 2, 4, 6]
    my_sort(A)
    print ('test case #3:' + ('OK' if A == A_ans else 'Fail'))

    A = [1000]
    A_ans = [1000]
    my_sort(A)
    print ('test case #4:' + ('OK' if A == A_ans else 'Fail'))

    A = []
    A_ans = []
    my_sort(A)
    print ('test case #5:' + ('OK' if A == A_ans else 'Fail'))

    A = [5]*100
    A_ans = [5]*100
    my_sort(A)
    print ('test case #6:' + ('OK' if A == A_ans else 'Fail'))

def do_nothing(A):
    pass

def bubble_sort(A):
    N = len(A)
    for prohod in range(1,N):
        for i in range(N-prohod):
            if A[i] > A[i+1]:
                tmp = A[i]
                A[i]=A[i+1]
                A[i+1] = tmp


if __name__ == '__main__':
    sort_test(bubble_sort)

