from speak import *
from SpeechRecognition import *
from wolfram import *

if __name__ == "__main__":
    while True:
    # if 1:
        query = Listen().lower()

     # Logic for executing tasks based on query
        if 'question' in query:
                wolfram(query)
        else:
            Say("NO Data!!!")
