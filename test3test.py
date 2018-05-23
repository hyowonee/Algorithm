def solution(p, n):
    getAMPM = p.split(" ")[0]
    getTimeTwelve = p.split(" ")[1]
    hour = int(getTimeTwelve.split(":")[0])
    minute = int(getTimeTwelve.split(":")[1])
    second = int(getTimeTwelve.split(":")[2])

    second += n
    
    if hour == 12:
        hour = 0

    if getAMPM == "PM":
        hour += 12

    hour += int(second / 3600)
    minute += int(second % 3600 / 60)
    second = int(second % 3600 % 60) 

    if minute >= 60:
      minute %= 60
      hour += 1

    hour %= 24

    if hour < 10:
        hour = "0" + str(hour)

    if minute < 10:
        minute = "0" + str(minute)

    if second < 10:
        second = "0" + str(second)

    resultTime = "%s:%s:%s" % (hour, minute, second)
    print(resultTime)
    
solution("PM 01:00:00", 10)
solution("PM 11:59:59", 1)
solution("AM 12:10:00", 40)