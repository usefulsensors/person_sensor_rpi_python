import time

import smbus

# I2C channel 1 is connected to the GPIO pins
channel = 1

# The person sensor has the I2C ID of hex 62, or decimal 98.
peripheral_address = 0x62

# Sensor data length in bytes.
sensor_data_byte_count = 13

# How long to pause between sensor polls.
sensor_delay = 0.2

# Initialize I2C (SMBus)
bus = smbus.SMBus(channel)

while True:
  try:
    sensor_bytes = bus.read_i2c_block_data(peripheral_address, 0, sensor_data_byte_count)
  except OSError:
    print("No person sensor data found")
    time.sleep(sensor_delay)
    continue
  print("Sensor data found")
  time.sleep(sensor_delay)