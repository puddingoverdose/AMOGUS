import random

string_to_be_replaced = input("AMOGUS: ").split()
i = 0
while i < len(string_to_be_replaced):
    string_to_be_replaced[random.randint(1, len(string_to_be_replaced))-1] = "SUS"
    i+=1
new_amogus = ' '.join(string_to_be_replaced)
print(new_amogus)
