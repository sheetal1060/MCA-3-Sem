def iterate_lists(list1, list2):
    for item1, item2 in zip(list1, reversed(list2)):
        print(f"List1 Item: {item1}, List2 Item: {item2}")


list1 = [1, 2, 3, 4]
list2 = [10, 20, 30, 40]
iterate_lists(list1, list2)
