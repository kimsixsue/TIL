# https://tech.kakao.com/2021/01/25/2021-kakao-recruitment-round-1/
def solution(play_time, adv_time, logs):  # 정답률 : 1.23%
    def time_to_sec(hhmmss):  # 시각을 초로 환산하여 저장
        hh, mm, ss = map(int, hhmmss.split(':'))
        return hh * 3600 + mm * 60 + ss

    # 00시간 00분 01초 이상 99시간 59분 59초 이하
    play_sec = time_to_sec(play_time)
    adv_sec = time_to_sec(adv_time)
    total_sec = [0 for _ in range(play_sec + 1)]
    for _ in logs:
        start_sec = time_to_sec(_[:8])  # H1:M1:S1
        end_sec = time_to_sec(_[9:])  # H2:M2:S2
        total_sec[start_sec] += 1  # 시작된 재생 구간의 개수 – 종료된 재생 구간의 개수
        total_sec[end_sec] -= 1
    for _ in range(1, play_sec + 1):  # 초 간의 구간을 포함하는 재생 구간의 개수
        total_sec[_] += total_sec[_ - 1]
    for _ in range(1, play_sec + 1):  # 초 간의 구간을 포함하는 "누적" 재생시간
        total_sec[_] += total_sec[_ - 1]
    acc = total_sec[adv_sec - 1]
    best_time = 0
    for play in range(adv_sec, play_sec):  # adv_sec <= play_sec
        if acc < total_sec[play] - total_sec[play - adv_sec]:
            acc = total_sec[play] - total_sec[play - adv_sec]
            best_time = play - adv_sec + 1
    h = "0" + str(best_time // 3600)
    m = "0" + str((best_time % 3600) // 60)
    s = "0" + str((best_time % 3600) % 60)
    answer = ":".join([h[-2:], m[-2:], s[-2:]])
    return answer  # HH:MM:SS


print(solution("02:03:55", "00:14:15",  # result = "01:30:59"
               ["01:20:15-01:45:14", "00:40:31-01:00:00", "00:25:50-00:48:29", "01:30:59-01:53:29",
                "01:37:44-02:02:30"]))
print(solution("99:59:59", "25:00:00",  # result = "01:00:00"
               ["69:59:59-89:59:59", "01:00:00-21:00:00", "79:59:59-99:59:59", "11:00:00-31:00:00"]
               ))
print(solution("50:00:00", "50:00:00",  # result = "01:30:59"
               ["15:36:51-38:21:49", "10:14:18-15:36:51", "38:21:49-42:51:45"]
               ))
