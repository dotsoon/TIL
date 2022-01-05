## 함수
class Node() :                    # 노드 생성 약속!!통째로 그냥 외우기
    def __init__(self):
        self.data = None
        self.link = None

def printNodes(start):
    current = start                   # node1에서 모든노드 print하기
    print(current.data, end=' ')
    while current.link != None :      # 노드링크가 none이 아닐 때까지
      current = current.link          # 연결된 링크 프린트 
      print(current.data, end=' ')
    print()

# 첫번째 노드 삽입 
def insertNode(findData, insertData) :     # 헤드 다현을 찾아서 화사를 삽입
    global memory, head, current, pre      # 그냥 무조건 하는거
    if head.data == findData :             # 헤드 데이터가 내가 찾고자 하는 데이터
        node = Node()                      # 화사 생성
        node.data = insertData             # 데이터에 화사 삽입
        node.link = head                   # 화사를 헤드랑 연결
        head = node                        # 헤드 노드를 화사로 지정 
        return

# 중간에 노드 삽입 
    current = head                         # 헤드를 먼저 찾기
    while current.link != None :           # 노드 링크가 없는곳 까지
        pre = current                      # 프리가 커렌트를 잡고있기
        current = current.link             
        if current.data == findData :      # 커렌트가 찾던데이터면 
            node = Node()                  # 빈노드 생성
            node.data = insertData         # 빈노드에 삽입
            node.link = current            # 다음 링크 연결
            pre.link = node                # 프리 노드랑 연결 
            return 

# 마지막에 노드 삽입
    node = Node()                          # 빈 노드 생성
    node.data = insertData         
    current.link = node
    return

# 첫번째 노드 삭제
def deleteNode(deleteData) :
    global memory, head, current, pre
    if head.data == deleteData :          # 지우려는 데이터가 헤드데이터
        current = head                    # 커런트를 헤드로
        head = head.link                  # 헤드를 옆노드로 옮겨주기
        del(current)
        return
    # 첫노드 외 삭제
    current = head                        # 커런트를 헤드로지정
    while current.link != None :          # 커런트링크가 없을떄까지
        pre = current                     # 프리가 커런트를 앞에서 잡도록
        current = current.link       
        if current.data == deleteData :   # 커런트데이터가 지울데이타인경우
            pre.link = current.link       # 프리를 다음링크랑 연결
            del(current)                  # 지우기
            return

# 노드 찾기
def findNode(findData) : 
    global memory, head, current, pre
    current = head                       # 머리부터 찾기
    if current.data == findData :        # 커렌트가 찾는 데이타면
        return current
    while current.link != None :         # none이 아닐 때까지
        current = current.link 
        if current.data == findData :        
             return current
    return Node()





## 전역
memory = []
head, current, pre = None, None, None
dataArray = ['다현', '정연', '쯔위', '사나', '지효']

## 메인
node = Node()   # 첫 노드
node.data = dataArray[0]
head = node     # 첫번째 노드를 헤드로 지정
memory.append(node)

for data in dataArray[1:] :   # ['정연', '쯔위', '사나', '지효']
    pre = node                # 첫번째 노드를 pre로 잡고있음
    node = Node()             # 새로운 빈 노드 생성
    node.data = data          # 빈 노드에 data 들어감 
    pre.link = node           # 이전(pre)의 링크를 새 노드에 대입
    memory.append(node)       # 새 노드를 메모리에 넣음 

printNodes(head)              # head부터 출력 

insertNode('다현', '화사')
printNodes(head)
insertNode('사나', '솔라')
printNodes(head)
insertNode('재남', '문별')
printNodes(head)

deleteNode('화사')
printNodes(head)

deleteNode('쯔위')
printNodes(head)

deleteNode('원빈')
printNodes(head)


fNode = findNode('지효')
print(fNode.data)
fNode = findNode('재남')
print(fNode.data)