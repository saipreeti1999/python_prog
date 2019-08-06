def group_value(list,n):
    for i in list:
        if n==i:
            return True
    return False
print(group_value([1,5,8,3],2))
print(group_value([1,5,8,3],8))
