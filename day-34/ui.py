from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
class QuizInterface :
    def __init__(self, quiz_brain:QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        # Score label
        self.score_label = Label(text="Score: 0", fg="white", bg=THEME_COLOR, font=("Arial", 16))
        self.score_label.grid(row=0, column=1, pady=10)

        # Question canvas
        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(
            150, 125,
            text="Question goes here",
            font=("Arial", 20, "italic"),
            fill=THEME_COLOR,
            width=280,
            anchor="center"
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=20)

        # Buttons
        true_img = PhotoImage(file="images/true.png")
        false_img = PhotoImage(file="images/false.png")

        self.true_button = Button(image=true_img,command=self.user_answer_true, highlightthickness=0, bd=0, bg=THEME_COLOR)
        self.true_button.grid(row=2, column=0, pady=10)

        self.false_button = Button(image=false_img, command=self.user_answer_false, highlightthickness=0, bd=0, bg=THEME_COLOR)
        self.false_button.grid(row=2, column=1, pady=10)
        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text =self.quiz.next_question()
            self.canvas.itemconfig(self.question_text , text = q_text)
        else :
            self.canvas.itemconfig(self.question_text , text = "You Have Finished The Quiz")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")
    def user_answer_true(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def user_answer_false(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self,is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)