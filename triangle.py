def pythagorean_triple():
    side_1 = input("Please input side 1")
    side_2 = input("Please input side 2")
    side_3 = input("Please input side 3")

    side_list = [side_1, side_2, side_3]

    hypotenuse = int(max(side_list))
    other_sides = list(map(int,[side for side in side_list if side != hypotenuse]))
    if other_sides[0]**2 + other_sides[1]**2 == hypotenuse**2:
        print('YES')
    else:
        print('NO')
    end()


def end():
    response = input("Would you like to try again?")
    if response == 'Yes':
        pythagorean_triple()
    else:
        print('Thank you come again next time!')


print('Welcome to Pythagorean Triples!')
pythagorean_triple()
