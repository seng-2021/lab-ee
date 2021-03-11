import codecs
def encode(s):
    if not in isinstance(s,str):        
        raise TypeError
    origlen = len(s)
    crypted = ""
    digitmapping = dict(zip('1234567890!"#€%&/()=','!"#€%&/()=1234567890'))
    s = s.ljust(1000,"v")
    if len(s) > 1000:
        raise ValueError
    for c in s:
        if c.isalpha():
            if c.isupper():
                c=c.lower()
            elif c.islower():
                c=c.upper()
            # Rot13 the character for maximum security
            crypted+=codecs.encode(c,'rot13')
        elif c in digitmapping:
          crypted+=digitmapping[c]
    return crypted[:origlen]
def decode(s):
    return encode(s)
