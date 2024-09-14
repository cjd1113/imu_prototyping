import time
import sys
import numpy as np
import matplotlib.pyplot as plt

accel_data = np.load('accel_data.npy')
gyro_data = np.load('gyro_data.npy')
mag_data = np.load('mag_data.npy')

accel_data = accel_data[1:-1,:]
gyro_data = gyro_data[1:-1,:]
mag_data = mag_data[1:-1,:]

# Create a time vector
time_vector_length = np.size(accel_data,0) #we need to remove the first data point in our data vectors 
freq = 8
dt = 1/freq
time_end = dt*time_vector_length
time_vector = np.arange(0,time_end,dt)
print(time_vector)

plt.figure(0)
plt.plot(time_vector, accel_data[:,0])
plt.plot(time_vector, accel_data[:,1])
plt.plot(time_vector, accel_data[:,2])
plt.xlabel('Time (s)')
plt.ylabel('Acceleration (g)')
plt.title('Body acceleration')
plt.legend(['x','y','z (up)'])


plt.figure(1)
plt.plot(time_vector, gyro_data[:,0])
plt.plot(time_vector, gyro_data[:,1])
plt.plot(time_vector, gyro_data[:,2])
plt.xlabel('Time (s)')
plt.ylabel('Angular rate (deg/s)')
plt.title('Body angular rate')
plt.legend(['x','y','z (about up axis)'])


plt.figure(2)
plt.plot(time_vector, mag_data[:,0])
plt.plot(time_vector, mag_data[:,1])
plt.plot(time_vector, mag_data[:,2])
plt.xlabel('Time (s)')
plt.ylabel('Magnetic field (uT)')
plt.title('Magnetometer output')
plt.legend(['x','y','z'])

plt.show()
#plt.show(block=False)

#print('Enter "close" to close the plots')
#prompt = input()
#if prompt == 'close':
#   plt.close('all')
    
