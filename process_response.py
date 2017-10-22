import random
import MySQLdb as mdb
from twilio.twiml.messaging_response import MessagingResponse
from userStates import OFF, NEW_USER, ADDING_USER, EXISTING_USER, CATEGORY_INPUT, GETTING_CATEGORY
from db_functions import set_user_state, add_user, get_scores, user_exists
from report_generator import PHENOTYPES

categoriesCommands = ["1", "2", "3", "4", "5"]
quitCommands = ["q", "Q", "QUIT", "quit", "Quit"]


def isNewUser(phoneNumber):
    with mdb.connect('localhost', 'root', 'toor', 'userdb') as cur:
        if not user_exists(phoneNumber, cur):
            return True
        else:
            return False


# TODO
def getPhenotypeDescription(phenotype):
    return "description"


# TODO
def getPhenotypeRecommendation(phenotype):
    return "recommendation"


def getScores(phoneNumber, phenotypes):
    with mdb.connect('localhost', 'root', 'toor', 'userdb') as cur:
        return get_scores(phoneNumber, phenotypes, cur)


def setState(phoneNumber, state):
    with mdb.connect('localhost', 'root', 'toor', 'userdb') as cur:
        set_user_state(phoneNumber, state, cur)


def addUser(phoneNumber, name):
    with mdb.connect('localhost', 'root', 'toor', 'userdb') as cur:
        add_user(phoneNumber, name, cur)


def reply(phoneNumber, body, state):
    resp = MessagingResponse()
    response = "hi"
    resp.message(response)

    if state is OFF:
        msg = "Hi there! This is Uplift’s automated chat bot responding. "\
                "I’m here to give you some useful insight about your genome as well as some tips to help you be the best you."
        resp.message(msg)
        if isNewUser(phoneNumber):
            setState(phoneNumber, NEW_USER)
        else:
            setState(phoneNumber, EXISTING_USER)
        
    elif state is NEW_USER:
        msg = "Looks like you’re a new user. What’s your name?"
        resp.message(msg)
        setState(phoneNumber, ADDING_USER)
    elif state is ADDING_USER:
        msg = "Nice to meet you, (name)."
        resp.message(msg)
        # Set name here with body
        addUser(phoneNumber, body)
        # Change state to CATEGORY INPUT
        setState(phoneNumber, CATEGORY_INPUT)
    elif state is EXISTING_USER:
        msg = "Welcome back, " + "(NAME)" + "!"
        resp.message(msg)
        # Change state to CATEGORY INPUT
        setState(phoneNumber, CATEGORY_INPUT)
    
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
        setState(phoneNumber, GETTING_CATEGORY)
    elif state is GETTING_CATEGORY:
        if body in categoriesCommands:
            # A WHOLE LOTTA SHIT HERE
            if body is "1":
                msg_1 = "Cool, you selected physical traits! Give me a second to grab your information."
                phenotypes = getScores(phoneNumber, PHENOTYPES['trait'])
                phenotype = random.choice(list(phenotypes.keys()))
                score = phenotypes[phenotype]
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
                setState(phoneNumber, GETTING_CATEGORY)
            elif body is "2":
                msg_1 = "Cool, you selected personality! Give me a second to grab your information."
                phenotypes = getScores(phoneNumber, PHENOTYPES['personality'])
                phenotype = random.choice(list(phenotypes.keys()))
                score = phenotypes[phenotype]
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
                setState(phoneNumber, GETTING_CATEGORY)
            elif body is "3":
                msg_1 = "Cool, you selected food and nutrition! Give me a second to grab your information."
                phenotypes = getScores(phoneNumber, PHENOTYPES['food_and_nutrition'])
                phenotype = random.choice(list(phenotypes.keys()))
                score = phenotypes[phenotype]
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
                setState(phoneNumber, GETTING_CATEGORY)
            elif body is "4":
                msg_1 = "Cool, you selected allergies! Give me a second to grab your information."
                phenotypes = getScores(phoneNumber, PHENOTYPES['allergy'])
                phenotype = random.choice(list(phenotypes.keys()))
                score = phenotypes[phenotype]
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
                setState(phoneNumber, GETTING_CATEGORY)
            else:
                msg_1 = "Cool, you selected diseases! Give me a second to grab your information."
                phenotypes = getScores(phoneNumber, PHENOTYPES['disease'])
                phenotype = random.choice(list(phenotypes.keys()))
                score = phenotypes[phenotype]
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
                setState(phoneNumber, GETTING_CATEGORY)
        elif body in quitCommands:
            msg = "Thanks for listening! Hope to hear from you soon :)"
            resp.message(msg)
            # Set state to OFF
            setState(phoneNumber, OFF)
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
