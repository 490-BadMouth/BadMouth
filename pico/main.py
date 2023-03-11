from machine import Pin
import time, neopixel
from rotary_irq_rp2 import RotaryIRQ

print("Running")

led = Pin(25, Pin.OUT) #Onboard LED

# 16 neopixels, gpio pin 0
np = neopixel.NeoPixel(machine.Pin(0), 16)
np[0] = (15,0,0)

r = RotaryIRQ(pin_num_clk=14, 
              pin_num_dt=15, 
              min_val=0, 
              max_val=15, 
              reverse=True, 
              range_mode=RotaryIRQ.RANGE_BOUNDED,
              pull_up = True)
              
val_old = r.value()
while True:
    val_new = r.value()
    
    if val_old != val_new:
        if val_old > val_new:
            np[val_old] = (0, 0, 0)
        np[val_new] = (15-val_new, val_new, 0)
        np.write()
        val_old = val_new
        led.toggle()
        
    time.sleep_ms(50)
