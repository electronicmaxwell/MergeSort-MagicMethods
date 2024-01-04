from person import Person, create_persons_list
import numpy as np


def mergesort(lst, key=lambda x: x, reverse=False):
    if len(lst) > 1:
        mid_idx = len(lst) // 2
        left_lst = mergesort(lst[:mid_idx], key, reverse)
        right_lst = mergesort(lst[mid_idx:], key, reverse)
        ordered_lst = merge(left_lst, right_lst, key, reverse)
        return ordered_lst
    else:
        return lst


def merge(lst1, lst2, key=lambda x: x, reverse=False):
    ordered_lst = []
    i = j = 0
    while i < len(lst1) and j < len(lst2):
        if (reverse and key(lst1[i]) >= key(lst2[j])) or (not reverse and key(lst1[i]) < key(lst2[j])):
            ordered_lst.append(lst1[i])
            i += 1
        else:
            ordered_lst.append(lst2[j])
            j += 1

    ordered_lst.extend(lst1[i:] if i < j else lst2[j:])
    return ordered_lst


def compare(ipt):
    if type(ipt) == str:
        if ipt.lower() in ['name', 'age', 'height', 'weight']:
            return lambda person: getattr(person, f'_{ipt.lower()}')
        else:
            raise KeyError('You must select an attribute in the Person class (name, age, height, and weight)')
    elif type(ipt) == int:
        if 0 <= ipt <= 3:
            return lambda person: person[ipt]
        else:
            raise IndexError('You must select an index between 0 and 3')
    else:
        raise ValueError('You must input an attribute of Person (str) or valid index (int) to use this function')


def main():
    test_person = p2 = Person('Max', 22, 196, 87)

    print(f'Person Class Representation: {repr(test_person)}')
    print(f'Person Class String Conversion: {str(test_person)}')
    print(f'Person Class Int Conversion: {int(test_person)}')
    print(f'Person Class Float Conversion: {float(test_person)}')
    print(f'Person Class List Conversion: {list(test_person)}')
    print(f'Person Class Tuple Conversion: {tuple(test_person)}\n')

    people = create_persons_list()
    print('List to Sort:')
    print(f'{people}\n')

    print('Default Merge Sort')
    print(f'{mergesort(people)}\n')

    print('Reversed Default Merge Sort')
    print(f'{mergesort(people, reverse=True)}\n')

    print('Merge Sort By Name')
    print(f'{mergesort(people, key=compare("name"))}\n')

    print('Reversed Merge Sort By Age')
    print(f'{mergesort(people, key=compare("age"), reverse=True)}\n')

    print('Merge Sort By Height')
    print(f'{mergesort(people, key=compare("height"))}\n')

    print('Reversed Merge Sort By Weight')
    print(f'{mergesort(people, key=compare("weight"), reverse=True)}\n')

    print('Merge Sort By Age Index')
    print(f'{mergesort(people, key=compare(1))}\n')

    print('Reversed Merge Sort By Weight Index')
    print(f'{mergesort(people, key=compare(3), reverse=True)}\n')

    print('Merge Sort By List Conversion')
    print(f'{mergesort(people, key=lambda person: list(person))}\n')

    print('Reversed Merge Sort By Tuple Conversion')
    print(f'{mergesort(people, key=lambda person: tuple(person), reverse=True)}\n')

    print('Merge Sort By Index of List Conversion')
    print(f'{mergesort(people, key=lambda person: list(person)[0])}\n')

    print('Reversed Merge Sort By Index of Tuple Conversion')
    print(f'{mergesort(people, key=lambda person: tuple(person)[2], reverse=True)}\n')

if __name__ == '__main__':
    main()

