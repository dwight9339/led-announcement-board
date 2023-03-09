#!/usr/bin/env python
import json
import os
from signcontroller import SignController

if __name__ == "__main__":
	cwd_path = os.path.abspath(os.path.dirname(__file__))
	ctlr = SignController()
	with open(cwd_path + "/defaults.json") as fp:
		defaults = json.load(fp)
		
	while True:
		with open(cwd_path + "/messages.json") as fp:
			messages = json.load(fp)
		
		if not messages:
			messages = [{"message": "No messages..."}]
			
		for message in messages:
			anim_type = defaults["animation"] if "animation" not in message else message["animation"]
			msg_font = defaults["font"] if "font" not in message else message["font"]
			msg_color = defaults["color"] if "color" not in message else message["color"]
			msg_speed = defaults["speed"] if "speed" not in message else message["speed"]
			msg_repeat = defaults["repeat"] if "repeat" not in message else message["repeat"]
			msg_hold_time = defaults["hold_time"] if "hold_time" not in message else message["hold_time"]
			
			if anim_type == "fly_in_top":
				ctlr.flyInTop(
					message["message"],
					msg_font,
					msg_color,
					msg_speed,
					msg_hold_time
				)
			elif anim_type == "fly_in_bottom":
				ctlr.flyInBottom(
					message["message"],
					msg_font,
					msg_color,
					msg_speed,
					msg_hold_time
				)
			else:
				ctlr.scrollRL(
					message["message"],
					msg_font,
					msg_color,
					msg_speed,
					msg_repeat
				)
			ctlr.reset()
