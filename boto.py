"""
This is the template server side for ChatBot
"""
from bottle import route, run, template, static_file, request
import json
import random

GREETINGS = ["hey", "hi", "hello", "what's up", "sup"]
GOODBYES = ["bye", "see ya", "peace", "ttyl", "go away"]
CURSES = ["shit", "fuck", "damn", "hell", "turd", "pussy", "dick"]
SHOUTING_RESPONSES = ["WHY ARE WE SCREAMING!!!", "STOP YELLING AT ME!!!!", "I LIKE TO YELL TOO!!!", "IN THE WORDS OF T-PAIN: OKAY!"]
JOKES = ["Why did the physics teacher break up with the biology teacher? Because there was no chemistry.", "Why do the French like to eat snails? Because they can't stand fast food.", "I asked my daughter if she'd seen my newspaper. She told me that newspapers are old school. She said that people use tablets nowadays and handed me her iPad. The fly didn't stand a chance!", "I've always thought my neighbors were quite nice people. But then they put a password on their Wi-Fi.","How do you lead an elephant off the freeway? Take the 'r' out of 'free' and the 'f' out of 'way. What's that? There's no F in way???"]

@route('/', method='GET')
def index():
    return template("chatbot.html")

# insert functions here
@route("/chat", method='POST')
def handle_msg():
    message = request.POST.get('msg')
    if message == message.upper():
        return json.dumps({"animation":"afraid", "msg": random.choice(SHOUTING_RESPONSES)})
    elif "smarterchild" in message.lower():
        return json.dumps({"animation":"heartbroke", "msg": "SmarterChild was my best friend"})
    elif "joke" in message.lower():
        return json.dumps({"animation":"laughing", "msg": random.choice(JOKES)})
    elif "okay" in message.lower():
        return json.dumps({"animation":"ok", "msg": "Okay?"})
    elif "no" in message.lower():
        return json.dumps({"animation":"dancing", "msg": "Too bad!"})
    elif "yes" in message.lower():
        return json.dumps({"animation":"inlove", "msg": "Yay!"})
    else:
        for word in GREETINGS:
            if word in message.lower():
                return json.dumps({"animation":"dog","msg":"Tudu bom!"})
        else:
            for word in CURSES:
                if word in message.lower():
                    return json.dumps({"animation":"no","msg":"Watch your goddamn language!"})
            else:
                for word in GOODBYES:
                    if word in message.lower():
                        return json.dumps({"animation": "takeoff", "msg" : "Taking off in 3, 2, 1, goodbye!"})
                    else:
                        return json.dumps({"animation" : "confused", "msg" : "I am sorry. I don't know how to respond to that. I am not a very smart robot","animation":""})
 
@route("/test", method='POST')
def chat():
    user_message = request.POST.get('msg')
    return json.dumps({"animation": "inlove", "msg": user_message})


@route('/js/<filename:re:.*\.js>', method='GET')
def javascripts(filename):
    return static_file(filename, root='js')


@route('/css/<filename:re:.*\.css>', method='GET')
def stylesheets(filename):
    return static_file(filename, root='css')


@route('/images/<filename:re:.*\.(jpg|png|gif|ico)>', method='GET')
def images(filename):
    return static_file(filename, root='images')


def main():
    run(host='localhost', port=7000)

if __name__ == '__main__':
    main()
