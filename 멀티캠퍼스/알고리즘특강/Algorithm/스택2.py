## 함수
def isStackFull():               # 스택이 꽉 찼는지 확인
    global SIZE, stack, top
    if ( top >= SIZE-1 ) :
        return True
    else : 
        return False

def push(data) :                 
    global SIZE, stack, top
    if (isStackFull()) : 
        print('스택 꽉 찼다')
        return
    top += 1
    stack[top] = data

def isStackEmpty():             # 스택이 비었는지 확인
    global SIZE, stack, top
    if ( top <= -1 ) :
        return True
    else : 
        return False

def pop() :
    global SIZE, stack, top
    if (isStackEmpty()):
        print('스택이 비어있다')
        return None
    data = stack[top]
    stack[top] = None
    top -= 1
    return data

def peek() :                   # 다음에 나올 값을 미리 확인
    global SIZE, stack, top
    if (isStackEmpty()) : 
        print('스택이 비어있다')
        return None
    return stack[top]

## 전역
SIZE = 5
stack = [None for _ in range(SIZE)]
top = -1 


## 메인
# stack = ['커피', '녹차', '꿀물', '콜라', '환타']
# top = 4

# stack = ['커피', '녹차', '꿀물', '콜라', '환타']
# top = 3
# 
# push('보리차')
# print(stack)
# push('사이다')
# print(stack)

stack = ['커피', '녹차', '꿀물', '콜라', '환타']
top = 0

print('다음나올예정:', peek())
print(pop())
print(pop())

