import numpy as np
import matplotlib.pyplot as plt


def EulerMethod(f, t0, tf, y0, h):
    t = np.arange(t0, tf + h, h)
    y = np.zeros((len(t), len(y0)))
    y[0] = y0

    for i in range(len(t) - 1):
        y[i + 1] = y[i] + h * f(t[i], y[i])

    return t, y


def ResourceUtilization(t, y):
    return y[:, 0]


def ResourceAllocation(t, y):
    return y[:, 1]


def ArrivalRate(t):
    return np.cos(t)


def DepartureRate(t):
    return np.sin(t)


def ode_system(t, y):
    A = ArrivalRate(t)
    D = DepartureRate(t)
    dU_dt = A - D
    dR_dt = A - D
    return np.array([dU_dt, dR_dt])


timeInit = 0
timeFinal = 100
InitVals = np.array([0, 100])
h = 0.01

t, y = EulerMethod(ode_system, timeInit, timeFinal, InitVals, h)

utilization = ResourceUtilization(t, y)
allocation = ResourceAllocation(t, y)

plt.plot(t, utilization, label='Resource Utilization')
plt.plot(t, allocation, label='Resource Allocation')
plt.xlabel('Time')
plt.ylabel('Value')
plt.title('Resource Utilization and Allocation over Time')
plt.legend()
plt.grid(True)
plt.show()
