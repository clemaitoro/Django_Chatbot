import random
import string
import requests
msg=None
key="b8d2833625b34875bea184542241004"
def bot_response(message):
    global msg  

    normalized_message = message.lower()

    if normalized_message == msg:
        return "STOP REPEATING YOURSELF!"
    msg = normalized_message
    if normalized_message == "hello":
        return "Hello there, human!"
    elif normalized_message == "goodbye":
        return "I am dead."
    elif normalized_message == "gimme image":
        random_id = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
        return f'<img src="https://picsum.photos/200/300?id={random_id}" alt="Random Image">'
    elif "tell me about" in normalized_message:
        topic = normalized_message.split("tell me about", 1)[1].strip()
        return f'<a href= https://en.wikipedia.org/wiki/{topic}> Wikipedia article about {topic} </a>'
    elif "weather in" in normalized_message:
        words = message.split()
        last_word = words[2] if len(words) > 1 else None
        url = f"http://api.weatherapi.com/v1/current.json?key=b8d2833625b34875bea184542241004&q={last_word}&aqi=no"
        url2=requests.get(url)
        data = url2.json()
        temperature = data['current']['temp_c']
        return f"Temperature in {last_word} is currently {temperature} degrees C"
    
    elif normalized_message == "help":
        return f"""
                Hi there! I'm here to help you with a few things:<br><br>

                * **Greetings:** Say "hello" and I'll greet you back.<br>
                * **Goodbyes:** Say "goodbye" and I'll respond in a (slightly dramatic) way. <br>
                * **Random Images:** Say "gimme image" and I'll show you a random image from the internet.<br>
                * **Wikipedia Lookups:** Ask me "tell me about [topic]" and I'll provide a link to the Wikipedia article for that topic. (Example: "tell me about cats")<br>
                * **Weather:** Ask me "weather in [location]" and I'll try to fetch the current temperature in Celsius for that location using an API. (Example: "weather in London")<br><br>

                **Note:** I'm still under development, so I might not understand everything or always have the right information. But I'm learning and improving all the time!
                """
    else:
        return "I do not understand."