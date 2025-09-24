#!/usr/bin/env python3

def print_fibonacci(length):
    if length == 0:
          print ([])
          return []
    elif length ==1:
          print ([0])
          return[0]
          
    fibonacci_sequence = [0,1]
    while len(fibonacci_sequence) < length:
            next_value = fibonacci_sequence[-1] + fibonacci_sequence[-2]            
            fibonacci_sequence.append(next_value)
    print(fibonacci_sequence)
    return fibonacci_sequence

print_fibonacci(0)

# my_list = [34,35,36,37,38,39]
# # my_list[-2] = True
# # my_list.append(-1)
# my_list.insert(0,34)
# # del(my_list[0:4])
# my_list.remove(37)
# print(my_list)
# # print(sorted_list)

# my_tuples = [('Jog',2),('Stev',1),('Mer',4)]

# def sort_tuple(tuple_value):
#     return tuple_value[0]
# my_tuples.sort(key =sort_tuple)
# print(my_tuples)


