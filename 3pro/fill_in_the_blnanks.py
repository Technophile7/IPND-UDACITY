# IPND Stage 2 Final Project

#the questions for easy level
easy_ques ="The name of this project is __1__ .The coding language used in this project is __2__ .The first project used __3__ langusge.the last lesson is to __4__ your path"

#the questions for medium level
medium_ques="The name of the star player of The REAL MADRID(football) is __1__ .The __2__ is the star player of BARCELONA(football). __3__ is the captain of INDIAN CRICKET TEAM(2018).M.S.Dhoni is the wicket __4__ of india"
#the questions for tough level
tough_ques=" __1__ is the fourth planet of our solar system.our solar system has __2__ no. of planets(pluto excluded).The name of our galaxy is __3__ .Earth is placed after __4__ in our solar system  "
#the list of answers of the questions of easy level 
easy_ans=["madlib","python","html","discover"]
#the list of answers for the questions of medium level
medium_ans=["ronaldo","messi","virat","keeper"]
#the list of answers for the questions of tough level
tough_ans=["mars","eight","milkiway","venus"]

#method that generates the questions according to the level/mode selected by user
def mode(level):
    if(level=="easy"):
       print easy_ques
       print "\n"
       main(easy_ques,easy_ans)
    else:
        if(level=="medium"):
            print medium_ques
            print"\n"
            main(medium_ques,medium_ans)
        else:
            if(level=="tough"):
                print tough_ques
                print"\n"
                main(tough_ques,tough_ans)
            else:
                print "sorry!!! wrong input please fill the appropriate option \n"
                run()
#the main method that takes question and answers as input and ask the user to input value to fill in the blank and checks whether the ans is correct or not
def main(ques,ans):
    iteration=0
    while iteration<=len(ans):
        location="__"+str(iteration+1)+"__"
        if location in ques:
            user_input=raw_input("what is the true answer of"+location)
            if user_input == ans[iteration]:
                ques=ques.replace(location,user_input)
                print ques
            else:
                user_input=raw_input(" wrong ans plzz try again (last try)   what is the true answer of"+location)
                if user_input == ans[iteration]:
                    ques=ques.replace(location,user_input)
                    print ques
                else:
                    print "srry u again answered wrong move to next ques"
        iteration=iteration+1
    return gameover()
#method that tells the user that the game is over
def gameover():
    print "CONGRATULATIONS!!! \n Game Over "


#welcomes the user and prompts the user to select the difficulty level of the game 
def run():
    print"hey!!! \n wassup!"
    print "welcome !!! \n  select your level \n  1>easy  2>medium  3>tough"
    level=raw_input("input now")
    mode(level)
#to execute the run method
run()



