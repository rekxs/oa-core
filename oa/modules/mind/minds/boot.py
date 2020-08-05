import oa.legacy

from oa.core.util import command_registry

from oa.modules.abilities.interact import say, play, mind


kws = {}
command = command_registry(kws)

@command(["boot mind","warm up"])
def response_sound():
  play('r2d2.wav')
  
@command(["open assistant", "Kali wake up", "Hey Kali", "Kali"])
def open_root():
  #play('beep_open.wav')
  say('Whats up?')
  mind('root')

@command(["list commands", "help"])
def list_commands():
    say('The currently available voice commands are..')
    [say(cmd) for cmd in kws.keys()]

@command(["stop listening", "no swiper no spying", "no spying", "swipter no spying"])
def do_exit():
    oa.legacy.hub.finished.set()
