Temperature-Controlled-MOSFET-Driver-Using-Raspberry-Pi-Pico

This project presents the design of a temperature-controlled power switching circuit using a Raspberry Pi Pico microcontroller, NTC thermistors, a MOSFET driver, and power MOSFETs. The primary objective is to monitor temperature and control a high-current load based on the measured temperature.

The sensing element used is a 10kΩ NTC thermistor, which changes resistance with temperature. It is connected in a voltage divider configuration with a fixed 10kΩ resistor, and the output voltage is fed into the ADC pin of the Raspberry Pi Pico. The microcontroller reads this analog voltage, converts it into a digital value, and calculates the temperature using the thermistor beta equation.

The Raspberry Pi Pico is selected due to its built-in ADC, ease of programming using MicroPython, and sufficient GPIO pins. Based on the computed temperature, the Pico generates a PWM signal that is sent to the IR2110 MOSFET driver IC. The IR2110 is chosen because it provides proper gate drive voltage and current required to efficiently switch power MOSFETs.

Three IRF3205 N-channel MOSFETs are connected in parallel to handle high current loads. These MOSFETs are selected due to their low on-resistance and high current capability. Gate resistors are used to limit inrush current and ensure stable switching. Pull-down resistors are added to prevent floating gates.

A bulk capacitor of 1000µF is placed across the supply to stabilize voltage and handle transient current demands during switching. Additional small capacitors are placed near the driver and microcontroller for noise filtering.

The circuit is powered using a DC-DC converter (LM2596) to step down the input voltage to a suitable level for the microcontroller and driver. Proper PCB layout practices such as short gate drive paths, thick power traces, and separation of signal and power grounds are followed to ensure reliable operation.

Overall, the design ensures efficient temperature monitoring and safe high-power switching, making it suitable for applications like thermal protection systems and automated control circuits.

