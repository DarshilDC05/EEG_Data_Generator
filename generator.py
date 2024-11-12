import numpy as np
import math
import matplotlib.pyplot as plt
import random

print("Generating data...")

sampling_frequency = 200
x = np.arange(0.005, 45.005, 0.005)

p0 = np.arange(0.005, 45.005, 0.005)
for i in range(0,600):
    temp = np.arange(0.005, 45.005, 0.005)
    rand = np.zeros(9000)
    rand[:] = random.randint(-314,314)/100
    amp = np.zeros(9000)
    amp[:] = random.randint(-100,100)/100
    temp += rand
    temp = np.sin((2*math.pi*(i/1000)*temp))
    temp = temp*amp
    # temp = temp[:]/3000
    p0 += temp

p0 = p0 - x

#delta
p1 = np.arange(0.005, 45.005, 0.005)
for i in range(500,4000):
    temp = np.arange(0.005, 45.005, 0.005)
    rand = np.zeros(9000)
    rand[:] = random.randint(-314,314)/100
    amp = np.zeros(9000)
    amp[:] = random.randint(-100,100)/100
    temp += rand
    temp = np.sin((2*math.pi*(i/1000)*temp))
    temp = temp*amp
    # temp = temp[:]/3000
    p1 += temp

p1 = p1 - x

p1_2int = np.arange(0.005, 45.005, 0.005)
for i in range(4000,5000):
    temp = np.arange(0.005, 45.005, 0.005)
    rand = np.zeros(9000)
    rand[:] = random.randint(-314,314)/100
    amp = np.zeros(9000)
    amp[:] = random.randint(-100,100)/100
    temp += rand
    temp = np.sin((2*math.pi*(i/1000)*temp))
    temp = temp*amp
    # temp = temp[:]/3000
    p1_2int += temp

p1_2int = p1_2int - x


#theta
p2 = np.arange(0.005, 45.005, 0.005)
for i in range(4000,8000):
    temp = np.arange(0.005, 45.005, 0.005)
    rand = np.zeros(9000)
    rand[:] = random.randint(-314,314)/100
    amp = np.zeros(9000)
    amp[:] = random.randint(-100,100)/100
    temp += rand
    temp = np.sin((2*math.pi*(i/1000)*temp))
    temp = temp*amp
    # temp = temp[:]/3000
    p2 += temp

p2 = p2 - x


p2_3int = np.arange(0.005, 45.005, 0.005)
for i in range(8000,9000):
    temp = np.arange(0.005, 45.005, 0.005)
    rand = np.zeros(9000)
    rand[:] = random.randint(-314,314)/100
    amp = np.zeros(9000)
    amp[:] = random.randint(-100,100)/100
    temp += rand
    temp = np.sin((2*math.pi*(i/1000)*temp))
    temp = temp*amp
    # temp = temp[:]/3000
    p2_3int += temp

p2_3int = p2_3int - x

#alpha
p3 = np.arange(0.005, 45.005, 0.005)
for i in range(8000,12000):
    temp = np.arange(0.005, 45.005, 0.005)
    rand = np.zeros(9000)
    rand[:] = random.randint(-314,314)/100
    amp = np.zeros(9000)
    amp[:] = random.randint(-100,100)/100
    temp += rand
    temp = np.sin((2*math.pi*(i/1000)*temp))
    temp = temp*amp
    # temp = temp[:]/3000
    p3 += temp

p3 = p3 - x

p3_4int = np.arange(0.005, 45.005, 0.005)
for i in range(12000,15000):
    temp = np.arange(0.005, 45.005, 0.005)
    rand = np.zeros(9000)
    rand[:] = random.randint(-314,314)/100
    amp = np.zeros(9000)
    amp[:] = random.randint(-100,100)/100
    temp += rand
    temp = np.sin((2*math.pi*(i/1000)*temp))
    temp = temp*amp
    # temp = temp[:]/3000
    p3_4int += temp

p3_4int = p3_4int - x

#beta
p4 = np.arange(0.005, 45.005, 0.005)
for i in range(12000,30000):
    temp = np.arange(0.005, 45.005, 0.005)
    rand = np.zeros(9000)
    rand[:] = random.randint(-314,314)/100
    amp = np.zeros(9000)
    amp[:] = random.randint(-100,100)/100
    temp += rand
    temp = np.sin((2*math.pi*(i/1000)*temp))
    temp = temp*amp
    # temp = temp[:]/3000
    p4 += temp

p4 = p4 - x

p4_5int = np.arange(0.005, 45.005, 0.005)
for i in range(30000,40000):
    temp = np.arange(0.005, 45.005, 0.005)
    rand = np.zeros(9000)
    rand[:] = random.randint(-314,314)/100
    amp = np.zeros(9000)
    amp[:] = random.randint(-100,100)/100
    temp += rand
    temp = np.sin((2*math.pi*(i/1000)*temp))
    temp = temp*amp
    # temp = temp[:]/3000
    p4_5int += temp

p4_5int = p4_5int - x

p4_5int_1 = np.arange(0.005, 45.005, 0.005)
for i in range(30000,35000):
    temp = np.arange(0.005, 45.005, 0.005)
    rand = np.zeros(9000)
    rand[:] = random.randint(-314,314)/100
    amp = np.zeros(9000)
    amp[:] = random.randint(-100,100)/100
    temp += rand
    temp = np.sin((2*math.pi*(i/1000)*temp))
    temp = temp*amp
    # temp = temp[:]/3000
    p4_5int_1 += temp

p4_5int_1 = p4_5int_1 - x

#noise
p5 = np.arange(0.005, 45.005, 0.005)
for i in range(30000,100000):
    temp = np.arange(0.005, 45.005, 0.005)
    rand = np.zeros(9000)
    rand[:] = random.randint(-314,314)/100
    amp = np.zeros(9000)
    amp[:] = random.randint(-100,100)/100
    temp += rand
    temp = np.sin((2*math.pi*(i/1000)*temp))
    temp = temp*amp
    # temp = temp[:]/3000
    p5 += temp

p5 = p5 - x

    

s = np.zeros(9000)
s = 0.001*p0 + 0.15*p1 + 0.1*p1_2int + 0.15*p2 + 0.2*p2_3int + 0.15*p3 + 0.2*p3_4int + 0.2*p4 + 0.05*p4_5int + 0.01*p5 + 0.1*p4_5int_1




f = open("file5_beta.txt", "w")

for i in s:
    f.write(str(i))
    f.write("\n")
f.close()
print("Completed")

# plt.show()