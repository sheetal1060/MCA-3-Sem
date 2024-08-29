def check(lst):
    if len(lst) > 0 and lst[0] == lst[-1]:
        return True
    return False


result = check([10, 20, 30, 10])
print(result)  
