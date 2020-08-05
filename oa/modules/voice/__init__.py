# voice.py - Audio output: Text To Speech (TTS)

import logging

from oa.modules.abilities.core import get, put


import platform
import os
sys_os = platform.system()
flMac = (sys_os == 'Darwin')
engine = "default"
if flMac:
    import subprocess
else:
    import pyttsx3


def _in(ctx):
    if not flMac:
        if os.system('which festival') != 0:
            tts = pyttsx3.init()
        else:
            engine = "festival"
            tts = pyttsx3.init()

    
    while not ctx.finished.is_set():
        s = get()
        logging.debug("Saying: %s", s)

        # Pause Ear (listening) while talking. Mute TTS.
        # TODO: move this somewhere else
        put('speech_recognition', 'mute')

        if flMac:
            _msg = subprocess.Popen(['echo', s], stdout=subprocess.PIPE)
            _tts = subprocess.Popen(['say'], stdin=_msg.stdout)
            _msg.stdout.close()
            _tts.communicate()
        #elif engine === "festival":
        #    os.system('echo "{0}" | festival --tts'.format(s))
        else:
            if engine == "festival":
                os.system('echo "{0}" | festival --tts'.format(s))
            else:
                tts.say(s)
                tts.runAndWait()

        # Wait until speaking ends.
        # Continue ear (listening). Unmute TTS.
        # TODO: move this somewhere else
        put('speech_recognition', 'unmute')
