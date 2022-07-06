import wolframalpha
from speak import *

def wolfram(query):

    api_key = " YourApiID "

    requester = wolframalpha.client(api_key)

    requested = requester.query(query)

    try:
        Answer = next(requested.results).text

        return Answer

    except:
        speak("An String Value is Not Answerable")

wolfram()
