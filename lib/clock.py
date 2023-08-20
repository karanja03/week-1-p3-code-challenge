def clock_conversion(time_str):
    hour_str, minute_str = time_str.split(":")
    minute, period = minute_str.split()

    if period.lower() == "pm" and int(hour_str) != 12:
        hour = int(hour_str) + 12
    elif period.lower() == "am" and int(hour_str) == 12:
        hour = 0
    else:
        hour = int(hour_str)

    hour_str = str(hour).zfill(2)

    return hour_str + minute
