import numpy as np
import matplotlib.pyplot as plt

R_on = 100
R_off = 16000
D = 1e-6
mu = 1e-8
p = 2
V_max = 1
time = np.linspace(0, 20, 10000)
Omega = [.46,.49,.52,.55,.58]

for o in Omega:
    I = []
    w = 0.5 * D
    V = V_max * np.sin(o * time)
    for v in V:
        R = R_on * w / D + R_off * (1 - w / D)
        i = v / R
        I.append(i)

        f_w = 1 - (2 * w / D - 1) ** (2 * p)
        dw = mu * R_on * i * f_w
        w += dw

        if w > D:
            w = D
        elif w < 0:
            w = 0

    plt.plot(V, I, label=f"Omega={o} rad/s")

plt.xlabel("Voltage (V)")
plt.ylabel("Current (A)")
plt.title("Pinched hysteresis loop of the memristor")
plt.grid(linestyle="--")
plt.legend()
plt.ticklabel_format(axis="both", style="sci", scilimits=(0,0))
plt.xticks(np.arange(-1, 1.2, .5))
plt.show()
