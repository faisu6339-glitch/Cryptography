q=["hello","how are you","what is your name?","tell me a joke","goodbye"]
a=["Hi there!","I'm doing well, thank you! How can I assist you?","I am ChatGPT', 'your virtual assistant.','Why did the scarecrow win an award? Because he was outstanding in his field!","Goodbye! Have a great day!"]

while True:
    user_input=input("You: ").lower()
    if user_input in ["exit","quit","bye"]:
        print(" Goodbye! Have a great day!")
        break
    if user_input in q:
        index=q.index(user_input)
        print("ChatGPT: "+a[index])
    else:
     print("Bot says:",user_input)
        