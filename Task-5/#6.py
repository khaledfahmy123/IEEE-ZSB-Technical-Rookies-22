import bisect as bs



ranked_count = int(raw_input())

ranked = sorted(set(map(int, raw_input().split())))

player_count = int(raw_input())

player = map(int, raw_input().split())

for i in player:
	print(len(ranked) - bs.bisect_right(ranked, i) + 1)



print(score([100,100,50,40,40,20,10], [5,25,50,120]))
