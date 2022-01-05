## 함수부
def add_data(friend) :       # 선형 리스트에 추가 
    katok.append(None)
    kLen = len(katok)
    katok[kLen-1] = friend

def insert_data(position, friend) :      # 중간에 추가 함수
    katok.append(None)                   # 새로운 칸 만들기
    kLen = len(katok)                    
    for i in range(kLen-1, position, -1):    # 추가하고 하나씩 떙기는작업
        katok[i] = katok[i-1]
        katok[i-1] = None                   # 땡기고 난 빈칸
    katok[position] = friend                # 빈칸에 포지션값 넣기

def delete_data(position) :               # 중간에 삭제 함수
    katok[position] = None               # 포지션값 비우기
    kLen = len(katok)
    for i in range(position+1, kLen, 1) :  # 지우고 하나씩 땡기는 작업
        katok[i-1] = katok[i]            
        katok[i] = None 
    del(katok[kLen-1])                    #마지막칸삭제


## 전역변수부
katok = []   # 선형 리스트


## 메인코드부
add_data('다현')
add_data('정연')
add_data('쯔위')
add_data('사나')
add_data('지효')

print(katok)
add_data('모모')
print(katok)

insert_data(3,'미나')
insert_data(5,'유정')

delete_data(4)            # 사나 삭제

print(katok)