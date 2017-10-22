<<<<<<< HEAD
from twilio.twiml.messaging_response import MessagingResponse
from userStates import OFF, NEW_USER, ADDING_USER, EXISTING_USER, CATEGORY_INPUT, GETTING_CATEGORY

categoriesCommands = ["1", "2", "3", "4", "5"]
quitCommands = ["q", "Q", "QUIT", "quit", "Quit"]

def reply(phoneNumber, body, state):
    resp = MessagingResponse()
    response = "hi"
    resp.message(response)

    if state is OFF:
        msg = "Hi there! This is Uplift’s automated chat bot responding. "\
                "I’m here to give you some useful insight about your genome as well as some tips to help you be the best you."
        resp.message(msg)
        if isNewUser(phoneNumber):
            # Change state to NEW USER
        else:
            # Change state to EXISTING USER
        
    elif state is NEW_USER:
        msg = "Looks like you’re a new user. What’s your name?"
        resp.message(msg)
        # Change state to ADDING USER
    elif state is ADDING_USER:
        msg = "Nice to meet you, (name)."
        resp.message(msg)
        # Set name here with body

        # Change state to CATEGORY INPUT
    elif state is EXISTING_USER:
        msg = "Welcome back, " + "(NAME)" + "!"
        resp.message(msg)
        # Change state to CATEGORY INPUT
    
    elif state is CATEGORY_INPUT:
        msg = "What would you like to learn about today? Here are some commands you can reply with to learn more about your phenotypes:"\
                "\n“1” to learn about your physical traits"\
                "\n“2” to learn about your personality"\
                "\n“3” to learn about your food and nutrition"\
                "\n“4” to learn about your allergies"\
                "\n“5” to learn about your diseases"\
                "\n“q or quit” to leave the conversation"
        resp.message(msg)
        # Change state to GETTING CATEGORY
    elif state is GETTING_CATEGORY:
        if body in categoriesCommands:
            # A WHOLE LOTTA SHIT HERE
            if body is "1":
                msg_1 = "Cool, you selected physical traits! Give me a second to grab your information."
                profile = UserProfile('european', 'traits')
                phenotype = getPhenotype(profile)
                msg_2 = "Here's an interesting one: " + phenotype
                msg_3 = getPhenotypeDescription()
                msg_4 = getPhenotypeRecommendation()
                msg_5 = "Would you like to learn more about your phenotypes?"\
                    "\n“1” to learn about your physical traits"\
                    "\n“2” to learn about your personality"\
                    "\n“3” to learn about your food and nutrition"\
                    "\n“4” to learn about your allergies"\
                    "\n“5” to learn about your diseases"\
                    "\n“q or quit” to leave the conversation"
                resp.message(msg_1)
                resp.message(msg_2)
                resp.message(msg_3)
                resp.message(msg_4)
                resp.message(msg_5)
                # Set state to GETTING_CATEGORY
            elif body is "2":
                msg_1 = "Cool, you selected personality! Give me a second to grab your information."
                profile = UserProfile('european', 'personality')
                phenotype = getPhenotype(profile)
                msg_2 = "Here's an interesting one: " + phenotype
                msg_3 = getPhenotypeDescription()
                msg_4 = getPhenotypeRecommendation()
                msg_5 = "Would you like to learn more about your phenotypes?"\
                    "\n“1” to learn about your physical traits"\
                    "\n“2” to learn about your personality"\
                    "\n“3” to learn about your food and nutrition"\
                    "\n“4” to learn about your allergies"\
                    "\n“5” to learn about your diseases"\
                    "\n“q or quit” to leave the conversation"
                resp.message(msg_1)
                resp.message(msg_2)
                resp.message(msg_3)
                resp.message(msg_4)
                resp.message(msg_5)
                # Set state to GETTING_CATEGORY
            elif body is "3":
                msg_1 = "Cool, you selected food and nutrition! Give me a second to grab your information."
                profile = UserProfile('european', 'food_and_nutrition')
                phenotype = getPhenotype(profile)
                msg_2 = "Here's an interesting one: " + phenotype
                msg_3 = getPhenotypeDescription()
                msg_4 = getPhenotypeRecommendation()
                msg_5 = "Would you like to learn more about your phenotypes?"\
                    "\n“1” to learn about your physical traits"\
                    "\n“2” to learn about your personality"\
                    "\n“3” to learn about your food and nutrition"\
                    "\n“4” to learn about your allergies"\
                    "\n“5” to learn about your diseases"\
                    "\n“q or quit” to leave the conversation"
                resp.message(msg_1)
                resp.message(msg_2)
                resp.message(msg_3)
                resp.message(msg_4)
                resp.message(msg_5)
                # Set state to GETTING_CATEGORY
            elif body is "4":
                msg_1 = "Cool, you selected allergies! Give me a second to grab your information."
                profile = UserProfile('european', 'allergies')
                phenotype = getPhenotype(profile)
                msg_2 = "Here's an interesting one: " + phenotype
                msg_3 = getPhenotypeDescription()
                msg_4 = getPhenotypeRecommendation()
                msg_5 = "Would you like to learn more about your phenotypes?"\
                    "\n“1” to learn about your physical traits"\
                    "\n“2” to learn about your personality"\
                    "\n“3” to learn about your food and nutrition"\
                    "\n“4” to learn about your allergies"\
                    "\n“5” to learn about your diseases"\
                    "\n“q or quit” to leave the conversation"
                resp.message(msg_1)
                resp.message(msg_2)
                resp.message(msg_3)
                resp.message(msg_4)
                resp.message(msg_5)
                # Set state to GETTING_CATEGORY
            else:
                msg_1 = "Cool, you selected diseases! Give me a second to grab your information."
                profile = UserProfile('european', 'diseases')
                phenotype = getPhenotype(profile)
                msg_2 = "Here's an interesting one: " + phenotype
                msg_3 = getPhenotypeDescription()
                msg_4 = getPhenotypeRecommendation()
                msg_5 = "Would you like to learn more about your phenotypes?"\
                    "\n“1” to learn about your physical traits"\
                    "\n“2” to learn about your personality"\
                    "\n“3” to learn about your food and nutrition"\
                    "\n“4” to learn about your allergies"\
                    "\n“5” to learn about your diseases"\
                    "\n“q or quit” to leave the conversation"
                resp.message(msg_1)
                resp.message(msg_2)
                resp.message(msg_3)
                resp.message(msg_4)
                resp.message(msg_5)
                # Set state to GETTING_CATEGORY
        elif body in quitCommands:
            msg = "Thanks for listening! Hope to hear from you soon :)"
            resp.message(msg)
            # Set state to OFF
        else:
            msg_1 = "Hmm... I don’t recognize that command."
            msg_2 = "Here are some commands you can reply with to learn more about your phenotypes:"\
                "\n“1” to learn about your physical traits"\
                "\n“2” to learn about your personality"\
                "\n“3” to learn about your food and nutrition"\
                "\n“4” to learn about your allergies"\
                "\n“5” to learn about your diseases"\
                "\n“q or quit” to leave the conversation"
            resp.message(msg_1)
            resp.message(msg_2)        
    return str(resp)

# TODO
def isNewUser(phoneNumber):
    # Check database here and set STATE
    # If STATE != OFF, set it to STATE
    # else STATE = EXISTING USER
    return False

# TODO
def getPhenotype(profile):
    return "cool"

# TODO
def getPhenotypeDescription(phenotype):
    return "description"

# TODO
def getPhenotypeRecommendation(phenotype):
    return "recommendation"
