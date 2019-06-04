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
j = np.size(f, 0)
i = 0
a = f[i:i + 1, :]
#print(a.shape)

p2=pa.DataFrame()


m = 100
n = len(a[0])- m + 1
arr = np.array([[0 for j in range(n)] for h in range(m)])
for i in range(m):
    #arr = np.array([[0 for g in range(n)]])
    arr[i]=a[:,i:i+n]
p1=pa.DataFrame(arr)
p2=pa.concat([p2,p1])
#arr = np.array(p2)
U1, S1, V1 = SVd(arr)
#print(V1.shape)
v1 = V1[:, 1:50]
y=arr.dot(v1.dot(v1.T))
y = y[:, 0:1]
d2 = pa.DataFrame(v1.T)
p2 = pa.DataFrame()
d2 = pa.DataFrame()
for i in range(1, j):
    a = f[i:i + 1, :]
    m = 100
    n = len(a[0]) -m +1
    arr = np.array([[0 for j in range(n)] for h in range(m)])
    for k in range(m):

        #print(arr.shape)
        arr[k] = a[:, k:k + n]
    p1 = pa.DataFrame(arr)
    p2 = pa.concat([p2, p1])
    #arr=np.array(p2)
    #print(arr.shape)
    U1, S1, V1 = SVd(arr[i:i + 1, :])
    #print(V1.shape)
    v1=V1[:,1:50]
    #print(v1.shape)
    y=arr.dot(v1.dot(v1.T))
    y = y[:, 0:1]
    d3 = pa.DataFrame(y.T)

    d2 = pa.concat([d2, d3])
d2.to_excel(r"C:\Users\DELL\Downloads\testehsvd.xlsx")
