import json

def send_to_server(data2send, s):
    data2send = json.dumps(data2send).encode()
    s.sendall(len(data2send).to_bytes(4, "little"))
    s.sendall(data2send)


def receive_from_server(s):
    rcv_size = int.from_bytes(s.recv(4), 'little')
    msg = json.loads(s.recv(rcv_size).decode())
    return msg


def send_anchor_info(anchor, s):
    data2send = anchor
    data2send["type"] = "new_anchor"
    send_to_server(data2send, s)


def send_relate_to_masters(s):
    data2send = {}
    data2send["type"] = "relate_to_masters"
    send_to_server(data2send, s)


def send_rf_config(rf_params, s):
    data2send = rf_params
    data2send["type"] = "rf_config"
    send_to_server(data2send, s)


def send_start(s):
    data2send = {}
    data2send["type"] = "Start"
    send_to_server(data2send, s)


def send_stop(s):
    data2send = {}
    data2send["type"] = "Stop"
    send_to_server(data2send, s)


def send_get_anchors(s):
    data2send = {}
    data2send["type"] = 'get_anchors'
    send_to_server(data2send, s)


def send_get_tags(s):
    data2send = {}
    data2send["type"] = 'get_tags'
    send_to_server(data2send, s)


def send_state_request(s):
    data2send = {}
    data2send["type"] = 'state_request'
    send_to_server(data2send, s)

def send_disconnect(s):
    data2send = {}
    data2send["type"] = 'disconnect'
    send_to_server(data2send, s)

def send_log_enable(s):
    data2send = {}
    data2send["type"] = 'log_enable'
    send_to_server(data2send, s)

def send_log_disable(s):
    data2send = {}
    data2send["type"] = 'log_disable'
    send_to_server(data2send, s)

def send_accumulation_on(s, buf_len):
    data2send = {}
    data2send["type"] = 'acc_on'
    data2send["buf_len"] = buf_len
    send_to_server(data2send, s)

def send_accumulation_off(s):
    data2send = {}
    data2send["type"] = 'acc_off'
    send_to_server(data2send, s)

def send_ref_tag_state(s, state):
    data2send = {}
    data2send["type"] = 'ref_tag_state'
    data2send["state"] = state
    send_to_server(data2send, s)

def send_update_ref_tag(s, name, x, y, z):
    data2send = {}
    data2send["type"] = 'update_ref_tag'
    data2send["name"] = name
    data2send["x"] = x
    data2send["y"] = y
    data2send["z"] = z
    send_to_server(data2send, s)

def send_update_tag_hei(s, h):
    data2send = {}
    data2send["type"] = 'update_tag_hei'
    data2send["h"] = h
    send_to_server(data2send, s)

