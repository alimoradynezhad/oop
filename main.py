lst = ['11', 'pooya', '10', None, '10.5']

if __name__ == '__main__':
    for item in lst:
        is_decimal = True
        if type(item) is not str :
            continue
        else:
            print(item)
        for char in item:
            if char not in '0123456789':
                is_decimal = False
                break



