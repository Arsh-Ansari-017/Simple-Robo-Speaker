import win32com.client

speaker = win32com.client.Dispatch("SAPI.SpVoice")

print("You're welcome to RoboSpeaker 2.0 - Created by Arsh Ansari")
print("I will help you to make your words into voice just type what you want me to say or type 'null' to exit ")

while True:
    x = input("Enter the words you want me to say: ").strip()
    if x.lower() == "null":
        print("Exiting roboSpeaker.")
        break
    speaker.Speak(x)

