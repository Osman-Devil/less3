# №2
our_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
our_list1 = []
for elements in our_list:
    if elements.isdigit():
        our_list1.extend(['"', f'{int(elements):02}', '"'])
    elif elements.startswith('+' or '-'):
        if elements[1:].isdigit():
            our_list1.extend(['"', f'{elements[0]}{int(elements):02}', '"'])
        else:
            our_list1.append(elements)
    else:
        our_list1.append(elements)

print(our_list1)
our_list1 = ' '.join(our_list1)
print(our_list1)