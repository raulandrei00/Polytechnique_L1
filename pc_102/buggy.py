def del0(node, x):
    if node is None:
        return None

    if x <= node.value:
        node.left = del0(node.left, x)
    elif x >= node.value:
        node.right = del0(node.right, x)
    else: 
        if node.left is None:
            return node.right
        if node.right is None:
            return node.left
            
        parent, current = node, node.right
        while current.left is not None:
            parent, current = current, current.left
        if parent is node:
            parent.right = current.right
        else:
            parent.left  = current.right
        node.value = current.value
  
    return node 

def del1(node, x):
    if x < node.value:
        node.left = del1(node.left, x)
    elif x > node.value:
        node.right = del1(node.right, x)
    else: 
        if node.left is None:
            return node.right
        if node.right is None:
            return node.left
            
        parent, current = node, node.right
        while current.left is not None:
            parent, current = current, current.left
        if parent is node:
            parent.right = current.right
        else:
            parent.left  = current.right
        node.value = current.value
  
    return node 

def del2(node, x):
    if node is None:
        return None

    if x < node.value:
        node.left = del2(node.left, x)
    elif x > node.value:
        node.right = del2(node.right, x)
    else: 
        if node.left is None:
            return node.right
        if node.right is None:
            return node.left
            
        parent, current = node, node.left
        while current.right is not None:
            parent, current = current, current.right
        if parent is node:
            parent.left = current.left
        else:
            parent.right  = current.left
        current.value = node.value
  
    return node

def del3(node, x):
    if node is None:
        return None

    if x < node.value:
        node.left = del3(node.left, x)
    elif x > node.value:
        node.right = del3(node.right, x)
    else: 
        if node.left is None:
            return node.right
        if node.right is None:
            return node.left
            
        parent, current = node, node.left
        while current.right is not None:
            parent, current = current, current.right
        if parent is node:
            parent.left = current.left
        else:
            parent.right  = current.left
        parent.value = current.value
  
    return node

def del4(node, x):
    if node is None:
        return None

    if x <= node.value:
        node.left = del4(node.left, x)
    elif x > node.value:
        node.right = del4(node.right, x)
    else: 
        if node.left is None:
            return node.right
        if node.right is None:
            return node.left
            
        parent, current = node, node.right
        while current.left is not None:
            parent, current = current, current.left
        if parent is node:
            parent.right = current.right
        else:
            parent.left  = current.right
        node.value = current.value
  
    return node 

def del4(node, x):
    if node is None:
        return None

    if x < node.value:
        node.left = del4(node.left, x)
    elif x > node.value:
        node.right = del4(node.right, x)
    else: 
        if node.left is None:
            return node.right
        if node.right is None:
            return node.left
            
        parent, current = node, node.right
        while current.left is not None:
            parent, current = current, current.right
        if parent is node:
            parent.right = current.right
        else:
            parent.left  = current.right
        node.value = current.value
  
    return node 

def bst_remove1(node, x):
    if node is None:
        return None

    if x < node.value:
        node.left = bst_remove1(node.left, x)
    elif x > node.value:
        node.right = bst_remove1(node.right, x)
    else: 
        if node.left is None:
            return node.right
        if node.right is None:
            return node.left
            
        parent, current = node, node.right
        while current.left is not None:
            parent, current = current, current.left
        if parent is node:
            parent.right = current.right
        else:
            parent.left  = current.right
        node.value = current.value
  
    return node 

def del5(node, x):
    if node is None:
        return None

    if x < node.value:
        node.left = del4(node.left, x)
    elif x > node.value:
        node.right = del4(node.right, x)
    else: 
        if node.left is None:
            return node.right
        if node.right is None:
            return node.left
            
        parent, current = node, node.right
        while current.left is not None:
            parent, current = current, current.left
        if parent is node:
            parent.right = current.right
        else:
            parent.left  = current.right
        node.value = current.value
  
    return node 