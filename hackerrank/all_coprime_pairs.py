# https://allhackerranksolutionsbykaira.blogspot.com/2020/12/coprime-array-hackerearth-solution.html?m=1
def gcd(a, b):
    while 0 < a != b > 0:
        if a > b:
            a = a - b
        else:
            b = b - a
    if a == 0:
        return b
    if b == 0:
        return a
    if a == b:
        return a


def process(a):
    ans = 0
    for i in range(len(a)-1):
        for j in range(i+1, len(a)):
            if gcd(a[i], a[j]) == 1:
                ans = ((a[i]*a[j]) % 1000000007) % 1000000007
    return ans


if __name__ == '__main__':
    print(process([1, 3, 4, 8, 5, 12]))

