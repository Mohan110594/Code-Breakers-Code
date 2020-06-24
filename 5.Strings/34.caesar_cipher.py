#o(n)
#o(1)
def caesarCipher(s, k):
    if k==0:
        return s
    out=''
    for val in s:
        if val.isupper():
            index=(ord(val)-ord('A')+k)%26
            out=out+chr(index+ord('A'))
        elif val.islower():
            index=(ord(val)-ord('a')+k)%26
            out=out+chr(index+ord('a'))
        else:
            out=out+val
            continue
        
    return out