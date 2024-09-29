# https://contest.yandex.ru/contest/53032/
def rec(seq, open_cnt_f, close_cnt_f, open_cnt_k, close_cnt_k):
    if len(seq) == N:
        print(seq)
        return
    if open_cnt_f + open_cnt_k < N/2:
        stack.append('(')
        rec(seq + '(', open_cnt_f + 1, close_cnt_f, open_cnt_k, close_cnt_k)
        stack.pop()
    if open_cnt_k + open_cnt_f < N/2:
        stack.append('[')
        rec(seq + '[', open_cnt_f, close_cnt_f, open_cnt_k + 1, close_cnt_k)
        stack.pop()
    if stack and stack[-1] == '(':
        stack.pop()
        rec(seq + ')', open_cnt_f, close_cnt_f + 1, open_cnt_k, close_cnt_k)
        stack.append('(')
    if stack and stack[-1] == '[':
        stack.pop()
        rec(seq + ']', open_cnt_f, close_cnt_f, open_cnt_k, close_cnt_k + 1)
        stack.append('[')


stack = []
N = int(input())
if N % 2 == 0:
    rec('', 0, 0, 0, 0)
