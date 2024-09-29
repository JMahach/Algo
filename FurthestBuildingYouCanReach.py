# https://leetcode.com/problems/furthest-building-you-can-reach/description/
heights = [4, 2, 7, 6, 9, 14, 12]
bricks = 5
ladders = 1


def furthest_building(heights, bricks, ladders, i=0):
    result = i
    if i != len(heights) - 1:
        if heights[i] > heights[i + 1]:
            i += 1
            if i == len(heights) - 1:
                return i
        if (diff := heights[i + 1] - heights[i]) <= bricks:
            bricks -= diff
            i += 1
            result = max(result,
                         furthest_building(heights, bricks, ladders, i))
            i -= 1
            bricks += diff
        if ladders:
            ladders -= 1
            i += 1
            result = max(result,
                         furthest_building(heights, bricks, ladders, i))
            i -= 1
            ladders += 1
        return max(result, i)
    return result


def furthest_building2(heights, bricks, ladders):
    import heapq
    heap = []
    i = 0
    while i != len(heights) - 1:
        if heights[i] > heights[i + 1]:
            i += 1
        elif ladders:
            heapq.heappush(heap, heights[i + 1] - heights[i])
            ladders -= 1
            i += 1
        elif heap:
            if (bricks - heap[0] < 0 and
                    bricks - (heights[i + 1] - heights[i]) < 0):
                break
            elif heap[0] < (heights[i + 1] - heights[i]):
                bricks -= heapq.heappop(heap)
                heapq.heappush(heap, heights[i + 1] - heights[i])
                i += 1
            else:
                bricks -= heights[i + 1] - heights[i]
                i += 1
        elif bricks - (heights[i + 1] - heights[i]) >= 0:
            bricks -= heights[i + 1] - heights[i]
            i += 1
        else:
            break
    return i
