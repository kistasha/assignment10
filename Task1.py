# importing the modules
import module1
import module2

# calling the method for each list
print(module1.find_two_smallest(module2.list1))
print(module1.find_two_smallest(module2.list2))
print(module1.find_two_smallest(module2.list3))
print(module1.find_two_smallest(module2.list4))

my_file = "results.txt"

file = open(my_file,'w')
file.write(f'Two smallest values in list1: {module1.find_two_smallest(module2.list1)}\n')
file.write(f'Two smallest values in list2: {module1.find_two_smallest(module2.list2)}\n')
file.write(f'Two smallest values in list3: {module1.find_two_smallest(module2.list3)}\n')
file.write(f'Two smallest values in list4: {module1.find_two_smallest(module2.list4)}\n')
file.close()
