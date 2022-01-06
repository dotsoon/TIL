# 원형 큐 
## 함수
def isQueueFull() :
    global SIZE, queue, front, rear
    if ( (rear+1)%SIZE == front) :     # 원형 큐 
        return True
    else :
        return False

def enQueue(data) :
    global SIZE, queue, front, rear
    if (isQueueFull()) :
        print('큐 꽉!')
        return
    rear = (rear + 1) %SIZE            # 원형 큐 
    queue[rear] = data

def isQueueEmpty() :
    global SIZE, queue, front, rear
    if (front == rear) :               # 원형 큐 
        return True
    else :
        return False

def deQueue() :
    global SIZE, queue, front, rear
    if (isQueueEmpty()) :
        print('큐 텅~')
        return None
    front = (front + 1) %SIZE         # 원형 큐 
    data = queue[front]
    queue[front] = None
    return data

def peek() :
    global SIZE, queue, front, rear
    if (isQueueEmpty()) :
        print('큐 텅~')
        return None
    return queue[ (front+1) % SIZE]     # 원형 큐 

## 전역
SIZE = 5
queue = [None for _ in range(SIZE)]
front=rear=0                            # 원형 큐 

## 메인
enQueue('화사')
enQueue('솔라')
enQueue('문별')
enQueue('휘인')
enQueue('선미')
print('출구<--', queue, '<--입구')
print('입장 손님 : ', deQueue())
print('입장 손님 : ', deQueue())
print('출구<--', queue, '<--입구')
enQueue('선미')
print('출구<--', queue, '<--입구')