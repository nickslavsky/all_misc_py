import random
import pickle


def populate(filename, amount: object = 10):
    hours_minutes_seconds = []
    try:
        with open(filename, 'wb') as file:
            for each_i in range(amount):
                hours_minutes_seconds.append([random.randrange(12), random.randrange(60), random.randrange(60)])
            pickle.dump(hours_minutes_seconds, file)
    except IOError as ioerr:
        print('File Error: ' + str(ioerr))

populate('data.txt', 10000)
