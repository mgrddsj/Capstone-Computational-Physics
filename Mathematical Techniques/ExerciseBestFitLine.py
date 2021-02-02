#%% 1
import BestFitLine
import numpy as np

W_list = [70, 75, 77, 80, 82, 84, 87, 90]
A_list = [2.1, 2.12, 2.15, 2.20, 2.22, 2.23, 2.26, 2.30]
Wlog_list = list(map(lambda w: np.log(w), W_list))
Alog_list = list(map(lambda a: np.log(a), A_list))

print(BestFitLine.getBestFit(Wlog_list, Alog_list))

#%% 2
import BestFitLine
import numpy as np
import matplotlib.pyplot as plt

mass_list = [400, 70, 45, 2, 0.3, 0.16]
metabolism_list = [270, 82, 50, 4.8, 1.45, 0.97]

masslog_list = list(map(lambda a: np.log(a), mass_list))
mlog_list = list(map(lambda m: np.log(m), metabolism_list))

plt.plot(mass_list, metabolism_list, '.')
plt.subplots(1)
plt.plot(masslog_list, mlog_list, '.')

print(BestFitLine.getBestFit(mass_list, metabolism_list))