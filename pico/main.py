from machine import Pin, UART
import time, neopixel
from rotary_irq_rp2 import RotaryIRQ
debounce_time = 200

# Init UART
uart1 = UART(1, baudrate=115200, tx=Pin(4), rx=Pin(5), bits=8, parity=None, stop=1)

# Button press ISR
def button_isr(button):
    button.irq(handler=None)
    button_out = f'{button}'
    print(button_out)
    button_char = button_out[8]
    if button_char == '2':
        uart1.write(b'C\n')
    elif button_char == '3':
        uart1.write(b'R\n')
    elif button_char == '6':
        uart1.write(b'U\n')
    elif button_char == '7':
        uart1.write(b'L\n')
    elif button_char == '8':
        uart1.write(b'D\n')

    machine.Timer(-1).init(period=debounce_time, mode=machine.Timer.ONE_SHOT, callback=lambda t:button.irq(handler=lambda pin:button_isr(button), trigger=machine.Pin.IRQ_FALLING))

def main():
    print("Running")
    #self.bounces = 0
    
    led = Pin(25, Pin.OUT) #Onboard LED

    # Set up the button pin with the pull-up resistor
    button1= machine.Pin(2, machine.Pin.IN, machine.Pin.PULL_UP)
    button2= machine.Pin(3, machine.Pin.IN, machine.Pin.PULL_UP)
    button3= machine.Pin(6, machine.Pin.IN, machine.Pin.PULL_UP)
    button4= machine.Pin(7, machine.Pin.IN, machine.Pin.PULL_UP)
    button5= machine.Pin(8, machine.Pin.IN, machine.Pin.PULL_UP)

    # # Set up the interrupt for the button
    # button1.irq(trigger=machine.Pin.IRQ_FALLING, handler=button1_isr)
    # button2.irq(trigger=machine.Pin.IRQ_FALLING, handler=button2_isr)
    # button3.irq(trigger=machine.Pin.IRQ_FALLING, handler=button3_isr)
    # button4.irq(trigger=machine.Pin.IRQ_FALLING, handler=button4_isr)
    # button5.irq(trigger=machine.Pin.IRQ_FALLING, handler=button5_isr)
    button1.irq(trigger=machine.Pin.IRQ_FALLING, handler=lambda pin:button_isr(button1))
    button2.irq(trigger=machine.Pin.IRQ_FALLING, handler=lambda pin:button_isr(button2))
    button3.irq(trigger=machine.Pin.IRQ_FALLING, handler=lambda pin:button_isr(button3))
    button4.irq(trigger=machine.Pin.IRQ_FALLING, handler=lambda pin:button_isr(button4))
    button5.irq(trigger=machine.Pin.IRQ_FALLING, handler=lambda pin:button_isr(button5))

    # 16 neopixels, gpio pin 0
    np = neopixel.NeoPixel(machine.Pin(28), 16)
    np[0] = (15,0,0)

    r = RotaryIRQ(pin_num_clk=15, 
                pin_num_dt=14,
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
            np[val_new] = (val_new, 15-val_new, 0)
            np.write()
            uart1.write(b'%i\n' % val_new)
            print("current value is: ", val_new)
            val_old = val_new
            led.toggle()
        time.sleep_ms(25)

if __name__ == "__main__":
    main()