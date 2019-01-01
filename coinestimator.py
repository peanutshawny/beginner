coins = ['pennies','nickels','dimes','quarters','dollars']
weights = [2.5, 5, 2.25, 5.67,8]
values = [0.01, 0.05, 0.10, 0.25, 1]
wrappers = [50, 40, 50, 40, 25]


def main():
    num_coin = []
    wrapper_coin = []
    value_coin = []
    sum_coin = 0
    temp_num = 0

    for weight in range(0,5):
        print('Enter the weight of', coins[weight])
        temp_num = float(input()) / weights[weight]
        num_coin.append(temp_num)
        wrapper_coin.append(round(num_coin[weight] / wrappers[weight]))
        value_coin.append(num_coin[weight] * values[weight])

    sum_coin = sum(value_coin)

    for value in range(0,5):
        print('The number of', coins[value], 'is', round(num_coin[value]))

    print('')

    for value in range(0,5):
        print('The numbers of wrappers you will need for', coins[value], 'is', round(wrapper_coin[value]))

    print('')

    print('you have $', round(sum_coin), 'in total')
    end()


def end():
    response = input('Would you like to try again?')
    if response == "Yes":
        main()
    else:
        print('Thank you!')


print('Welcome to Coin Estimator!')
print('')
main()

# num_penny = int(input('Please input weight of pennies '))/weights['penny']
# num_nickel = int(input('Please input weight of nickel ')) / weights['nickel']
# num_dime = int(input('Please input weight of dimes ')) / weights['dime']
# num_quarter = int(input('Please input weight of quarter ')) / weights['quarter']
# num_dollar = int(input('Please input weight of dollar ')) / weights['dollar']
#
# sum_coin = int(num_penny * 0.01 + num_nickel * 0.05 + num_dime * 0.1 + num_quarter * 0.25 + num_dollar)
#
# wrapper_penny = round(num_penny / wrapper['penny'])
# wrapper_nickel = round(num_nickel / wrapper['nickel'])
# wrapper_dime = round(num_dime / wrapper['dime'])
# wrapper_quarter = round(num_quarter / wrapper['quarter'])
# wrapper_dollar = round(num_dollar/ wrapper['dollar'])
#
# print('you have', num_penny, 'pennies')
# print('you have', num_nickel, 'nickels')
# print('you have', num_dime, 'dimes')
# print('you have', num_quarter, 'quarters')
# print('you have', num_dollar, 'dollars')
# print('')
# print('you will need', wrapper_penny, 'penny wrappers')
# print('you will need', wrapper_nickel, 'nickel wrappers')
# print('you will need', wrapper_dime, 'dime wrappers')
# print('you will need', wrapper_quarter, 'quarter wrappers')
# print('you will need', wrapper_dollar, 'dollar wrappers')
# print('')
# print('you have a total of $', sum_coin)

