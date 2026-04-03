from machine import ADC, Pin, PWM
import math
import timeADC_PIN = 26        
PWM_PIN = 15        
THRESHOLD = 40      
R0 = 10000          
BETA = 3950
T0 = 298.15         
SERIES_RESISTOR = 10000  
adc = ADC(ADC_PIN)
pwm = PWM(Pin(PWM_PIN))
pwm.freq(1000)
def read_temperature():
    adc_value = adc.read_u16()
    voltage = adc_value * 3.3 / 65535
    if voltage == 0:
        return 0
    resistance = SERIES_RESISTOR * (3.3 / voltage - 1)
    temp_k = 1 / (1/T0 + (1/BETA) * math.log(resistance / R0))
    temp_c = temp_k - 273.15
    return temp_c
while True:
    temp = read_temperature()
    print("Temperature:", temp)

    if temp > THRESHOLD:
        pwm.duty_u16(50000)   
    else:
        pwm.duty_u16(0)
    time.sleep(1)