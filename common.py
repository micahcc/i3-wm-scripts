#/usr/bin/env python3
import json
import subprocess
from collections import defaultdict

def get_tree():
    """return i3 container tree"""
    data = subprocess.check_output(["i3-msg", "-t", "get_tree"])
    data = json.loads(data.decode("UTF-8"))
    return data

def get_named_windows():
    """return (current-id, dict of (wm-class,window-name) to list of IDs)"""
    i3_tree = get_tree()
    assert i3_tree["name"] == "root", i3_tree["name"]
    queue = [i3_tree]
    current_id = None
    data = defaultdict(list)
    while queue:
        current = queue.pop()
        if current["layout"] == "dockarea":
            continue
        nodes = current.get("nodes")
        if nodes:
            queue.extend(nodes)
            continue
        if not current["geometry"]["width"]:
            continue
        if current.get("type") != "con":
            continue
        if current.get("focused"):
            current_id = current["id"]
        key = (current["window_properties"]["class"], current["name"].strip())
        data[key].append(current["id"])
    return current_id, data

def cycle_selected(current, selected):
    """return next selected window"""
    if current in selected:
        selected.sort()
        idx = (selected.index(current) + 1) % len(selected)
        return selected[idx]
    return selected[0]

def focus_window(id):
    subprocess.check_call(["i3-msg", "[con_id=\"{}\"] focus".format(id)])
