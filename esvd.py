import numpy as np
import pandas as pd


def svd(a):
    t=a.t
    X=t.dot(a)
    ev,V= np.linalg.eig(X)
    ev= np.absolute(ev)
    ev= np.array(sorted(ev,reverse=True))
    S= np.diag(ev ** 0.5)
    U=A.dot(V.dot(np.linalg.pinv(S)))
    return U,S,V
df= pd.read_excel (r'C:\Users\DELL\Downloads\eSVD.xlsx')
A=df.as_matrix(columns=None)
writer=pd.ExcelWriter('esvd1.xlsx',engine='xlsxwriter')
for i in range(0,A.length()):
    u,s,v = svd(A[i])
    v1=v[1:100]
    y=A[i].dot(v1.dot(v1.t))
    z=pd.DataFrame(y)
    z.to_excel(writer,sheet_name='Sheet1',header=False,index=False)
writer.save()