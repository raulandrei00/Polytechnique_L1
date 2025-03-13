

def partition (l ,b, e):

    #! b <= e
    
    pivot = l[e]
    p = b
    i = b

    #! X := forall k in [b,p], l[k] <= l[p]
    
    while i < e :
        #! P(l[i] , l[p])

        if l[i] < pivot :
            l[i] , l[p] = l[p] , l[i]
            #! P(l[p] , l[i])
            
            #! p = n
            p = p + 1
            #! p = n+1
        else :
            pass
        #! (l[i] < pivot AND P(l[p] , l[i]) AND p = n+1) OR (l[i] >= pivot)
        #! => X
        #! l[i] >= pivot
        #! P(i)
        i = i + 1
        #! P(i-1)
    #! P(l[e] , l[p])
    l[e] , l[p] = l[p] , l[e]
    #! P(l[p] , l[e])
    return p