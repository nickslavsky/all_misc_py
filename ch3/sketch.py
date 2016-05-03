try:
        data = open('sketch.txt')
        for each_line in data:
                try:
                        (role, line) = each_line.split(':',1)
                        print(role + ' said: ' + line, end='')
                except ValueError:
                        #pass
                        print(each_line, end='')
        data.close()
except IOError:
        print('File is missing')

