import machine, time, neopixel
from rotary_irq_rp2 import RotaryIRQ

# 16 neopixels, gpio pin 0
pixels = neopixel.NeoPixel(machine.Pin(0), 16)

r = RotaryIRQ(pin_num_clk=15, 
              pin_num_dt=13, 
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
        np[val_new] = (6*val_new, 96-(6*val_new), 0)
        val_old = val_new
        
        
    time.sleep_ms(50)