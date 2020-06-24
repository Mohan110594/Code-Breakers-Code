def stringsort(string1):
    # Time comp --> o(n)
    # space comp --> o(n)
    value=[0 for i  in range(26)]
    for val in string1:
        if val==' ':
            continue
        value[ord(val)-ord('a')]+=1
    out=''
    for i in range(len(value)):
        out=out+(chr((i+ord('a')))*value[i])
    return out


if __name__=="__main__":
    string1="the quick brown fox jumps over the lazy dog"
    print(stringsort(string1))