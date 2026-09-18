def bubble_sort(my_list: list[int]):
    for outer_index in range(len(my_list) -1):
        print(f'iteration index: {outer_index}')
        for index in range(len(my_list) -1 , outer_index, -1):
            current_value = my_list[index]
            next_value = my_list[index - 1]
            if(current_value < next_value):
                print(f"{current_value} is less than {next_value}")
                my_list[index - 1] = current_value
                my_list[index ]= next_value
                print(f"moving {my_list[index - 1]} to index {index - 1} and {my_list[index]} to index: {index}")
                print(my_list)
            else:
                print(f"{current_value} is higher than {next_value}")
            print(f"---- index is {index} and value is {my_list[index]} ----")
        print("--- Final list ---")
        print(my_list)
            
            

my_list =  [14, 6, 9, 10, 5 ,2 ,1, 15, -1]
bubble_sort(my_list)




    