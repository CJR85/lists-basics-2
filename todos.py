
header = """  _____         _           
  _____         _           
 |_   _|__   __| | ___  ___ 
   | |/ _ \ / _` |/ _ \/ __|
   | | (_) | (_| | (_) \__ \\
   |_|\___/ \__,_|\___/|___/
                            

"""
print(header)

todos = []
while True:
    for i in range(len(todos)):
        print(f"{i+1}) {todos[i]}")

    print("***********************************")
    print("Enter a command. Type 'h' for help:")
    command = input("> ")
    if command == 'q':
        break
    elif command.isnumeric():
        idx = int(command) -1
        if idx >= len(todos):
          print("THER IS NO TODO WITH THAT NUMBER!")
        else:
          todos.pop(idx)
    else:
        todos.append(command)
    # Print todos from list 
print("OK. GOODBYE!")   