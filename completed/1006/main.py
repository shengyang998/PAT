# 1006 Sign in and sign out
#


if __name__ == "__main__":
    s = input()
    M = int(s.split(' ')[0])
    t = []
    for i in range(M):
        s = input()
        name, s_in, s_out = s.split(' ')
        s_in_t = ''
        s_out_t = ''
        s_in = s_in.split(':')
        s_out = s_out.split(":")
        for j in s_in:
            s_in_t = s_in_t.join(j)
        for j in s_out:
            s_out_t = s_out_t.join(j)
        s_in_t = int(s_in_t)
        s_out_t = int(s_out_t)
        t.append((name, s_in_t, s_out_t))
    min_x = min(t, key=lambda x: x[1])
    max_x = max(t, key=lambda x: x[2])
    print(min_x[0], max_x[0])




