import time
import numpy as np
from numba import njit, prange
from spins2 import functions

def iteration3(latt, X_s, Y_s, J0, J1, Ja, J_1, J_a, val, nequilibrium, nworks):
    t0 = time.time()
    Nw = np.zeros((nworks, 2, 8))
    Ew = np.zeros(nworks)
    for i in range(nequilibrium):
        randvals = np.random.rand(2, 8, Y_s, X_s)
        E0 = update3(latt, randvals, X_s, Y_s, J0, J1, Ja, J_1, J_a, val)
    for i in range(nworks):
        randvals = np.random.rand(2, 8, Y_s, X_s)
        E0 = update3(latt, randvals, X_s, Y_s, J0, J1, Ja, J_1, J_a, val)
        Ew[i] = E0 / 2
        Nw[i,0] = functions.Average(latt[0,0]), functions.Average(latt[0,1]), functions.Average(latt[0,2]), functions.Average(latt[0,3]),\
                  functions.Average(latt[0,4]), functions.Average(latt[0,5]), functions.Average(latt[0,6]), functions.Average(latt[0,7])
        Nw[i,1] = functions.Average(latt[1,0]), functions.Average(latt[1,1]), functions.Average(latt[1,2]), functions.Average(latt[1,3]),\
                  functions.Average(latt[1,4]), functions.Average(latt[1,5]), functions.Average(latt[1,6]), functions.Average(latt[1,7])
    t = time.time() - t0
    return t, Nw, Ew

@njit(cache=True, parallel=True)
def update3(latt, randvals, X_s, Y_s, J0, J1, Ja, J_1, J_a, val):
    nn_sum = 0
    for f in prange(8):
        for g in range(2):
            for j in range(Y_s):
                for i in range(X_s):
                    ipp  = (i + 1) if (i + 1) < X_s else 0
                    inn  = (i - 1) if (i - 1) > -1  else (X_s - 1)
                    jpp  = (j + 1) if (j + 1) < Y_s else 0
                    jnn  = (j - 1) if (j - 1) > -1  else (Y_s - 1)
                    go   = 1  - g
                    f_4  = f  % 4
                    f_2  = f  % 2

                    if f_4 < 2:
                        f0 = f - 2
                        if f0 < 0: f0 = f0 + 8
                        x__a = i
                        x__b = i if f_2 == 1 else inn
                    else:
                        f0 = f - 1
                        if f0 % 2 == 0: f0 = f0 - 2
                        x__a = i if f_2 == 0 else ipp
                        x__b = i

                    f1 = f0 + 4 if f0      < 4 else f0 - 4
                    f2 = f1 - 1 if f1 % 2 == 1 else f1 + 1
                    f3 = f0 - 1 if f0 % 2 == 1 else f0 + 1

                    if f_2 == 0:
                        fp   = f + 1
                        x_ap = i
                        x_an = inn
                    else:
                        fp   = f - 1
                        x_ap = ipp
                        x_an = i

                    if f < 2:
                        y__a = jnn
                        y__b = j
                    elif f > 5:
                        y__a = j
                        y__b = jpp
                    else:
                        y__a = j
                        y__b = j

                    if g == 0:
                        x_0  = x_an
                        fo2  = f2
                        y__0 = y__b
                        x__0 = x__b
                        foa  = f3
                        y_1  = y__a
                        x_1  = x__b
                        fob  = f1
                        y_b  = y__b
                        x_b  = x__a
                        foc  = fo2 - 1 if fo2 % 2 == 1 else fo2 + 1
                        x_c  = inn
                    else:
                        x_0  = x_ap
                        fo2  = f0
                        y__0 = y__a
                        x__0 = x__a
                        foa  = f1
                        y_1  = y__b
                        x_1  = x__a
                        fob  = f3
                        y_b  = y__a
                        x_b  = x__b
                        foc  = fo2 + 1 if fo2 % 2 == 0 else fo2 - 1
                        x_c  = ipp

                    energy  = ( -J0 * ( latt[go,f  ,j   ,i   ] + latt[go,fp ,j   ,x_0 ] +
                                        latt[go,fo2,y__0,x__0] ) -
                                 J1 *   latt[go,foa,y_1 ,x_1 ] -
                                 J_1* ( latt[go,fob,y_b ,x_b ] + latt[go,foc,y__0,x_c ] ) -
                                 Ja * ( latt[g ,f0 ,y__a,x__a] + latt[g ,f3 ,y__a,x__b] +
                                        latt[g ,f1 ,y__b,x__a] + latt[g ,f2 ,y__b,x__b] ) -
                                 J_a* ( latt[g ,fp ,j   ,x_ap] + latt[g ,fp ,j   ,x_an] )
                              )
                    energy *= latt[g,f,j,i]

                    if val == 0:
                        if energy >  0: latt[g,f,j,i] *= -1
                    else:
                        if energy >= 0 or randvals[g,f,j,i] < np.exp( 2.0 * val * energy ): latt[g,f,j,i] *= -1

                    nn_sum += energy
    return nn_sum
