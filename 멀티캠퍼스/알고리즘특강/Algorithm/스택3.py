
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



SIZE = 5
stack = [None for _ in range(SIZE)]
top = -1 

stack = ['커피', '녹차', '꿀물', '콜라', '환타']
top = 0


if __name__ =="__main__" :
    select = input('삽입(I)/추출(E)/확인(V)/종료(X) 중 하나를 선택==>')

    while(select !='X' and select !='x'):
        if select =='I' or select =='i' :
            data =input('입력할데이터 ==>')
            push(data)
            print('스택상태:', stack)
        elif select =='E' or select =='e':
            data = pop()
            print('추출된 데이터 ==>', data)
            print('스택상태:',stack)
        elif select =='V' or select =='v':
            data = peek()
            print('확인된 데이터 ==>', data)
            print('스택 상태:', stack)
        else:
            print('입력이잘못됨')

        select = input('삽입(I)/추출(E)/확인(V)/종료(X) 중 하나를 선택==>')



print('프로그램 종료!')