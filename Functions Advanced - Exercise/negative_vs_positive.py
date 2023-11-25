def operations(*args):
    def negatives():
        negatives_sum = sum([x for x in args if x < 0])
        print(negatives_sum)
        return negatives_sum

    def positives():
        positives_sum = sum([x for x in args if x > 0])
        print(positives_sum)
        return positives_sum

    if abs(negatives()) < abs(positives()):
        return "The positives are stronger than the negatives"
    else:
        return "The negatives are stronger than the positives"


numbers = [int(x) for x in input().split()]
print(operations(*numbers))