import re
def General():
    fh = open('regex_sum_689538.txt')
    sum1 = 0
    nums = []
    for line in fh:
        nums = nums + re.findall('[0-9]+',line)
    for n in nums:
        n = int(n)
        sum1 = sum1 + n
    print('Sum using General medhod:',sum1)

    return

def UsingListComprehsion():
    fh = open('regex_sum_689538.txt')
    print('Sum using List Comprehsion:',sum([int(i) for i in re.findall('[0-9]+',fh.read())  ]))

    return
if __name__ =='__main__':
    General()
    UsingListComprehsion()
