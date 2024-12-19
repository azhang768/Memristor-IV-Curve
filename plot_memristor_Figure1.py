import numpy as np
import matplotlib.pyplot as plt
omega_values = [5, 4, 3, 2, 1] # Different angular frequencies
bound = 1e-4
for omega in omega_values:
    voltage = [-1,-1,0,1,1,-1]
    slope = 1/(omega+1)
    current = [-bound,-bound*slope,0,bound*slope,bound,-bound]
    plt.plot(voltage, current, label=f'Omega={omega}')
plt.title("Memristor I-V Pinched Hysteresis Loop")
plt.xlabel('Voltage (V)')
plt.ylabel('Current (A)')
plt.legend()
plt.grid(linestyle='--')
plt.ticklabel_format(axis='both', style='sci', scilimits=(0,0))
plt.show()
