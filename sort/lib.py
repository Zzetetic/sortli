def bubble_sort_asc(ListInst):
    for i in range(ListInst.__len__()-1):
        for j in range(ListInst.__len__()-1-i):
            if ListInst[j+1] < ListInst[j]:
                tmp_value = ListInst[j+1]
                ListInst[j+1] = ListInst[j]
                ListInst[j] = tmp_value
            j = j + 1
            
        i = i + 1
				


def bubble_sort_desc(ListInst):
    bubble_sort_asc(ListInst)
    reverse_list(ListInst)






def insertion_sort_asc(ListInst):
    for i in range(1, ListInst.__len__()):
        tmp_value = ListInst[i]
        j = i
        while j > 0 and ListInst[j-1] > tmp_value:
            ListInst[j] = ListInst[j-1]
            j = j - 1
        ListInst[j] = tmp_value
        i = i + 1
    


def insertion_sort_desc(ListInst):
    insertion_sort_asc(ListInst)
    reverse_list(ListInst)




def reverse_list(ListInst):
    listHalfLen = ListInst.__len__()//2
    listLen = ListInst.__len__()-1
    
    i = 0
    while i < listHalfLen:
        temp_value_right = ListInst[i]
        temp_value_left = ListInst[listLen-i]
        ListInst[i] = temp_value_left
        ListInst[listLen-i] = temp_value_right
        i = i + 1






        
