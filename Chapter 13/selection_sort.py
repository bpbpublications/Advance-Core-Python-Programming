def selection_sort(input_list):
    for i in range(len(input_list)-1):
        for j in range(i+1,len(input_list)):
            if input_list[j] < input_list[i]:
                temp = input_list[j]
                input_list[j] = input_list[i]
                input_list[i] = temp
    print(input_list)


selection_sort([15,10,3,19,80,75])
selection_sort([5,9,80,65,71,24,15,10,3,19,85,75])


    
