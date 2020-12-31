def plotCurvaNivel(x_inicial=(), x_final=(), y_inicial=(), y_final=(), n=()):
    from numpy import sin, sqrt
    import numpy as np
    import matplotlib.pyplot as plt


    xlist = np.linspace(x_inicial, x_final, n)
    ylist = np.linspace(y_inicial, y_final, n)
    X, Y = np.meshgrid(xlist, ylist)
    Z = 999.5 - ((sin(sqrt(X**2 + Y**2)))**2 - 0.5) / (1 + 0.001 * (X**2 + Y**2))**2 # F6 elevada

    plt.figure()
    cp = plt.contourf(X, Y, Z)


    return cp


# import matplotlib.pyplot as plt
# cp = plotCurvaNivel(x_inicial=(-5), x_final=(5), y_inicial=(-5), y_final=(5), n=(1000))
# plt.colorbar(cp)
# plt.title('Curvas de nível da função F6(x, y)')
# plt.xlabel('x')
# plt.ylabel('y')
# plt.show()