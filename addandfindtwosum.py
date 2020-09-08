global_nums = []

def add(num):
    """
    :type num: int
    :rtype: -
    """
    global_nums.append(num)


def find(target):

    for num in global_nums:
        if target - num in global_nums:
            return True
    return False

add(1)
add(3)
add(5)
print(find(4))
print(find(1))
print(find(8))
print(find(7))