import tkinter as tk

# Quiz questions and answers
quiz_data = [
    {
        "question": "What is the capital of France?",
        "options": ["Paris", "Berlin", "Madrid", "Rome"],
        "correct_option": 0
    },
    {
        "question": "What is the largest planet in our solar system?",
        "options": ["Earth", "Jupiter", "Mars", "Venus"],
        "correct_option": 1
    },
    {
        "question": "How many continents are there on Earth?",
        "options": ["4", "5", "6", "7"],
        "correct_option": 3
    }
]

# Initialize variables
current_question = 0
score = 0

# Function to check the answer
def check_answer():
    global current_question, score
    selected_option = var.get()
    if selected_option == quiz_data[current_question]["correct_option"]:
        score += 1
    if current_question < len(quiz_data) - 1:
        current_question += 1
        next_question()
    else:
        result_label.config(text=f"You scored {score}/{len(quiz_data)}")
        for button in option_buttons:
            button.config(state=tk.DISABLED)
        submit_button.config(state=tk.DISABLED)

# Function to move to the next question
def next_question():
    question_label.config(text=quiz_data[current_question]["question"])
    var.set(-1)  # Clear the selection
    for i, option in enumerate(option_buttons):
        option_labels[i].config(text=quiz_data[current_question]["options"][i])

# Create a GUI window
window = tk.Tk()
window.title("Quiz Application")

# Create and configure widgets
question_label = tk.Label(window, text=quiz_data[current_question]["question"])
question_label.pack()

option_buttons = []
option_labels = []
var = tk.IntVar()

for i in range(4):  # Create 4 option buttons
    option_buttons.append(tk.Radiobutton(window, variable=var, value=i))
    option_labels.append(tk.Label(window, text="", wraplength=300))  # Set wraplength for better display
    option_buttons[i].pack()
    option_labels[i].pack()

submit_button = tk.Button(window, text="Submit", command=check_answer)
submit_button.pack()

result_label = tk.Label(window, text="")
result_label.pack()

next_button = tk.Button(window, text="Next", command=next_question)
next_button.pack()

next_question()  # Initialize the first question

# Start the GUI main loop
window.mainloop()
