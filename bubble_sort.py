def standard_bubble_sort(my_list: list[int]):
    for outer_index in range(0, len(my_list) -1):
        for index in range(0, len(my_list) -1 - outer_index):
            current_value = my_list[index]
            next_value = my_list[index + 1]
            if(current_value > next_value):
                my_list[index + 1] = current_value
                my_list[index ]= next_value
    print("--- standard Final list ---")
    print(my_list)

def bubble_sort(my_list: list[int]):
    for outer_index in range(len(my_list) -1):
        for index in range(len(my_list) -1 , outer_index, -1):
            current_value = my_list[index]
            next_value = my_list[index - 1]
            if(current_value < next_value):
                my_list[index - 1] = current_value
                my_list[index ]= next_value
    print("--- Final list ---")
    print(my_list)
            
my_list =  [14, 6, 9, 10, 5 ,2 ,1, 15, -1]
standard_bubble_sort(my_list) 

bubble_sort(my_list)