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
select = -1

## 메인코드부

if __name__ == "__main__" :
    while (select != 4) :
        select = int(input("선택하세요(1:추가,2:삽입,3:삭제,4:종료)-->"))

        if (select == 1):
            data = input("추가할 데이터 -->")
            add_data(data)
            print(katok)

        elif (select == 2):
            pos = int(input("삽입할 위치-->"))
            data = input("추가할 데이터-->")
            insert_data(pos,data)
            print(katok)

        elif (select == 3) :
            pos = int(input("삭제할 위치-->"))
            delete_data(pos)
            print(katok)
        elif (select == 4) :
            print(katok)
            exit
        else:
            print("1~4중 하나를 입력하세요")
            continue