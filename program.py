import FaBo9Axis_MPU9250
import time
import sys
import numpy as np

mpu9250 = FaBo9Axis_MPU9250.MPU9250()
#go to /usr/local/lib/python3.9/dist-packages/FaBo9Axis_MPU9250 to configure ranges of the MPU9250

accel_store = np.array([[0,0,0]])
gyro_store = np.array([[0,0,0]])
mag_store = np.array([[0,0,0]])

try:
    while True:
        accel = mpu9250.readAccel()
        print(" ax = " ,  accel['x'])
        print(" ay = " ,  accel['y'])
        print(" az = " ,  accel['z'])
        accel_temp = np.array([[accel['x'], accel['y'], accel['z']]])
        accel_store = np.append(accel_store, accel_temp, axis=0)
        
        
        gyro = mpu9250.readGyro()
        print(" gx = " ,  gyro['x'])
        print(" gy = " ,  gyro['y'])
        print(" gz = " ,  gyro['z'])
        gyro_temp = np.array([[gyro['x'], gyro['y'], gyro['z']]])
        gyro_store = np.append(gyro_store, gyro_temp, axis=0)

        mag = mpu9250.readMagnet()
        print(" mx = " ,  mag['x'])
        print(" my = " ,  mag['y'])
        print(" mz = " ,  mag['z'])
        mag_temp = np.array([[mag['x'], mag['y'], mag['z']]])
        mag_store = np.append(mag_store, mag_temp, axis=0)
        

        time.sleep(0.1)

except KeyboardInterrupt:
    
    print("\n Terminating data collection.")
    np.save('accel_data',accel_store)
    np.save('gyro_data',gyro_store)
    np.save('mag_data',mag_store)
    sys.exit()