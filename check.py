def sum(n):
    if n // 2 != 0:
        n -= 1
        answer = n
    if 0 < n:
        answer += sum(n -2)
    return answer
print(sum(4))