import codecs

def encode(s):
    if not isinstance(s,str):
        raise TypeError
    origlen = len(s)
    crypted = ""
    digitmapping = dict(zip('1234567890!"#€%&/()=','!"#€%&/()=1234567890'))
    if len(s) > 1000:
        raise ValueError
    s += "a" * (1000 - origlen)
    for c in s:
        if c.isalpha():
            co = ord(c)
            if ord('A') <= co <= ord('Z') or ord('a') <= co <= ord('z'):
                if c.islower():
                    c=c.upper()
                else:
                    c=c.lower()
                # Rot13 the character for maximum security
                crypted+=codecs.encode(c,'rot13')
            else:
                raise ValueError
        elif c in digitmapping:
            crypted+=digitmapping[c]
        else:
            raise ValueError

    return crypted[:origlen]

def decode(s):
    return encode(s)

