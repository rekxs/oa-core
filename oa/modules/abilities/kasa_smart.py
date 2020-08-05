import asyncio
#from pyHS100 import SmartPlug, SmartBulb, SmartStrip
from kasa import SmartPlug, SmartBulb, SmartStrip
from pprint import pformat as pf
import time

from oa.modules.abilities.interact import say


### TPLINK KASA HS100
### Change the ip addresss accordingly

async def plug_turn_on():
    await plug.update()
    await plug.turn_on()
async def plug_turn_off():
    await plug.turn_off()


### TPLINK KASA KL130
### Change the ip addresss accordingly
bulbs = {}

print('Loading smartbulb <--- KL60')
print('Loading smartbulb <--- KL110')
bulbs = {
  "schlafzimmer": SmartBulb("192.168.2.117"),
  "wohnzimmer": SmartBulb("192.168.2.119")
}

#wohnzimmer = SmartBulb("192.168.2.119")


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
def bulb_turn_on(room):
    bulb = bulbs[room]
    if bulb:
      asyncio.run(bulb.update())
      if bulb.is_on == True:
        say("But It's already turn on. Nothing to be done.")
      else:
        asyncio.run(bulb.turn_on())
    
def bulb_turn_off(room):
  bulb = bulbs[room]
  if bulb:
    asyncio.run(bulb.update())
    if bulb.is_off == True:
      say("But it's already turn off. Nothing to be done.")
    else:
      asyncio.run(bulb.turn_off())

# bulb brightness
def bulb_dim_down_10(room):
  bulb = bulbs[room]
  if bulb:
    asyncio.run(bulb.update())
    cur = bulb.brightness
    asyncio.run(bulb.set_brightness(cur-10))
def bulb_dim_up_10(room):
  bulb = bulbs[room]
  if bulb:
    asyncio.run(bulb.update())
    cur = bulb.brightness
    asyncio.run(bulb.set_brightness(cur+10))
def bulb_brightness_1(room):
  bulb = bulbs[room]
  if bulb:
    asyncio.run(bulb.update())
    asyncio.run(bulb.set_brightness(1))
def bulb_brightness_5(room):
  bulb = bulbs[room]
  if bulb:
    asyncio.run(bulb.update())
    asyncio.run(bulb.set_brightness(5))
def bulb_brightness_10(room):
  bulb = bulbs[room]
  if bulb:
    asyncio.run(bulb.update())
    asyncio.run(bulb.set_brightness(10))
def bulb_brightness_50(room):
  bulb = bulbs[room]
  if bulb:
    asyncio.run(bulb.update())
    asyncio.run(bulb.set_brightness(50))
def bulb_brightness_30(room):
  bulb = bulbs[room]
  if bulb:
    asyncio.run(bulb.update())
    asyncio.run(bulb.set_brightness(30))
def bulb_brightness_100(room):
  bulb = bulbs[room]
  if bulb:        
    asyncio.run(bulb.update())
    asyncio.run(bulb.set_brightness(100))


### TPLINK KASA HS300
### Change the ip addresss accordingly


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
