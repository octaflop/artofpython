# encoding: utf-8

import turtle as t

rotation = 60 * 1.3
 
def branch(length=100):
    """ 
    paints a branch of a tree with 2 smaller branches, like an Y
    """
    # escape the function when done (we're iterating down)
    if length < 10:
       return       
    # paint the thick branch of the tree
    t.fd(length)        
    # rotate left for smaller "fork" branch
    t.left(rotation)          
    # create a smaller branch with 2/3 the lenght of the parent branch
    branch(length * 0.6)     
    # rotate right for smaller "fork" branch 
    t.right(rotation * 2)         
    # create second smaller branch
    branch(length * 0.6)     
    # rotate back to original heading 
    t.left(rotation)          
    t.fd(-length)       
    return              
 
# calling the function the first time
branch(350) # create a tree, the first branch has a length of 200 pixel
