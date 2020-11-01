set = [6,7,3,5,9,1,234,2,8,24,26,12]
import sys
sys.setrecursionlimit(5000)

def bubble_sort(set):
    finished = False
    while finished == False:
        swap = False
        for i in range(len(set)-1):
            if(set[i]>set[i+1]):
                print(i)
                swap = True
                temp = set[i+1]
                set[i+1] = set[i]
                set[i] = temp
            print(swap)
        if(swap == False):
            finished = True


def quick_sort(set):

    small_set=[]
    big_set=[]
    equal = []
    if len(set)>1:
        pivot = set[0]
        for x in set:
            if x < pivot:
                small_set.append(x)
            elif x==pivot:
                equal.append(x)
            elif x>pivot:
                big_set.append(x)
        print(small_set)
        return quick_sort(small_set) + quick_sort(equal)+ quick_sort(big_set)
    else:
        return set


def insertion_sort(set):
    for i in range(len(set)):
        x = set[i]
        j = i - 1
        while j > -1 and set[j] > x:
            set[j + 1] = set[j]
            j = j - 1
        set[j + 1] = x
    return set

print(insertion_sort(set))



        
        

