katz_deli = ["mary", "john"]

# FUNC line()
# Build the line() function that shows everyone their current place in the line. If there is nobody in line, it should say "The line is currently empty.".

def line(arr: list) -> str:
    print("The line is currently empty.") if len(arr) == 0 else print("The line is currently: " +" ".join([f"{index + 1}. {person}" for index,person in enumerate(arr) ]))

# FUNC take_a_number()
# Build a function that a new customer will use when entering the deli. The take_a_number() function should accept two arguments, the list for the current line of 
# people (katz_deli), and a string containing the name of the person joining the end of the line. The function should call out (i.e., print) the person's name along with their position in line.
## Top-Tip: Remember that people like to count from 1, not from 0 like computers.
def take_a_number(arr: list, name: str) -> str:
    arr.append(name)
    print(f"Welcome, {name}. You are number {arr.index(name) + 1} in line.")
    
# FUNC now_serving()
# Build the now_serving() function which should call out (print) the next person in line and then remove them from the front. If there is nobody in line, it 
# should call out (print) that "There is nobody waiting to be served!".
def now_serving(arr: list):
    print(f"Currently serving {arr.pop(0)}.") if len(arr) > 0 else print("There is nobody waiting to be served!")
    
if __name__ == "__main__":
    # print(take_a_number(katz_deli, "Jerry Smith"))
    # print(now_serving())
    print(line([]))
    print(take_a_number(katz_deli, "Morty"))
    print(now_serving(katz_deli))