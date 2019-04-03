# Counts the number of cat and dog instances in a string and returns true if they have the same count
def cat_dog(str):
    dog_count = 0
    cat_count = 0
    length = len(str)-2

    for i in range(length):
        if str[i] == 'c':
            if str[i+1] == 'a' and str[i+2] == 't':
                cat_count += 1
        elif str[i] == 'd':
            if str[i+1] == 'o' and str[i+2] == 'g':
                dog_count += 1

    return dog_count == cat_count
#Test using -> cat_dog("catdog")

# Returns true if a list has a 2 adjacent to another 2
def has22(ls):
    length = len(ls) - 1

    for i in range(length):
        if ls[i] == 2:
            if ls[i+1] == 2:
                return True
            else:
                continue

    return False
#Test using -> hass22([1,2,2,3,2])

# Returns true if the goal number of chocolates can be created using the combination of small and big
def make_chocolate(small,big,goal):
    need_kilos =  (big) * 5
    if need_kilos < 0:
        return -1
    else:
        if small >= need_kilos:
            return need_kilos
        else:
            return -1
#Test using -> make_chocolate(1,5,11)

# Returns true if either b or c is within a distance of 1 from a while the other is greater then or equals 10
def close_far(a,b,c):

	if abs(b - a) <= 1 :
		if abs(c - a) >= 2 and abs(c-b)>=2:
			return True
		else:
			return False

	elif abs(c - a) == 1:
		if abs(b - a) >= 2 and abs(b-c) >= 2:
			return True
		else:
			return False
# Test using -> close_far(1,2,10)

# Returns true is the goal number of bricks can be created using the cobination of small and big bricks
def make_bricks(small, big, goal):
    divide_by = goal / 5
    if divide_by < 1:
        final = goal - small
        if final <=0:
            return True
        else:
            return False
    else:
        if divide_by == big:
            return True
        elif divide_by < big:
            semi_final = goal - (divide_by*5)
            final = semi_final - small
            if final <=0:
                return True
            else:
                return False
        elif divide_by > big:
            semi_final = goal - (big*5)
            final = semi_final - small
            if final <=0:
                return True
            else:
                return False
# Test using -> make_bricks(1,1,7)

# Returns repeated characters in a string
def repeat_chars(n):
    dict = {}
    for char in n:
        if char in dict:
            dict[char] = dict[char] + 1
        else:
            dict[char] = 1
    for key in dict:
        if dict[key] > 1:
            print(key)
# Test using repeat_chars("Rafsan")

# Returns a list with no repeated characters
def unique_string(n):
    myset = set()
    buffer = ""
    for char in n:
        myset.add(char)
    for item in myset:
        buffer += item
    return sorted(buffer)
# Test using unique_string("Rafsan")

# iterates through an unsorted list to find whether two same entries equals the sum.
def unsorted_list_sum(lst, sum):
    leng = len(lst) - 1
    y = 0

    while y != leng-1:
        for i in range(leng):
            if lst[y] == lst[i+1]:
                val = lst[y] + lst[i+1]
                if val == sum:
                    return True
        y = y + 1
    return False
# Test using unsorted_list_sum([1,4,5,3,6],9)

# iterates through a sorted list to find whether two same entries equals the sum.
def sorted_list_sum(lst, sum):
    leng = len(lst)-1
    target_number = sum / 2
    for i in range(leng):
        if lst[i] == target_number:
            if lst[i] + lst[i+1] == sum:
                return True
    return False
# Test using sorted_list_sum([1,2,3,4,4],8)

# Checks whether a given list has repeats in linear time.
def has_repeats(lst):
    lst_length = len(lst)
    my_set     = set(lst)
    set_length = len(my_set)

    if lst_length > set_length:
        return True
    else:
        return False
# Test using has_repeats([1,2,3,3,5,4,6,4])

# Returns the first recurring character of a list
def first_recuring(lst):
    dict = {}
    ret_str = "No repeats"
    for item in lst:
        if item in dict:
            return item
        else:
            dict[item] = 1
    return ret_str
# Test using first_recuring(['A','B','C','A','C'])
