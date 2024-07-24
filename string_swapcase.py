def swap_case(s):
    l =[]
    for i in s:

        if i == i.lower():
            l.append(i.upper())
        elif i == i.upper():
            l.append(i.lower())
        else :
            l.append(i)
    return ''.join(l)    

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)