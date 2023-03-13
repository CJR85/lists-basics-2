
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
    for todos in todos:
        print(f"* {todos}")
    print("***********************************")
    print("Enter a command. Type 'h' for help:")
    command = input("> ")
    if command == 'q':
        break
    else:
        todos.append(command)
    # Print todos from list 
print("OK. GOODBYE!")   