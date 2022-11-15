def cube(n):
    return n**3
 
# Taking list as iterator
evennum = [2,4,6,8]
res = map(cube,evennum)
print(list(res))