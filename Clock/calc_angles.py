import pickle


def angle(hours, minutes, seconds):
    hour_hand = (3600 * hours + 60 * minutes + seconds)/120
    minute_hand = (60 * minutes + seconds)/10
    temp = abs(hour_hand - minute_hand)
    return min((360-temp), temp)
try:
    with open('data.txt', 'rb') as data:
        hms = pickle.load(data)
        for each in hms:
            print(str(angle(each[0], each[1], each[2])))
except IOError as ioerr:
    print('File Error: ' + str(ioerr))


