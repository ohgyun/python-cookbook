# 언패킹

p = (4, 5)
x, y = p
print(x) #-> 4
print(y) #-> 5


# 언패킹은 튜플이나 리스트 뿐 아니라 순환 가능한 모든 객체에 적용할 수 있다.
# 여기엔 문자열, 파일, 이터레이터, 제너레이터가 포함된다.

s = 'Hello'
a, b, c, d, e = s

print(a) #-> 'H'
print(b) #-> 'e'
print(c) #-> 'l'
print(d) #-> 'l'
print(e) #-> 'o'


# 언패킹할 때 특정 값을 무시하는 경우 관례적으로,
# _ 또는 ign(ignored) 변수를 사용한다.

data = ['foo', 'bar', 'baz']
x, _, y = data

print(x) #-> 'foo'
print(y) #-> 'baz'


# 요소개 여러 개 이상인 경우 별 표현식(애스태리크, *)를 사용할 수 있다.
# 실제로 * 는 splat operator 이며, 이런 방식을 길이를 알 수 없는 순환체에 안성맞춤이다.

# 예를 들어, 처음과 끝 값을 제외한 평균을 구한다면 아래와 같이 작성할 수 있다.

def drop_first_last(grades):
    first, *middle, last = grades
    return avg(middle)


# 튜플을 언패킹하는 경우, 배열을 얻을 수 있다.

data = ('a', 'b', 'c', 'd')
x, *y = data
print(x) #-> 'a'
print(y) #-> ['b', 'c', 'd']


# 별표가 붙어있는 변수를 리스트의 앞에서 쓸 수도 있다.

data = 'Hello'
*x, y = data
print(x) #-> ['H', 'e', 'l', 'l'] 
print(y) #-> 'o'


# 중간값을 버리고 앞/뒤 값만 취하고 싶다면 아래처럼 작성해도 좋다.

data = ('first', 80, 'foo', 'bar', 'last')
head, *_, tail = data
print(head) #-> 'first'
print(tail) #-> 'last'


# 함수형처럼 재귀 알고리즘으로 아래처럼 함수를 작성할 수도 있다.
# (하지만 파이썬의 재귀적 제약이 존재하기 때문에 실질적으로 사용하기엔 무리가 있다)

def sum(items):
    head, *tail = items
    return head + sum(tail) if tail else head