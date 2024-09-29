# https://contest.yandex.ru/contest/53033
def iterating(curr_length, curr_index):

    if curr_length == N:
        if len(used_bricks) < result[0]:
            result[0] = len(used_bricks)
            result[1] = used_bricks.copy()
        return
    elif curr_length > N or len(used_bricks) >= result[0]:
        return

    for i in range(curr_index, M):
        if brick_count[brick_lengths[i]] == 2:
            continue
        used_bricks.append(brick_lengths[i])
        brick_count[brick_lengths[i]] += 1
        iterating(curr_length + brick_lengths[i], i)
        used_bricks.pop()
        brick_count[brick_lengths[i]] -= 1


N, M = map(int, input().split())
brick_lengths = list(map(int, input().split()))
brick_lengths.sort(reverse=True)
used_bricks = []
brick_count = {length: 0 for length in brick_lengths}
result = [float('inf'), []]
max_length = sum([x * 2 for x in brick_lengths])
if max_length < N:
    print(-1)
else:
    iterating(0, 0)
    if result[0] == float('inf'):
        print(0)
    else:
        print(result[0], ' '.join(map(str, result[1])), sep='\n')
