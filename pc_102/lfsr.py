def bitstring_to_uint16(bs):
    x = 0
    for b in bs:
        x = (x << 1) + b
    return x

def tap_uint16(x, i):
    if (x & (1 << i)):
        return 1
    else:
        return 0
    
def polytap_uint16(x , I):
    ret = 0
    for i in I:
        ret ^= tap_uint16(x , i)

    return ret

def lfsr_uint16(x , I):
    # bits = [0] * 16
    # bits[0] = (polytap_uint16(x , I))
    

    
    ret = (polytap_uint16(x , I) << 15) + (x >> 1) 
    return ret

