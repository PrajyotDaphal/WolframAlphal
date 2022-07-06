import wolframalpha
from speak import *

def wolfram(query):

    api_key = "XY8VJ7-GP8P4KG7QU"

    requester = wolframalpha.client(api_key)

    requested = requester.query(query)

    try:
        Answer = next(requested.results).text

        return Answer

    except:
        speak("An String Value is Not Answerable")

wolfram()
