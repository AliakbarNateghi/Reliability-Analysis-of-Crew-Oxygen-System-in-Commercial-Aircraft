$ import math, random
$
$ # Component reliabilities at t = 50,000 hr
$ R_G_single = math.exp(- (50000.0/40000.0)**1.5)   # ~0.2472
$ R_Gpar = 1 - (1-R_G_single)**2                    # ~0.4333
$ R_valve = math.exp(-1e-6 * 50000.0)               # ~0.9512294
$ R_dist  = math.exp(-1e-7 * 50000.0)               # ~0.9950125
$ R_sensor = math.exp(-5e-7 * 50000.0)              # ~0.9753099
$ R_Spar = 1 - (1-R_sensor)**2                      # ~0.9993904
$ R_mask = math.exp(-1e-7 * 50000.0)                # ~0.9950125
$
$ N = 10000
$ count_top = 0
$
$ for _ in range(N):
$     # Simulate generator units (two independent units)
$     g1_ok = random.random() < R_G_single
$     g2_ok = random.random() < R_G_single
$     gen_supplied = g1_ok or g2_ok
$
$     valve_ok = random.random() < R_valve
$     dist_ok  = random.random() < R_dist
$
$     s1_ok = random.random() < R_sensor
$     s2_ok = random.random() < R_sensor
$     sensor_ok = s1_ok or s2_ok
$
$     mask_ok = random.random() < R_mask
$
$     # Top event: insufficient oxygen delivery
$     system_ok = gen_supplied and valve_ok and dist_ok and sensor_ok and mask_ok
$     if not system_ok:
$         count_top += 1
$
$ freq = count_top / N
$ print("Monte Carlo estimate of P(top event) with N =", N, ":", freq)