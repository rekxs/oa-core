from oa.core.util import command_registry
import time
from oa.modules.abilities.interact import say, play, mind, say_affirmative
from oa.modules.abilities.other import read_news_feed, diagnostics, read_forecast
from oa.modules.abilities.other import say_day, say_last_command, say_time

from oa.modules.abilities.kasa_smart import red_alert_mode, bulb_color_white, bulb_color_yellow, bulb_color_red, bulb_color_blue,bulb_turn_off, bulb_turn_on, dance_light
from oa.modules.abilities.kasa_smart import bulb_color_purple, bulb_color_green, bulb_color_pink, bulb_color_lime, dance_light, on_plug_2, off_plug_2
from oa.modules.abilities.kasa_smart import bulb_dim_up_10, bulb_dim_down_10, bulb_brightness_1, bulb_brightness_5, bulb_brightness_10, bulb_brightness_30, bulb_brightness_50, bulb_brightness_100

kws = {}

command = command_registry(kws)

@command("Kali")
def hello():
    say('Im here. How may i help you?')

@command(["close assistant", "go to sleep", "kali stop listening", "stop listening"])
def close_assistant():
    play('beep_close.wav')
    mind('boot')

@command([ "no swiper no spying", "no spying", "swiper no spying", "swiper no swiping" ])
def swiper():
    say("ohhh! maaan!")
    mind('boot')

@command(["list commands", "what can i say"])
def list_commands():
    say('- The currently available voice commands are:\n{}'.format(',\n'.join(kws.keys())))

@command(["read world news", "whats up in the world", "news", "nachrichten"])
def read_world_news():
    read_news_feed('https://www.reddit.com/r/worldnews/.rss', 'world')

@command("run diagnostics")
def run_diagnostics():
    diagnostics()

@command("sing a song")
def sing_a_song():
    play('daisy.wav')

@command("what day is it")
def what_day():
    say_day()

@command(["what did I say", "last command", "letzter satz", "was hab ich zuletzt gesagt"])
def what_command():
    say_last_command('You just said:')

@command(["what is the weather", "tell me the weather", "weather", "wetter", "wie ist das wetter"])
def what_weather():
    read_forecast()

@command(["what time is it", "time", "uhrzeit"])
def what_time():
    say_time()



########## TPLINK KASA KL130 ##########

@command(["on the lights", "turn on the lights", "licht an", "lumos"])
def lights_lights_on():
    say_affirmative()
    bulb_turn_on()

@command(["off the lights", "turn off the lights", "licht aus" ])
def lights_lights_off():
    say_affirmative()
    bulb_turn_off()

# Smart bulb colors
'''
@command("change the light color to yellow")
def lights_lights_yellow():
    say_affirmative()
    bulb_color_yellow()

@command("change the light color to red")
def lights_lights_red():
    say_affirmative()
    bulb_color_red()

@command("change the light color to blue")
def lights_color_blue():
    say_affirmative()
    bulb_color_blue()

@command("change the light color to green")
def lights_color_green():
    say_affirmative()
    bulb_color_green()

@command("change the light color to purple")
def light_color_purple():
    say_affirmative()
    bulb_color_purple()

@command("change the light color to pink")
def lights_color_pink():
    say_affirmative()
    bulb_color_pink()

@command("change the light color to white")
def lights_color_white():
    say_affirmative()
    bulb_color_white()

@command("change the light color to lime")
def lights_color_lime():
    say_affirmative()
    bulb_color_lime()
'''
@command(["dim up"])
def lights_up_10():
    bulb_dim_up_10()

@command(["dim down"])
def lights_down_10():
    bulb_dim_down_10()

#Smartbulb brightness
@command (["set light brightness to one", "set light to dimmest", "set to the dimmest", "set dimmest", "dim full"])
def lights_brightness_1():
    say_affirmative()
    bulb_brightness_1()

@command ("set light brightness to five")
def lights_bright_5():
    say_affirmative()
    bulb_brightness_5()


@command ("set light brightness to ten")
def lights_bright_10():
    say_affirmative()
    bulb_brightness_10()

@command (["set light brightness to fifty", "dim fifty", "dim half", "light half", "dim lights to fifty"])
def lights_bright_50():
    say_affirmative()
    bulb_brightness_50()

@command (["it's too bright", "it's too dark in here", "it's too dim"])
def lights_too_bright():
    say('okay')
    time.sleep(0.8)
    bulb_brightness_30()
    say('How about that?')

@command (["set light brightness to one hundred", "full brightness", "lumos maxima"])
def lights_bright_100():
    say_affirmative()
    bulb_brightness_100()

'''
@command("Red alert")
def red_alert():
    play('red_alert.wav')
    red_alert_mode()

@command("countdown")
def count_down():
    say_affirmative()
    play('countdown.wav')


@command("power up plug2")
def turn_on_plug_2():
    say_affirmative()
    on_plug_2()
    say('done')

@command("power down plug2")
def turn_off_plug_2():
    say_affirmative()
    off_plug_2()
    say('done')
'''


@command("dancing lights")
def dancing_light():
    say_affirmative()
    play('Chad_Crouch_Algorithms.wav')
    dance_light()
