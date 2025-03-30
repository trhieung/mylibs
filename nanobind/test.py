import object_ownership as ob
from time import time

lst = list(range(100000, 0, -1))
c_lst = ob.VectorInt(lst)

st = time()
ob.sort(c_lst)
print(time() - st)