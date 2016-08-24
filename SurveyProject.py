
question_one = raw_input("How was your first day of programming? (Bad, Good, Excellent): ")
question_two = raw_input("Are you excited to continue onto the next lesson? (Yes, No): ")
question_three = raw_input("Was the atmosphere pleasant for learning? (Yes, Bad): ")
question_four = raw_input("Did you have any programming experience befor? (Yes, No): ")
question_five = raw_input("Please supply any additional comments you have: ")
print ""
print ""
print "Your answers are "
print "How was your first day of programming? (Bad, Good, Excellent): " + question_one
print "Are you excited to continue onto the next lesson? (Yes, No): " + question_two
print "Was the atmosphere pleasant for learning? (Yes, Bad): " + question_three
print "Did you have any programming experience befor? (Yes, No): " + question_four
print "Please supply any additional comments you have: " + question_five
print ""
qustion_six = input("Please confirm your answers (Press 1 for Yes or Press 2 for NO): ")

if qustion_six == 1 :
                print ""
                print "Thank you for your valuable time"
elif qustion_six == 2 :
                print ""
                print "Please start again, Thank You"
