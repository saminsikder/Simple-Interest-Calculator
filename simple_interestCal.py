#Find yearly Interst

print('For how many years will you be saving Samin?')
years = int(input('Enter in years: '))

print('How much is currently in your account/the principal money?')
principal = float(input('Enter current amouont: '))

print('How much money do you plan on investing monthly?')
monthly_investment = float(input('Enter amount: '))

print('What is the yearly estimate of this investment?')
interest = float(input('Enter interst in decimal (10% = 0.1): '))

print(' ')

monthly_investment = monthly_investment * 12
final_amount = 0

for i in range(0, years):
    if final_amount ==0:
        final_amount = principal 

    final_amount = (final_amount + monthly_investment) * (1 + interest)

print('This is how much you would have in your account after {} years: '.format(years) + str(final_amount))