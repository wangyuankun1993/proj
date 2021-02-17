from survey import AnonymousSurvey

question = "What language did you first learn to speak?"
my_sruvey = AnonymousSurvey(question)

my_sruvey.show_question()
print("Enter 'q' at any time to quit.\n")
while True:
    response = input("Language:")
    if response == 'q':
        break
    my_sruvey.store_response(response)

print("\nThank you to everyone who participated in the survey!")
my_sruvey.show_results()