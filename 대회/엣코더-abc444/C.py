import sys
input =sys.stdin.readline 

#그대로거나 합치거나 둘 중 하나 
#합친숫자는 다시 합쳐질 수 없음, 모든수를 같게 만드는 문제 (답은 보장되어 있다고 함)

#N은 30만개, 각 수는 10억 이하 
#NlogN이 가능한가? 이분탐색? 
#모든수가 똑같아야함 ==> 정답후보는 일단 고를 수 있음 
#다 더해서 gcd로 나눔? 

N = int(input())
nums = map(int, input().split())

