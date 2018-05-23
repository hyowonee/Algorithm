def solution(p, n):
    getAMPM = p.split(" ")[0]
    getTimeTwelve = p.split(" ")[1]
    getTimeHour = int(getTimeTwelve.split(":")[0])
    getTimeMinute = int(getTimeTwelve.split(":")[1])
    getTimeSecond = int(getTimeTwelve.split(":")[2])
    afterHour = int(n / 3600)
    afterMinute = int(n % 3600 / 60)
    afterSecond = int(n % 3600 % 60)
    resultMinute = getTimeMinute + afterMinute
    resultSecond = getTimeSecond + afterSecond

    if getTimeHour == 12:
        getTimeHour = 0

    if getAMPM == "PM":
        resultHour = getTimeHour + afterHour + 12
    else:
        resultHour = getTimeHour + afterHour

    if resultSecond >= 60:
        resultMinute = int(resultMinute + resultSecond / 60)
        resultSecond = resultSecond % 60

    if resultMinute >= 60:
        resultHour = int(resultHour + resultMinute / 60)
        resultMinute = resultMinute % 60

    resultHour %= 24

    if resultHour < 10:
        resultHour = "0" + str(resultHour)

    if resultMinute < 10:
        resultMinute = "0" + str(resultMinute)

    if resultSecond < 10:
        resultSecond = "0" + str(resultSecond)

    resultTime = "%s:%s:%s" % (resultHour, resultMinute, resultSecond)
    print(resultTime)
    
solution("PM 01:00:00", 10)
solution("PM 11:59:59", 1)
solution("AM 12:10:00", 40)