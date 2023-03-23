from machine import Pin
import time, neopixel
from rotary_irq_rp2 import RotaryIRQ

def BEEP_BOOP(*_):
    bounces += 1
    print("Beep Boop ", bounces)

def main():
    print("Running")

    bounces = 0

    led = Pin(25, Pin.OUT) #Onboard LED
    center_button = Pin(1, Pin.IN, Pin.PULL_UP)
    center_button.irq(trigger=Pin.IRQ_FALLING, handler=BEEP_BOOP)

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

    #            
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
            
        time.sleep_ms(25)

if __name__ == "__main__":
    main()