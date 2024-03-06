# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT


# We will first import all the libraries
import time
import board
import adafruit_mpu6050
import matplotlib.pyplot as plt
from timeit import default_timer as timer


# Now we will define the variables
ct = 0  # create a counter and set its value to zero as was done in Lab 2
time_list = []  # create an empty list for keeping track of time 
temperature_list = []  # create an empty list for keeping track of time 
x_acceleration_list = []  # create an empty list for keeping track of time 
i2c = board.I2C()  # detect the connection for the IMU
mpu = adafruit_mpu6050.MPU6050(i2c)  # define the IMU as mpu using thins line
global_time = timer()  # initialize the global timer to track how many seconds have passed since the program started
start_time = timer()  # initialize the start timer for checking the elapsed time later


# Create a While loop to continuously obtain IMU values
while ct is not 5:  # while the counter is not equal to 5 the loop will run (you may change 5 to the number of values that you need)
    end_time = timer()  # initialize the end timer for checking the elapsed time later
    difference = end_time - start_time  # calculate the elapsed time since the while loop was executed

    if int(difference) is 5:  # same as Lab2: This statement checks if 5 seconds have passed. If yes, then it goes within the loop
        
        print("Acceleration: X:%.2f, Y: %.2f, Z: %.2f m/s^2" % (mpu.acceleration))  # print the IMU accerleration readings
        print("Gyro X:%.2f, Y: %.2f, Z: %.2f rad/s" % (mpu.gyro))  # print the IMU gyroscope readings pertaining to orientation
        print("Temperature: %.2f C" % mpu.temperature)  # print the IMU temperature readings
        print("")  # print a new line
        time.sleep(1)  # wait 1 second 

        ''' Keep Track of Time and Different IMU Readings in Lists '''
        time_list.append(end_time-global_time)  # add the the time elapsed since the program was execute to the empty list created on Line 15
        temperature_list.append(mpu.temperature)  # add the the temperature to the empty list created on Line 16
        x_acceleration_list.append(mpu.acceleration[0])  # add the the acceleration in the X-axis to the empty list created on Line 17
        start_time = end_time  # set start time equal to the end time
        ct += 1  # increment the counter


# Now we will visualize the results
print(time_list)  # print the list of temperature readings that was populated in Line 37
print(temperature_list)  # print the list of temperature readings that was populated in Line 38
print(x_acceleration_list)  # print the list of acceleration readings that was populated in Line 39

# Create the first plot for temperature 
plt.figure()  # initialize a figure
plt.plot(time_list, temperature_list)  # plot the time on the x-axis and the temperature on the y-axis
plt.title('temperature')  # create a title for the plot
plt.xlabel('time')  # label the x-axis
plt.ylabel('temperature in degrees celcius')  # label the y-axis
plt.savefig('temperature.png')  # save the image

# Create the second plot for acceleration 
plt.figure()  # initialize a figure
plt.plot(time_list, x_acceleration_list)
plt.title('acceleration')  # create a title for the plot
plt.xlabel('time')  # label the x-axis
plt.ylabel('acceleration in the x axis in m/s^2')  # label the y-axis
plt.savefig('acceleration.png')  # save the image





''' CGT 575 / ASM 59100 Code Block Starts For Lab3 Homework Assignment '''
# You are required to plot 100 readings from the IMU 
# Plot two different values of your choice (temperature, acceleration in any axis, or the gyroscope readings) against time
# You may be creative in the type of plot that you want to use (Example plots: Line Graphs, Scatter plots, Bubble Charts, Bar Charts, etc.)
# You may search the "matplotlib.pyplot" Python library for online examples on how you may change to different plots
# If you want, you may also elect to export the values and plot them in Excel

#### Enter Code Will Below This Line:

''' CGT 575 / ASM 59100 Code Block Ends For Lab3 Homework Assignment '''
