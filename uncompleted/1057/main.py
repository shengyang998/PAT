# 1057 Stack
# currect but out of time

if __name__ == "__main__":
    n = int(input())
    stack = []
    for _ in range(n):
        s = input()
        s = s.split(' ')
        if len(s) == 1:
            if s[0] == 'Pop':
                if stack == []:
                    print("Invalid")
                else:
                    print(stack.pop())
            elif s[0] == 'PeekMedian':
                if stack == []:
                    print("Invalid")
                else:
                    res = sorted(stack, reverse=True)
                    if len(stack) % 2 == 0:
                        print(res[int(len(stack)/2)])
                    else:
                        print(res[round(len(stack)/2)-1])
        else:
            stack.append(int(s[1]))


