# TODO : à refaire

def distinct_digits(year):
    new_year = str(year)
    return len(set(new_year)) == len(new_year)

while True:
    y += 1
    if distinct_digits(y):
        print(y)
        break