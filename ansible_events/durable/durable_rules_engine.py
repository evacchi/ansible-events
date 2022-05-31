# encoding: utf-8
# module durable_rules_engine
# from /Users/evacchi/Devel/rh/exp/ansible-events/venv/lib/python3.9/site-packages/durable_rules_engine.cpython-39-darwin.so
# by generator 1.147
# no doc
# no imports

# functions
import json

import requests


# HOST = "https://6290a0b427f4ba1c65bdaa54.mockapi.io/api/v1"
HOST = "http://localhost:8080"
LAST_RESP = None


def abandon_action(*args, **kwargs): # real signature unknown
    pass

def assert_event(*args, **kwargs): # real signature unknown
    return (0,1)

def assert_events(*args, **kwargs): # real signature unknown
    raise Exception("assert_events")

def assert_fact(*args, **kwargs): # real signature unknown
    global LAST_RESP
    r = requests.post(HOST + '/rules-durable-executors/'+args[0]+'/process', json=json.loads(args[1]))
    LAST_RESP = r.json()

    print( json.dumps(r.json(), indent=2) )

    # {
    #   "sid": "0",
    #   "id": "sid-0",
    #   "$s": 1
    # }

    print(args[0])
    print(args[1])

    return (0,args[0])

def assert_facts(*args, **kwargs): # real signature unknown
    pass

def assert_timers(*args, **kwargs): # real signature unknown
    pass

def cancel_timer(*args, **kwargs): # real signature unknown
    pass

count = 0

def complete_and_start_action(*args, **kwargs): # real signature unknown
    print("complete_and_start_action", args, kwargs)

    #
    # if count==1:
    #     return json.dumps({'r_4': {'m': {'payload': {'text': 'hello'}}}})
    # elif count == 2:
    #     return json.dumps({"r_5":{"m":{"payload": {"text": "hello"}}}})
    # else:
    #     return None

    global LAST_RESP
    print("start_action_for_state", args, kwargs)

    handle = args[0]
    try:
        resp = LAST_RESP.pop()
    except:
        return None

    rule_name = resp["ruleName"]
    facts = resp["facts"]

    new_resp = {rule_name: facts}

    # {'r_3': {'m': {'payload': {'text': 'hello'}}}}
    return json.dumps(new_resp)


def complete_get_idle_state(*args, **kwargs): # real signature unknown
    pass

def complete_get_queued_messages(*args, **kwargs): # real signature unknown
    pass

def create_ruleset(*args, **kwargs): # real signature unknown
    # {
    #   "sid": "0",
    #   "id": "sid-0",
    #   "$s": 1
    # }

    req = { args[0]: json.loads(args[1]) }


    r = requests.post(HOST + '/create-durable-rules-executor', json=req)


    id = r.text
    print(args[0])
    print(args[1])
    return id



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
    global LAST_RESP
    print("start_action_for_state", args, kwargs)

    handle = args[0]
    resp = LAST_RESP.pop()


    # {'r_3': {'m': {'payload': {'text': 'hello'}}}}

    rule_name = resp["ruleName"]
    facts = resp["facts"]

    new_resp = {rule_name: facts}

    return ('{ "sid":"0", "id":"sid-0", "$s":1}', json.dumps(new_resp), handle)

def start_timer(*args, **kwargs): # real signature unknown
    pass

def update_state(*args, **kwargs): # real signature unknown
    print("update_state", args, kwargs)

    global count
    count = count+1

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

