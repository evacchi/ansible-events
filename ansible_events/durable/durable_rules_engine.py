# encoding: utf-8
# module durable_rules_engine
# from /Users/evacchi/Devel/rh/exp/ansible-events/venv/lib/python3.9/site-packages/durable_rules_engine.cpython-39-darwin.so
# by generator 1.147
# no doc
# no imports

# functions
import json

import requests


HOST = "https://6290a0b427f4ba1c65bdaa54.mockapi.io/api/v1"

def abandon_action(*args, **kwargs): # real signature unknown
    pass

def assert_event(*args, **kwargs): # real signature unknown
    return (0,1)

def assert_events(*args, **kwargs): # real signature unknown
    raise Exception("assert_events")

def assert_fact(*args, **kwargs): # real signature unknown
    r = requests.post(HOST + '/assert-fact', data={ "name": args[0], "data": args[1] })
    print( json.dumps(r.json(), indent=2) )

    print(args[0])
    print(args[1])

    return (0,1)

def assert_facts(*args, **kwargs): # real signature unknown
    pass

def assert_timers(*args, **kwargs): # real signature unknown
    pass

def cancel_timer(*args, **kwargs): # real signature unknown
    pass

def complete_and_start_action(*args, **kwargs): # real signature unknown
    pass

def complete_get_idle_state(*args, **kwargs): # real signature unknown
    pass

def complete_get_queued_messages(*args, **kwargs): # real signature unknown
    pass

def create_ruleset(*args, **kwargs): # real signature unknown
    r = requests.post(HOST + '/create-ruleset', data={ "name": args[0], "data": args[1] })
    print( json.dumps(r.json(), indent=2) )
    print(args[0])
    print(args[1])
    return 1



def delete_ruleset(*args, **kwargs): # real signature unknown
    pass

def delete_state(*args, **kwargs): # real signature unknown
    raise Exception("delete_state")

def get_events(*args, **kwargs): # real signature unknown
    raise Exception("get_events")

def get_facts(*args, **kwargs): # real signature unknown
    raise Exception("get_facts")

def get_state(*args, **kwargs): # real signature unknown
    pass

def renew_action_lease(*args, **kwargs): # real signature unknown
    pass

def retract_fact(*args, **kwargs): # real signature unknown
    raise Exception("retract_fact")

def retract_facts(*args, **kwargs): # real signature unknown
    pass

def set_delete_message_callback(*args, **kwargs): # real signature unknown
    pass

def set_get_idle_state_callback(*args, **kwargs): # real signature unknown
    pass

def set_get_queued_messages_callback(*args, **kwargs): # real signature unknown
    pass

def set_queue_message_callback(*args, **kwargs): # real signature unknown
    pass

def set_store_message_callback(*args, **kwargs): # real signature unknown
    pass

def start_action(*args, **kwargs): # real signature unknown
    raise Exception("start_action")

def start_action_for_state(*args, **kwargs): # real signature unknown
    return ('{ "sid":"0", "id":"sid-0", "$s":1}', '{"r_0":{"m":{"subject": "World"}}}', 1)

def start_timer(*args, **kwargs): # real signature unknown
    pass

def update_state(*args, **kwargs): # real signature unknown
    pass

# classes

class error(Exception):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



# variables with complex values

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x107789f70>'

__spec__ = None # (!) real value is "ModuleSpec(name='durable_rules_engine', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x107789f70>, origin='/Users/evacchi/Devel/rh/exp/ansible-events/venv/lib/python3.9/site-packages/durable_rules_engine.cpython-39-darwin.so')"
