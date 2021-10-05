# 입력
n = int(input())
pi = list(map(int, input().split()))

'''
가장 시간이 적게 걸리는 고객부터 인출하면 시간 단축 가능
1. 오름차순 정렬 (시간이 적게 걸리는 고객순서)
2. 각자 기다리는 시간을 저장하느 배열 (앞순서 사람이 기다리는 시간 +_내가 처리하는시간 -> 누적합 배열)
3. 누적합 배열의 합은 모든 고객이 총 기다리는 시간
'''
pi.sort()
p_sum = []

temp = 0
for p in pi:
  temp += p
  p_sum.append(temp)

print(sum(p_sum))  
