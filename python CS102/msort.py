def merge(xs,ys):
    if not xs or not ys:
        return xs + ys
    else:
        if (xs[0] < ys[0]):
            return [xs[0]] + merge(xs[1::],ys)
        else:
            return [ys[0]] + merge(xs,ys[1::])
        
def split (xs):
    return (xs[0:len(xs) // 2:] , xs[len(xs) // 2: len(xs):])

def msort (xs):
    if (len(xs) < 2):
        return xs
    else:
        ys , zs = split(xs)
        ys = msort(ys)
        zs = msort(zs)
        return merge(ys , zs)

