import heapq


def calc_time_period(time1:int, time2:int) -> int:
    return abs(time1-time2)


def str2time(time:str) -> int:
""" convert hh:mm:ss to hhmmss as int"""
    return int("".join(time.split(':')))
    # return int("".join([x for x in time if x != ':'])) # 1/3 slower than above


def get_time_period(time1:str, time2:str) -> int:
    return calc_time_period(str2time(time1), str2time(time2))


if __name__ == "__main__":
    N:int = int(input())
    K:int = int(input())

    period = dict()
    in_time = dict()
    out_time = dict()
    queries = []

    for _ in range(N):
        s = input()
        s = s.split(' ')
        t_plate = s[0]
        t_time = str2time(s[1])
        t_flag = s[2]
        if t_flag == "in":
            if t_plate in in_time.keys():
                in_time[t_plate].append(t_time)
            else:
                in_time[t_plate] = [t_time]
        elif t_flag == "out":
            if t_plate in out_time.keys():
                out_time[t_plate].append(t_time)
            else:
                out_time[t_plate] = [t_time]

    for _ in range(K):
        s = str2time(input())
        queries.append(s)

    for i in in_time.keys():
        in_time[i].sort()
    for i in out_time.keys():
        out_time[i].sort()

    for t in len(queries):
        car_cnt = 0
        i_in = 0
        p_in = 1
        i_out = 0
        p_out = 1
        for key in in_time.keys():
            # 注意越界
            while in_time[key][i_in] > out_time[key][i_out]: # 要求 in_time 正序， 一开始，如果当前的 in 记录比当前的 out 记录大，那么删除当前的 out 记录
                del out_time[key][i_out]
            while in_time[key][p_in] < out_time[key][i_out] and in_time[key][i_in] < out_time[key][i_out]: # 要求 in_time 正序，如果下一个 in 记录比当前的 out 记录要小，同时当前的 in 记录比当前的 out 记录也要小，那么删除当前的 in 记录
                del in_time[key][i_in]
            while :

