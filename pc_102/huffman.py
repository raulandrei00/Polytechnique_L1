class Node:
    def __init__(self, value, left = None, right = None):
        self.value = value
        self.left  = left
        self.right = right
    

import heapq
class PQueue:
    def __init__(self):
        '''initialize an empty priority queue'''
        self.pqueue = []
        self.uid = 0

    def __len__(self):
        '''return the number of elements in the queue'''
        return len(self.pqueue)
        
    def put(self, value, weight):
        '''add a value to the queue with associated weight'''
        heapq.heappush(self.pqueue, (weight, self.uid, value))
        self.uid += 1

    def get(self):
        '''remove and return the value with lowest associated weight'''
        w, _, v = heapq.heappop(self.pqueue)
        return (v, w)

def huffman_stats(s):
    f = dict()
    for c in s:
        try:
            f[c] += 1
        except:
            f[c] = 1
    
    for key in f:
        f[key] /= len(s)

    return f

def huffman_tree(d):
    q = PQueue()
    for key in d:
        q.put(Node(key), d[key])

    while (len(q) > 1):
        n1, w1 = q.get()
        n2, w2 = q.get()
        new_node = Node(None, n1, n2)
        q.put(new_node, w1+w2)
    
    return q.get()[0]

def huffman_codes(tree):
    huff_code = dict()
    def dfs (node, crt_string = ""):
        if node.value is not None and node.value != 0:
            huff_code[node.value] = crt_string
        if node.left is not None:
            dfs(node.left , crt_string+"0")
        if node.right is not None:
            dfs(node.right , crt_string+"1")
    dfs(tree)
    return huff_code

def huffman_encode(tree, s):
    huff_code = huffman_codes(tree)
    ret = ""
    for c in s:
        ret += huff_code[c]
    
    return ret
            
def huffman_decode(tree, s):


    huff_code = huffman_codes(tree)
    ret = ""
    crt_node = tree

    for b in s:
        if b == '0':
            crt_node = crt_node.left
        else:
            crt_node = crt_node.right
        if crt_node.value is not None:
            ret += crt_node.value
            crt_node = tree
    
    return ret

def huffman_compress(s):
    stats = huffman_stats(s)
    tree = huffman_tree(stats)
    hs = huffman_encode(tree , s)

    return tree , hs , 8 * len(s) / len(hs)

def bitstring_to_uint16(bs):

    bs = [int(b) for b in bs]
    
    x = 0
    for b in bs:
        x = (x << 1) + b
    
    return x

def uint16_to_bitstring(x):
    ret = ""
    while (x != 0):
        if x % 2 == 1:
            ret = '1' + ret
        else:
            ret = '0' + ret
        x //= 2
    while (len(ret) < 8): ret = '0' + ret
    # ret.reverse()
    return ret

def huffman_bcodes(tree):
    hcode = huffman_codes(tree)
    for key in hcode:
        hcode[key] = len(hcode[key]) , bitstring_to_uint16(hcode[key])
    
    return hcode

def huffman_bencode(tree, s):
    ret = bytearray([])
    bs = huffman_encode(tree , s)
    while len(bs) % 8:
        bs += '0'

    for i in range(0, len(bs), 8):
        ret.append(bitstring_to_uint16(bs[i:i+8])) #using as uint8

    return bytes(ret)

def string_to_bytes (bs):
    ret = bytearray([])
    for i in range(0, len(bs), 8):
        
        ret.append(bitstring_to_uint16(bs[i:i+8])) #using as uint8

    return bytes(ret)

def huffman_bdecode(tree, bs, n):
    bitstring = ""

    if (len(bs) == 0):
        if n == 0:
            return ""
        else:
            return tree.value * n

    for xx in bs:
        # print(xx)
        bitstring += uint16_to_bitstring(int(xx))
        # print(uint16_to_bitstring(int(xx)))
    
    return huffman_decode(tree , bitstring)[0:n]

def huffman_bencode_tree(tree):
    ret = dfs_encode(tree)

    dfs_encode(tree)
    while (len(ret) % 8):
        ret += '0'
    
    return string_to_bytes(ret)

def dfs_encode (node):
    ret = ""
    if node.value is None:
        ret += '0'
        ret += dfs_encode(node.left)
        ret += dfs_encode(node.right)
    else:
        ret += "1"
        ret += uint16_to_bitstring(ord(node.value))
    return ret

def huffman_bcompress(s):
    ret = int.to_bytes(len(s) , 4 , "little")
    tree = huffman_tree(huffman_stats(s))
    ret += huffman_bencode_tree(tree)
    ret += huffman_bencode(tree , s)

    return ret


def huffman_buncompress(s):
    n = int.from_bytes(s[:4] , "little")
    

print(huffman_bcompress("aksudyvb"))
# print(huffman_bdecode(Node(None, Node(None, Node(None, Node('i', None, None), Node(None, Node('m', None, None), Node('o', None, None))), Node(None, Node('e', None, None), Node(None, Node(None, Node(None, Node(None, Node('f', None, None), Node(None, Node('E', None, None), Node('g', None, None))), Node('l', None, None)), Node('p', None, None)), Node('n', None, None)))), Node(None, Node(None, Node(None, Node('r', None, None), Node('u', None, None)), Node(' ', None, None)), Node(None, Node(None, Node(None, Node('c', None, None), Node(None, Node(None, Node(None, Node('.', None, None), Node(None, Node('b', None, None), Node(',', None, None))), Node('h', None, None)), Node(None, Node('q', None, None), Node(None, Node('v', None, None), Node('x', None, None))))), Node('a', None, None)), Node(None, Node('t', None, None), Node(None, Node('s', None, None), Node('d', None, None)))))), b'bdusz\x84\xf8\x8f\xf7Iu\xc4\xb4\x7f{z\xe9.\xa1\xf0>?/\xd4\xb5\x8d\xf6\xb7`oL]df\x9d\xb9\xc6\xcc\xb7\xb7\x95Y\xea0;x\x1b\xd4\'\xc4\x7f\xa2&\x15grG\x12U\xc7\x85B|G\xfb\x83"?\x9d\xc1\xbf\x96i\xde\xb9\xa4]pVz\xec\xf2\xb0\x9b\x0b*\x7f\xa8\x1dV}B|G\xfb\xe9~\xa6\xc1\x80\xc0\xda\xba\xe0\xdf\xcb\x1c\xbab\xb7`oLd\xe8{\t\xb0\xb2\xa7\xfa\x81\xd7\\\x15\xc1\x91\x1f\xce\xafy]\x9eW\x914\xe2\x87\xc0\xf8\xfc\xbf]\xfd\xd2][\x06>\x9f\xaa\x9a\xb6\xe7\'\x1aW4\x8fW\x1e\x16\x13aeO\xf5\x03\xabv\x06\xf4\xc5\xfa\xf2\x89~\xb8\x0c\xb3%W\xbc\xb2\x00', 368))
# print(huffman_bencode_tree(Node(None, Node(None, Node(None, Node('i', None, None), Node(None, Node('m', None, None), Node('o', None, None))), Node(None, Node('e', None, None), Node(None, Node(None, Node(None, Node(None, Node('f', None, None), Node(None, Node('E', None, None), Node('g', None, None))), Node('l', None, None)), Node('p', None, None)), Node('n', None, None)))), Node(None, Node(None, Node(None, Node('r', None, None), Node('u', None, None)), Node(' ', None, None)), Node(None, Node(None, Node(None, Node('c', None, None), Node(None, Node(None, Node(None, Node('.', None, None), Node(None, Node('b', None, None), Node(',', None, None))), Node('h', None, None)), Node(None, Node('q', None, None), Node(None, Node('v', None, None), Node('x', None, None))))), Node('a', None, None)), Node(None, Node('t', None, None), Node(None, Node('s', None, None), Node('d', None, None))))))))
# print(bitstring_to_uint16("0010100"))
# s = 'abc'
# mb = bytearray([97, 98, 99])
# print(bytes(mb))
# print(s.encode('ascii'))
