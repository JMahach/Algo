# https://leetcode.com/problems/meeting-rooms-iii/description/
# flake8: noqa
import heapq


def mostBooked(n, meetings):
    i = 0
    room_number_map = [[True, 0] for _ in range(n)]
    meetings_dict = {}
    done_meetings = 0
    heap_busy_room = []
    for el in meetings:
        meetings_dict[el[0]] = [el[1] - el[0]]

    def get_room_num(room_number_map):
        for i in range(len(room_number_map)):
            if room_number_map[i][0] is True:
                room_number_map[i][0] = False
                room_number_map[i][1] += 1
                return i
        return False

    while len(meetings) != done_meetings:
        while heap_busy_room and heap_busy_room[0][0] == i:
            time, room = heapq.heappop(heap_busy_room)
            room_number_map[room][0] = True
        if meetings_dict.get(i):
            while (
                meetings_dict.get(i)
                and (room := get_room_num(room_number_map)) is not False
            ):
                done_meetings += 1
                heapq.heappush(heap_busy_room, (i + meetings_dict[i].pop(), room))

            meetings_dict[i + 1] = meetings_dict.get(i + 1, [])
            meetings_dict[i + 1].extend(meetings_dict[i])
            meetings_dict[i] = []
        i += 1

    result = 0
    max_meeting = 0
    for i in range(len(room_number_map)):
        if room_number_map[i][1] > max_meeting:
            result = i
            max_meeting = room_number_map[i][1]

    return result


def mostBooked2(n, meetings):
    ans = [0] * n
    times = [0] * n
    meetings.sort()

    for start, end in meetings:
        flag = False
        minind = -1
        val = float('inf')
        for j in range(n):
            if times[j] < val:
                val = times[j]
                minind = j
            if times[j] <= start:
                flag = True
                ans[j] += 1
                times[j] = end
                break
        if not flag:
            ans[minind] += 1
            times[minind] += (end - start)

    maxi = -1
    id = -1
    for i in range(n):
        if ans[i] > maxi:
            maxi = ans[i]
            id = i
    return id
