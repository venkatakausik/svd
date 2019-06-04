import pandas as pa
import numpy as np

def SVd(A):
    t = A.T
    # X= np.multiply(t,A); -> This perform element-wise multiplication
    X = t.dot(A)
    v, V = np.linalg.eig(X)
    v = np.absolute(v)
    v = np.array(sorted(v, reverse=True))
    S = np.diag(v ** 0.5)
    U = A.dot(V.dot(np.linalg.pinv(S)))
    return U, S, V


df = pa.read_csv(r"C:\Users\DELL\Downloads\air.csv")
f = np.array(df.as_matrix())
print(f.shape)
j = np.size(f, 0)
i = 0
a = f[i:i + 1, :]
m = 100
n = len(a[0])+ 1 - m
arr =np.array([[0 for b in range(n)] for i in range(m)])
for i in range(m):
    arr[i]=a[:,i:i+n]
print(arr.shape)
print(arr)
U1, S1, V1 = SVd(arr)
v1 = V1[:, 0:1]
d2 = pa.DataFrame(v1.T)
for i in range(1, j):
    a = f[i:i + 1, :]
    m = 100
    n = len(a[0]) + m - 1
    arr = np.array([[0 for j in range(n)] for i in range(m)])
    for k in range(m):
        arr = a[:, k:k + n]
    U1, S1, V1 = SVd(arr)
    v1 = V1[:, 0:1]
    d3 = pa.DataFrame(v1.T)
    d2 = pa.concat([d2, d3])
d2.to_excel(r"C:\Users\DELL\Downloads\testv.xlsx")
d1 = pa.DataFrame(U1)
