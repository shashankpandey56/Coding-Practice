def reorder_log(logs):
    digit_logs, letter_logs = [],[]
    for log in logs:
        second = log.split()[1]
        if second.isdigit():
            digit_logs.append(log)
        else:
            letter_logs.append(log)
    letter_logs.sort(key = lambda x: x.split()[0])
    letter_logs.sort(key = lambda x: x.split()[1:])

    print(letter_logs + digit_logs)






logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
reorder_log(logs)