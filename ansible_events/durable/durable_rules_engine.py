import json

import requests


class DurableRulesEngine:
    host = "http://localhost:8080"
    last_resp = None

    def create_ruleset(self, ruleset_name, ruleset_string):  # real signature unknown
        # {
        #   "sid": "0",
        #   "id": "sid-0",
        #   "$s": 1
        # }

        req = {ruleset_name: json.loads(ruleset_string)}

        r = requests.post(self.host + '/create-durable-rules-executor', json=req)

        id = r.text
        print(ruleset_name)
        print(ruleset_string)
        return id

    def assert_fact(self, session_id, serialized_fact):  # real signature unknown
        r = requests.post(self.host + '/rules-durable-executors/' + session_id + '/process',
                          json=json.loads(serialized_fact))
        self.last_resp = r.json()
        self.last_resp.reverse()
        self.last_resp.pop()

        print(json.dumps(r.json(), indent=2))

        # {
        #   "sid": "0",
        #   "id": "sid-0",
        #   "$s": 1
        # }

        print(session_id)
        print(session_id)

        return (0, session_id)

    def start_action_for_state(self, handle):  # real signature unknown
        print("start_action_for_state", handle)

        try:
            resp = self.last_resp.pop()
        except:
            return None

        # {'r_3': {'m': {'payload': {'text': 'hello'}}}}

        rule_name = resp["ruleName"]
        facts = resp["facts"]

        new_resp = {rule_name: facts}

        return ('{ "sid":"0", "id":"sid-0", "$s":1}', json.dumps(new_resp), handle)

    def complete_and_start_action(self, handle):  # real signature unknown
        print("complete_and_start_action", handle)

        #
        # if count==1:
        #     return json.dumps({'r_4': {'m': {'payload': {'text': 'hello'}}}})
        # elif count == 2:
        #     return json.dumps({"r_5":{"m":{"payload": {"text": "hello"}}}})
        # else:
        #     return None

        try:
            resp = self.last_resp.pop()
        except:
            return None

        rule_name = resp["ruleName"]
        facts = resp["facts"]

        new_resp = {rule_name: facts}

        # {'r_3': {'m': {'payload': {'text': 'hello'}}}}
        return json.dumps(new_resp)


SINGLETON = DurableRulesEngine()


class error(Exception):
    # no doc
    def __init__(self, *args, **kwargs):  # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


def abandon_action(*args, **kwargs):  # real signature unknown
    pass


def assert_event(*args, **kwargs):  # real signature unknown
    return (0, 1)


def assert_events(*args, **kwargs):  # real signature unknown
    raise Exception("assert_events")


def assert_fact(session_id, serialized_fact):
    return SINGLETON.assert_fact(session_id, serialized_fact)


def assert_facts(*args, **kwargs):  # real signature unknown
    pass


def assert_timers(*args, **kwargs):  # real signature unknown
    pass


def cancel_timer(*args, **kwargs):  # real signature unknown
    pass


def complete_get_idle_state(*args, **kwargs):  # real signature unknown
    pass


def complete_get_queued_messages(*args, **kwargs):  # real signature unknown
    pass


def create_ruleset(ruleset_name, ruleset_string):
    return SINGLETON.create_ruleset(ruleset_name, ruleset_string)


def delete_ruleset(*args, **kwargs):  # real signature unknown
    pass


def delete_state(*args, **kwargs):  # real signature unknown
    raise Exception("delete_state")


def get_events(*args, **kwargs):  # real signature unknown
    raise Exception("get_events")


def get_facts(*args, **kwargs):  # real signature unknown
    raise Exception("get_facts")


def get_state(*args, **kwargs):  # real signature unknown
    pass


def renew_action_lease(*args, **kwargs):  # real signature unknown
    pass


def retract_fact(*args, **kwargs):  # real signature unknown
    raise Exception("retract_fact")


def retract_facts(*args, **kwargs):  # real signature unknown
    pass


def set_delete_message_callback(*args, **kwargs):  # real signature unknown
    pass


def set_get_idle_state_callback(*args, **kwargs):  # real signature unknown
    pass


def set_get_queued_messages_callback(*args, **kwargs):  # real signature unknown
    pass


def set_queue_message_callback(*args, **kwargs):  # real signature unknown
    pass


def set_store_message_callback(*args, **kwargs):  # real signature unknown
    pass


def start_action(*args, **kwargs):
    raise Exception("start_action")


def start_action_for_state(handle, state_handle):
    return SINGLETON.start_action_for_state(handle)


def complete_and_start_action(handle, context_handle):
    return SINGLETON.complete_and_start_action(handle)


def start_timer(*args, **kwargs):  # real signature unknown
    pass


def update_state(*args, **kwargs):  # real signature unknown
    print("update_state", args, kwargs)
