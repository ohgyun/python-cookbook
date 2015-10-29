# 순환이나 프로세싱 중 마지막으로 발견한 N개의 아이템 유지하고 싶다.


# 이런 목적으론 collection.deque 가 가장 적합한다.

# deque는 큐 구조체가 필요할 때 사용할 수 있다.
# deque(maxlen=N)으로 고정 크기 큐를 생성할 수 있으며,
# 큐가 찬 상태에서 새 아이템을 넣으면 첫 아이템이 자동으로 삭제된다.
from collections import deque

q = deque(maxlen=3)
q.append(1)
q.append(2)
q.append(3)
print(q) #-> deque([1, 2, 3], maxlen=3)
q.append(4)
print(q) #-> deque([2, 3, 4], maxlen=3)


# 그 외에도 양쪽에 아이템을 넣거나 뺄 수 있다.
q.appendleft(5)
print(q) #-> deque([5, 2, 3], maxlen=3)
x = q.pop()
print(x) #-> 3
print(q) #-> deque([5, 2], maxlen=3)
x = q.popleft()
print(x) #-> 5
print(q) #-> deque([2], maxlen=3)


# deque를 활용해서, 특정 파일에서 간단한 텍스트 매칭을 수행하고,
# 처음으로 발견한 N라인을 출력하는 함수를 아래와 같이 작성할 수 있다.

def search(lines, pattern, history=5):
    previous_lines = deque(maxlen=history)
    for line in lines:
        if pattern in line:
            yield line, previous_lines
        previous_lines.append(line)

if __name__ == '__main__':
    with open('somefile.txt') as f:
        for line, prevlines in search(f, 'python', 5):
            for pline in prevlines:
                print(pline, end='')
            print(line, end='')
            print('-'*20)









