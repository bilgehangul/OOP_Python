import math
R = 3.15
TS_out = float(input("Ts_out:"))
TS_in = float(input("Ts_in:"))
p = (TS_out - 30)/(120-30)
delta_T = ((120 - TS_in) - (TS_out - 30)) / math.log((120 - TS_in)/(TS_out - 30))

F = (math.sqrt(R**2+1) * math.log((1-p)/(1-p*R))) / ((R - 1) * math.log((2 - p*(R+1 -math.sqrt(R**2+1)))/(2 - p*(R+1 + math.sqrt(R**2+1)))))

Q1 = 1815.33 * 295.76 * delta_T * F
Q2 = 180*4200*(TS_in - 30)
Q3 = 120*2000 *(120 - TS_out)
