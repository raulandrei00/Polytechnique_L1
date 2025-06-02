def matrix_to_adjlist(nodes, MG):
    n = len(nodes)
    adj_list = {nod : [] for nod in nodes}
    for i in range(n):
        for j in range(n):
            if MG[i][j]:
                adj_list[nodes[i]].append(nodes[j])

    return adj_list

def is_symmetric (AG):
    for nod in AG:
        for to in AG[nod]:
            if nod not in AG[to]: 
                return False
    return True

def revert_edges (AG):
    rev_adj_list = {nod : [] for nod in AG}
    for nod in AG:
        for to in AG[nod]:
            rev_adj_list[to].append(nod)
    return rev_adj_list

