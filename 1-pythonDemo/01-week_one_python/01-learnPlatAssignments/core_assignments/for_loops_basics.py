for ints in range(0,51):
    print(ints)

for multiples_of_5 in range(5,1005,5):
    print(multiples_of_5)

for ints in range(1,101):
    if ints %10 == 0:
        print('Coding Dojo')
    elif ints %5 == 0:
        print('Coding')
    else:
        print(ints)

final_sum = 0
for ints in range(500001):
    if ints %2 == 1:
        final_sum = ints + final_sum
print(final_sum)

for positive_vibes in range(2018,0,-4):
    print(positive_vibes)

low_Num = 2
high_Num = 9
mult = 3
for integers in range(low_Num, high_Num+1):
    if integers % mult == 0:
        print(integers)
  