# mind.py - Core mind operations.

import importlib
import logging
import os

import oa.legacy

from oa.modules.abilities.core import info, call_function, get
from oa.modules.abilities.system import read_file, sys_exec


""" Core mind functions. """

_history = []

def load_mind(path):
    """ Load a mind by its `name`. """
    mind = oa.legacy.Core()
    mind.module = path
    mind.name = os.path.splitext(os.path.basename(mind.module))[0]
    mind.cache_dir = os.path.join(oa.legacy.core_directory, 'cache', mind.name)

    # Make directories.
    if not os.path.exists(mind.cache_dir):
        os.makedirs(mind.cache_dir)

    M = importlib.import_module("oa.modules.mind.minds"+".{}".format(mind.name))
    mind.__dict__.update(M.__dict__)
    
    # Add command keywords without spaces.
    mind.kws = {}
    for key, value in M.kws.items():
        for synonym in key.strip().split(','):
            mind.kws[synonym] = value

    return mind

def set_mind(name, history=True):
    """ Activate new mind. """
    logging.info('Opening Mind: {}'.format(name))
    if history:
        _history.append(name)
        
    oa.legacy.mind = oa.legacy.minds[name]
    return oa.legacy.mind

def switch_back():
    """ Switch back to the previous mind. (from `switch_hist`). """
    set_mind(_history.pop(), history=False)

def load_minds():
    """ Load and check dictionaries for all minds. Handles updating language models using the online `lmtool`.
    """
    logging.info('Loading minds...')
    mind_path = os.path.join(os.path.dirname(__file__), 'minds')
    for mind in os.listdir(mind_path):
        if mind.lower().endswith('.py'):
            logging.info("<- {}".format(mind))
            m = load_mind(os.path.join(mind_path, mind))
            oa.legacy.minds[m.name] = m
    logging.info('Minds loaded!')

def _in(ctx):

    default_mind = 'boot'
    load_minds()
    set_mind(default_mind)

    logging.debug('"{}" is now listening. Say "Boot Mind!" to see if it can hear you.'.format(default_mind))


    while not ctx.finished.is_set():
        text = get()
        logging.debug('Input: {}'.format(text))
        mind = oa.legacy.mind
        if (text is None) or (text.strip() == ''):
            # Nothing to do.
            continue
        t = text.upper()

        # Check for a matching command.
        fn = mind.kws.get(t, None)

        if fn is not None:
            # There are two types of commands, stubs and command line text.
            # For stubs, call `perform()`.
            if oa.legacy.isCallable(fn):
                call_function(fn)
                oa.legacy.oa.last_command = t
            # For strings, call `sys_exec()`.
            elif isinstance(fn, str):
                sys_exec(fn)
                oa.legacy.oa.last_command = t
            else:
                # Any unknown command raises an exception.
                raise Exception("Unable to process: {}".format(text))
        yield text

