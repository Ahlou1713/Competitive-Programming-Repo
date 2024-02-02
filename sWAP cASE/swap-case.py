def swap_case(s):
    s_s = ''
    for i in s:
        if(i.isupper()):
            s_s += i.lower()
        else:
            s_s += i.upper()
            
    return s_s

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)