# 재귀를 이용한 반복문

def addNumber(num):
    if num <= 1:
        return 1
    return num + addNumber(num-1)

print(addNumber(100))


# 우주선 발사 카운트 다운
def countDown(n):
    if n == 0:
        print('발사')
    else :
        print(n)
        countDown(n-1)

countDown(5)

# 별 모양 출력하기
def printStar(n):
    if n > 0:
        printStar(n-1)
        print('*'*n)

printStar(5)

# 구구단 출력하기
def gugu(dan, num):
    print("%d x %d = %d" %(dan,num,dan*num))
    if num < 9 :
        gugu(dan,num+1)

for dan in range(2, 10):
    print("## %d단 ##" % dan)
    gugu(dan, 1)

# n제곱 계산하기
tab =''
def pow(x, n):
    global tab
    tab += ' '
    if n == 0 :
        return 1
    print(tab + "%d*%d^(%d-%d)"%(x,x,n,1))
    return x * pow(x,n-1)
print('2^4')
print('답-->', pow(2,4))


# 배열의 합 계산하기
import random
def arySum(arr,n):
    if n <= 0:
        return arr[0]
    return arySum(arr,n-1)+arr[n]

ary = [random.randint(0,255) for _ in range
        (random.randint(10,20))]
print(ary)
print('배열 합계-->', arySum(ary,len(ary)-1))
