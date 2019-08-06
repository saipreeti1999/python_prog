def count_list4(num):
    count=0
    for i in num:
        if i==4:
            count+=1
    return count
print(count_list4([1,4,6,7,4]))
print(count_list4([1,4,6,4,7,4]))
