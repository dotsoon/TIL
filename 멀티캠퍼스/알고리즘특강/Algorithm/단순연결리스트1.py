# 함수
class Node() :                    # 노드 생성 약속!!통째로 그냥 외우기
    def __init__(self):
        self.data = None
        self.link = None

# 전역


# 메인
node1 = Node()
node1.data = '다현'

node2 = Node()
node2.data = '정현'
node1.link = node2

node3 = Node()
node3.data = '쯔위'
node2.link = node3

node4 = Node()
node4.data = '사나'
node3.link = node4

node5 = Node()
node5.data = '지효'
node4.link = node5

# newNode = Node()              # 노드삽입하기 새노드만들기
# newNode.data = '재남'         # 새 노드
# newNode.link = node2.link   
# node2.link = newNode

# node2.link = node3.link       #노드삭제하기
# del(node3)

# print(node1.data, end=' ')
# print(node1.link.data, end=' ')
# print(node1.link.link.data, end=' ')

current = node1                   # node1에서 모든노드 print하기
print(current.data, end=' ')
while current.link != None :      # 노드링크가 none이 아닐 때까지
    current = current.link        # 연결된 링크 프린트 
    print(current.data, end=' ')
