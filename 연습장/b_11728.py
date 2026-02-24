import sys
input = sys.stdin.readline 

N1, N2 = map(int, input().split())

nums1 = list(map(int, input().split()))
nums2 = list(map(int, input().split()))

p1 = 0
p2 = 0 

nums3 = []
while p1 < N1 and p2 < N2:
    if nums1[p1] <= nums2[p2]:
        nums3.append(nums1[p1])
        p1 += 1
    else:
        nums3.append(nums2[p2])
        p2 += 1

if p1 == N1:
    nums3 += nums2[p2:]
elif p2 == N2:
    nums3 += nums1[p1:]

print(" ".join(map(str, nums3)))