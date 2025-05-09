def uint16_to_bitstring(x):
    ret = []
    while (x != 0):
        if x % 2 == 1:
            ret.append(1)
        else:
            ret.append(0)
        x //= 2
    while (len(ret) < 16): ret.append(0)
    ret.reverse()
    return ret

def bitstring_to_uint16(bs):
    x = 0
    for b in bs:
        x = (x << 1) + b
    return x

def mod_pow2(x , k):
    return x & ((1 << k) - 1)

def is_pow2 (x):
    return x != 0 and ((x & (x - 1)) == 0)

def set_mask(w, m):
    
    
    return (w | m)

def toggle_mask(w, m):
    
    
    return (w ^ m)

def clear_mask(w, m):
    
    return (w & (~m))
