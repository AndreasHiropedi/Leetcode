number_of_1s = []
        for i in range(n+1):
            count = 0
            string = "{0:b}".format(i)
            for char in string:
                if char == '1':
                    count = count + 1
            number_of_1s.append(count)
        return number_of_1s
