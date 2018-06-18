import inflect
p = inflect.engine()


if __name__ == '__main__':
    sum = 0
    for i in range(1,1001):
        sum += len(p.number_to_words(i).replace(' ','').replace('-',''))
    print(sum)
