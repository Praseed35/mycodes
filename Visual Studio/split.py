import re


my_str = input("Enetr a strings:")

my_list = re.findall(r'[\w]+', my_str)
print(my_list)