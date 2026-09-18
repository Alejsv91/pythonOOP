def bubble_sort(my_list: list[int]):
    for outer_index in range(len(my_list) -1 , 0, -1):
        for index in range(len(my_list) -1 , 0, -1):
            current_value = my_list[index]
            next_value = my_list[index - 1]
            # print(f"index is {index} and value is {my_list[index]}")
            # print(f"current value: {current_value} and next value: {next_value}")
            if(current_value < next_value):
                print(f"{current_value} is less than {next_value}")
                my_list[index - 1] = current_value
                my_list[index ]= next_value
                print(f"moving {my_list[index - 1]} to index {index - 1} and {my_list[index]} to index: {index}")
                print(my_list)
            else:
                print(f"{current_value} is higher than {next_value}")
            print(f"---- index is {index} and value is {my_list[index]} ----")
        print("--- New list ---")
        print(my_list)
            
            

my_list =  [14, 6, 9, 10, 5 ,2 ,1, 15, -1]
bubble_sort(my_list)




    