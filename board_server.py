import json
import os
from flask import *

app = Flask(__name__)
cwd_path = os.path.abspath(os.path.dirname(__file__))

with open(cwd_path + "/defaults.json") as fp:
		defaults = json.load(fp)

def hex_to_rgb(hex_code):
    hex_code = hex_code.lstrip('#')
    return [int(hex_code[i:i+2], 16) for i in (0, 2, 4)]
    
def rgb_to_hex(r, g, b):
    return '#{:02x}{:02x}{:02x}'.format(r, g, b)

@app.route("/")
def index():
	with open(cwd_path + "/messages.json") as fp:
		messages = json.load(fp)
		
	for message in messages:
		if "color" in message:
			message["color"] = rgb_to_hex(*message["color"])
		else:
			message["color"] = rgb_to_hex(*defaults["color"])
	return render_template(
		"index.html",
		defaults=defaults,
		messages=messages
	)

@app.route("/appendMessage", methods=["POST"])
def appendMessage():
	message = request.form["message"]
	color= request.form["color"]

	with open(cwd_path + "/messages.json") as fp:
		messages = json.load(fp)
	
	messages.append({ "message": message, "color": hex_to_rgb(color)})
	with open(cwd_path + "/messages.json", "w") as fp:
		json.dump(messages, fp)
	
	return redirect("/")
	
@app.route("/moveMessage")
def moveMessage():
	args = request.args.to_dict()
	index, direction = int(args["index"]), args["direction"]
	
	with open(cwd_path + "/messages.json") as fp:
		messages = json.load(fp)
		
	if (index == 0 and direction == "up") or (index == len(messages) - 1 and direction == "down"):
		return redirect("/")
	
	print(messages)
	msg = messages.pop(index)
	print(messages)
	if direction == "up":
		messages = messages[:index - 1] + [msg] + messages[index - 1:]
	elif direction == "down":
		messages = messages[:index + 1] + [msg] + messages[index + 1:] 
		
	with open(cwd_path + "/messages.json", "w") as fp:
		json.dump(messages, fp)
		
	return redirect("/")
	
@app.route("/updateColor")
def updateColor():
	args = request.args.to_dict()
	index, color = int(args["index"]), hex_to_rgb(args["color"])
	
	print(index, color)
	
	with open(cwd_path + "/messages.json") as fp:
		messages = json.load(fp)
		
	messages[index]["color"] = color
	
	with open(cwd_path + "/messages.json", "w") as fp:
		json.dump(messages, fp)
		
	return redirect("/")
	
@app.route("/deleteMessage")
def deleteMessage():
	args = request.args.to_dict()
	index = int(args["index"])

	with open(cwd_path + "/messages.json") as fp:
		messages = json.load(fp)
	
	rm_message = messages.pop(index)
	with open(cwd_path + "/messages.json", "w") as fp:
		json.dump(messages, fp)
		
	return redirect("/")

if __name__ == "__main__":
	app.run(host="0.0.0.0")
