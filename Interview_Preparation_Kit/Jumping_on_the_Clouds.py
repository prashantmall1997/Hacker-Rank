# https://www.hackerrank.com/challenges/jumping-on-the-clouds/problem

jump = 0
start = 0
# clouds = int(input())
# cloud_type = list(map(int, input().split()))
clouds = 50
cloud_type = [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0,
              0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0]

for i in range(clouds):
    if start < clouds:
        if start < clouds-2 and cloud_type[start+2] == 0:
            jump += 1
            start += 2
        elif start < clouds-1 and cloud_type[start+1] == 0:
            jump += 1
            start += 1

print(jump)
