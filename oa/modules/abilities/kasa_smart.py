from pyHS100 import SmartPlug, SmartBulb, SmartStrip
from pprint import pformat as pf
import time

from oa.modules.abilities.interact import say


### TPLINK KASA HS100
### Change the ip addresss accordingly

print('loading smartplug <--- HS100')
plug = SmartPlug("192.168.1.x")


def plug_turn_on():
    plug.turn_on()
def plug_turn_off():
    plug.turn_off()


### TPLINK KASA KL130
### Change the ip addresss accordingly
print('Loading smartbulb <--- KL130')
bulb = SmartBulb("192.168.1.24")


def red_alert_mode():
    bulb.turn_on()
    bulb.hsv = (0, 75, 100)
    time.sleep (0.7)
    bulb.turn_off()
    time.sleep (0.7)
    bulb.turn_on()
    time.sleep (0.7)
    bulb.turn_off()
    time.sleep (0.7)
    bulb.turn_on()
    time.sleep (0.7)
    bulb.turn_off()
    time.sleep (0.7)
    bulb.turn_on()
    time.sleep (0.7)
    bulb.turn_off()
    time.sleep (0.7)
    bulb.turn_on()
    time.sleep (0.7)
    bulb.turn_off()
    time.sleep (0.7)
    bulb.turn_on()
    time.sleep(0.7)
    bulb.turn_off()


def dance_light():
    bulb.turn_on()
    bulb_color_red()
    time.sleep(0.4)
    bulb.turn_off()
    time.sleep(0.4)
    bulb.turn_on()
    bulb_color_blue()
    time.sleep(0.4)
    bulb.turn_off()
    time.sleep(0.4)
    bulb.turn_on()
    bulb_color_green()
    time.sleep(0.4)
    bulb_turn_off()
    time.sleep(0.4)
    bulb.turn_on()
    bulb_color_red()
    time.sleep(0.4)
    bulb.turn_off()
    time.sleep(0.4)
    bulb.turn_on()
    bulb_color_blue()
    time.sleep(0.4)
    bulb.turn_off()
    time.sleep(0.4)
    bulb.turn_on()
    bulb_color_green()
    time.sleep(0.4)
    bulb.turn_off()
    time.sleep(0.4)
    bulb.turn_on()
    bulb_color_red()
    time.sleep(0.4)
    bulb.turn_off()
    time.sleep(0.4)
    bulb.turn_on()
    bulb_color_blue()
    time.sleep(0.4)
    bulb.turn_on()
    bulb_color_yellow()
    time.sleep(0.4)
    bulb.turn_off()


# Change color to YELLOW
def bulb_color_yellow():
    if bulb.is_on == False:
      say("Please turn on the lights first.")
    else:
      bulb.color_temp = 2500
      bulb.hsv = (0, 0, 100)

# Change color to RED
def bulb_color_red():
    if bulb.is_on == False:
      say("Please turn on the lights first.")
    else:
      bulb.hsv = (0, 75, 100)

# Change color to GREEN
def bulb_color_green():
    if bulb.is_on == False:
      say("Please turn on the lights first.")
    else:
      bulb.hsv = (120, 75, 100)

# Change color to BLUE
def bulb_color_blue():
    if bulb.is_on == False:
      say("Please turn on the lights first.")
    else:
      bulb.hsv = (240, 75, 100)

# Change color to PURPLE
def bulb_color_purple():
    if bulb.is_on == False:
      say("Please turn on the lights first.")
    else:
      bulb.hsv = (259, 75, 100)

# Change color to PINK
def bulb_color_pink():
    if bulb.is_on == False:
      say("Please turn on the lights first.")
    else:
      bulb.hsv = (301, 79, 100)

def bulb_color_white():
    if bulb.is_on == False:
      say("Please turn on the lights first.")
    else:
      bulb.color_temp = (9000)

def bulb_color_lime():
    if bulb.is_on == False:
      say("Please turn on the lights first.")
    bulb.hsv = (106, 48, 100)

# Turn ON and OFF state with checker
def bulb_turn_on():
    if bulb.is_on == True:
      say("But It's already turn on. Nothing to be done.")
    else:
      bulb.turn_on()

def bulb_turn_off():
    if bulb.is_off == True:
      say("But it's already turn off. Nothing to be done.")
    else:
      bulb.turn_off()

# bulb brightness
def bulb_brightness_1():
    bulb.brightness = 1
def bulb_brightness_5():
    bulb.brightness = 5
def bulb_brightness_10():
    bulb.brightness = 10
def bulb_brightness_50():
    bulb.brightness = 50
def bulb_brightness_30():
    bulb.brightness = 30
def bulb_brightness_100():
    bulb.brightness = 100


### TPLINK KASA HS300
### Change the ip addresss accordingly

print('LOADING SMART-STRIP <--- HS300')
strip = SmartStrip("192.168.1.22")

# Plug1
def on_plug_0():
    strip.turn_on(index=0)
def off_plug_0():
    strip.turn_off(index=0)

# Plug2
def on_plug_1():
    strip.turn_on(index=1)
def off_plug_1():
    strip.turn_off(index=1)

# Plug3
def on_plug_2():
    strip.turn_on(index=2)
def off_plug_2():
    strip.turn_off(index=2)

# Plug4
def on_plug_3():
    strip.turn_on(index=3)
def off_plug_3():
    strip.turn_off(index=3)

# Plug5
def on_plug_4():
    strip.turn_on(index=4)
def off_plug_4():
    strip.turn_off(index=4)

# Plug6
def on_plug_5():
    strip.turn_on(index=5)
def off_plug_5():
    strip.turn_off(index=5)
