import sys

seconds = sys.argv[1]
if int(seconds) < 10:
    print('%02i' % int(seconds))
elif int(seconds) >= 10 and int(seconds) < 60:
    print(seconds)
elif int(seconds) >= 60 and int(seconds) < 3600:
    M = int(seconds) // 60       # minutes
    S = int(seconds) % 60        # seconds in minute
    print('%02i:%02i' % (M, S))
elif int(seconds) >= 3600 and int(seconds) < 86400:
    H = int(seconds) // 3600
    M = (int(seconds) % 3600) // 60
    S = (int(seconds) % 3600) % 60
    print('%02i:%02i:%02i' % (H, M, S))