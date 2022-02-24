# №1
def nums_generator(n=20):
    for code in range(1, n + 1):
        if code % 2 == 1:
            yield code


numbers = nums_generator()
print(*numbers)
print(type(numbers))

# №2
n = 20
nums_gen = (nums for nums in range(1, n + 1) if nums % 2 == 1)
print(*nums_gen)
print(type(nums_gen))

# №3
tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Борис', 'Елена'
]
klasses = [
    '9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А'
]


def gen_in_classes():
    i = 0
    j = 0
    while i < len(klasses):
        if i >= len(tutors):
            yield None, klasses[i]
            i += 1
            j += 1
        else:
            yield tutors[j], klasses[i]
            i += 1
            j += 1


for person in gen_in_classes():
    print(person)

print(type(gen_in_classes()))


# №4
src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

gen_src = ([src[num] for num in range(len(src)) if src[num] > src[num - 1]])
print(*gen_src)

