
def insertion_sort(l):

    for i in range(1,len(l)):
        if l[i - 1] > l[i]:
            current_val = l[i]
            j = i
            while current_val < l[j]:
                
                j -= 1
                if l[i] > l[j]:
                    

