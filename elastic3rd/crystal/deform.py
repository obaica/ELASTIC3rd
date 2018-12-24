#/usr/bin/python
#

import numpy as np

def deform_mode(strain, flag):
    #ref:PHYSICAL REVIEW B 75, 094105 (2007)
    #TODO: for arbitrary symmetry
    #      ref: Fausto G. Fumi, Physical Review, 83(1951), 1274-1275
    #           Fausto G. Fumi, Physical Review, 86(1952), 561-561
    strain = float(strain)
    if flag == 1:
        STRAIN = np.array([strain, 0, 0, 0, 0, 0])
    elif flag == 2:
        STRAIN = np.array([strain, strain, 0, 0, 0, 0])
    elif flag == 3:
        STRAIN = np.array([strain, strain, strain, 0, 0, 0])
    elif flag == 4:
        STRAIN = np.array([strain, 0, 0, 2. * strain, 0, 0])
    elif flag == 5:
        STRAIN = np.array([strain, 0, 0, 0, 0, 2. * strain])
    elif flag == 6:
        STRAIN = np.array([0, 0, 0, 2. * strain, 2. * strain, 2. * strain])
    elif flag == 7:
        STRAIN = np.array([0, strain, 0, 0, 0, 0])
    elif flag == 8:
        STRAIN = np.array([0, 0, strain, 0, 0, 0])
    elif flag == 9:
        STRAIN = np.array([0, strain, strain, 0, 0, 0])
    elif flag == 10:
        STRAIN = np.array([0, 0, 0, 2. * strain, 0, 0])
    elif flag == 11:
        STRAIN = np.array([0, 0, strain, 0, 0, 2. * strain])
    elif flag == 12:
        STRAIN = np.array([0, strain, 0, 2. * strain, 0, 0])
    elif flag == 13:
        STRAIN = np.array([0, strain, 0, 0, 2. * strain, 0])
    elif flag == 14:
        STRAIN = np.array([0, 0, strain, 0, 2. * strain, 0])
    elif flag == 15:
        STRAIN = np.array([strain, 0, strain, 2. * strain, 0, 0])
    elif flag == 16:
        STRAIN = np.array([strain, strain, 0, 0, 2. * strain, 0])

    return STRAIN

def vec2matrix(StrainVerctor):
    (e1, e2, e3, e4, e5, e6) = StrainVerctor
    e4 = e4/2.0
    e5 = e5/2.0
    e6 = e6/2.0
    StrainMatrix = np.array([[e1, e6, e5], [e6, e2, e4], [e5, e4, e3]])
    return StrainMatrix

def matrix2vec(StrainMatrix):
    if not is_strain_matrix(StrainMatrix):
        StrainVerctor = np.array([0, 0, 0, 0, 0, 0])
        print("Warning: The format of input strain matrix is not correct. And it is set as zeros")
        return StrainVerctor
    e1 = StrainMatrix[0][0]
    e2 = StrainMatrix[1][1]
    e3 = StrainMatrix[2][2]
    e4 = 2. * StrainMatrix[1][2]
    e5 = 2. * StrainMatrix[0][2]
    e6 = 2. * StrainMatrix[0][1]
    StrainVerctor = np.array([e1, e2, e3, e4, e5, e6])

def is_strain_matrix(StrainMatrix):
    (m, n) = StrainMatrix.shape
    if not (m == 3 and n == 3):
        print("Error: The size of input strain matrix is not 3 by 3!")
        return False
    else:
        for i in xrange(1, 3):
            for j in xrange(0, i):
                if StrainMatrix[i][j] != StrainMatrix[j][i]:
                    print("Warning: The input strain matrix is not symmtry!")
                    return False
    return True

def strain2deformgrad(StrainMatrix):
    Y = 2 * StrainMatrix + 1 * np.eye(3)
    print Y
    (D, V) = eigv(Y)
    VT = V.T
    DeformGrad = V.dot(np.sqrt(D)).dot(VT)
    return DeformGrad

def eigv(a):
    (D, V) = np.linalg.eigh(a)
    #print D
    #print V
    Dv = np.zeros((3, 3))
    for i in range(0, 3):
        Dv[i, i] = D[i]
    return (Dv, V)

'''
strain = 0.05
flag = 6
StrainMatrix = vec2matrix(deform_mode(strain, flag))
print StrainMatrix + np.eye(3)
DeformGrad = strain2deformgrad(StrainMatrix)
print DeformGrad
DT = DeformGrad.T
print DT.dot(DeformGrad)
'''

#For test
'''
a = deform_mode(0.1, 2)
b = vec2matrix(a)
#b[1][0] = 1.
if is_strain_matrix(b):
    print b
'''
