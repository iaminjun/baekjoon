# 입력
n, k = map(int, input().split())
ai = []

for _ in range(n):
  ai.append(int(input()))


'''
pointer : 가장 큰금액의 위치를 가리킴 
1. money(시작값 0)에 pointer가 가리키는 위치의 액수를 더함
2. 타겟금액보다 크면 더하기 취소하고 pointer는 하나 작은 금액을 가리킴 -> 1번으로 
3. 타겟금액보다 작으면 counter는 하나 증가 pinter는 그대로 -> 1번으로 
4. 타겟금액이 되면 반복문 종료
'''
money = 0
point = n - 1
count = 0

while True:

  if money + ai[point] > k:
    point -= 1
    continue
  else:
    money += ai[point]
    count +=1 

  if money == k:
    break

print(count)
