import codecs

def encode(s):
    if not isinstance(s,str):
        raise TypeError
        
    origlen = len(s)
    crypted = ""
   
    digitmapping = dict(zip('1234567890!"#€%&/()=','!"#€%&/()=1234567890'))
    if len(s) > 1000:
        raise ValueError
        
    s = s.ljust(1000, "o")
    error = ["å","ä","ö"]
    
    for c in s:
        if c in error:
            raise ValueError
        elif c.isalpha():
            if c.islower():
                c=c.upper()
            elif c.isupper():
                c=c.lower()

            crypted+=codecs.encode(c,'rot13')
        elif c in digitmapping:
            crypted+=digitmapping[c]
        else:
            raise ValueError
    
    return crypted[:origlen]

def decode(s):
    return encode(s)
