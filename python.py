hours = float(input("Enter hours: "))
rate = float(input("Enter rate: "))
pay = hours * rate
print(f"pay: {pay}")

while True:
    line = input(' > ')
    if line == 'done':
        break
    print(line)
print('Done!')

friends = ['Nwanunu', 'Ijele', 'Aloy']
for friend in friends:
    print('i love you:', friend)
print('Done')