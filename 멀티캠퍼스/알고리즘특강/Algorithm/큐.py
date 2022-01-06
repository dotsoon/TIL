## 함수

## 전역
SIZE = 5
queue = [None for _ in range(SIZE)]
front=rear=-1                            #큐는 -1부터 시작 

## 메인
#enQueue 데이터 삽입
rear += 1                        # 꼬리를 추가 
queue[rear] = '화사'
rear += 1
queue[rear] = '솔라'
rear += 1
queue[rear] = '문별'
#deQueue 데이터 추출
front += 1
data = queue[front]
queue[front] = None             # 큐의 프론트자리 비우기 
print('식사할 손님 : ', data)
front += 1
data = queue[front]
queue[front] = None
print('식사할 손님 : ', data)
front += 1
data = queue[front]
queue[front] = None
print('식사할 손님 : ', data)

print('출구<--', queue, '<--입구')


