#from ADCPi import ADCPi
import abelectronics

adc = ADCPi(0x68, 0x69, 18)

adc.read_voltage(1)