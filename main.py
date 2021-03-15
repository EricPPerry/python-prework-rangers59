def hello_name(user_name):
    print("Hello " + user_name.title() + "!")

def hello_name2(user_name):
    print(f"Hello {user_name.title()}!")

def odd_numbers():
    for num in range(1,101,2):
        print(num)

def find_max(a_list):
    return max(a_list)

def is_consecutive(my_list):
    return sorted(my_list) == list(range(min(my_list), (max(my_list)+1)))

print(is_consecutive([1,4,3,4,6]))