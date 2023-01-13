import pyjokes
joks_category = ['neutral', 'all','chuck']  # Jokes list.
def listen():
    print(f"Jokes cataegory: {joks_category}")
    print("Input 'exit' to programm terminated.") 
    return input("say joks category: ")  # Input joks category
def tell_some_jokes(command):
    command_broken = command.split()  # jokes convert list
    for word in command_broken:
        if word in joks_category:  # jokes check 
            joke = pyjokes.get_joke(language='en', category=word) 
            jokes_print(joke)  # print jokes 
            break
        else:
            jokes_print("Invalid joks category. ")  # invalid jokes list input 
            break
def jokes_print(jokes_all):
    print(f"\n{jokes_all}\n")
    
while True:
    command = listen() 
    if command =='exit':
        break
    tell_some_jokes(command)
