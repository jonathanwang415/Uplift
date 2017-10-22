import random
import MySQLdb as mdb
from collections import OrderedDict
from twilio.twiml.messaging_response import MessagingResponse
from userStates import OFF, NEW_USER, ADDING_USER, EXISTING_USER, CATEGORY_INPUT, GETTING_CATEGORY
from db_functions import  set_user_name, set_user_state, get_user_state, add_user, get_score, get_scores, user_exists, num_suggestions, get_suggestions
from report_generator import PHENOTYPES, login
from send_sms import send_message

login()

categoriesCommands = ["1", "2", "3", "4", "5", "6"]
quitCommands = ["q", "Q", "QUIT", "quit", "Quit"]


def isNewUser(phoneNumber):
    with mdb.connect('localhost', 'root', 'toor', 'userdb') as cur:
        if not user_exists(phoneNumber, cur):
            return True
        else:
            return False


def getPhenotypeDescription(phoneNumber, phenotype):
    with mdb.connect('localhost', 'root', 'toor', 'userdb') as cur:
        score_str = ''
        score = int(get_score(phoneNumber, phenotype, cur)[phenotype])
        if score == 0:
            score_str = 'zero'
        elif score == 1:
            score_str = 'one'
        elif score == 2:
            score_str = 'two'
        elif score == 3:
            score_str = 'three'
        elif score == 4:
            score_str = 'four'
        else:
            return 'No description'
        query = 'SELECT {} FROM {} WHERE phenotype_name=\'{}\';'
        if phenotype in PHENOTYPES['disease']:
            query = query.format(score_str, 'disease', phenotype.replace('-', '_'))
        elif phenotype in PHENOTYPES['food_and_nutrition']:
            query = query.format(score_str, 'foodnutrition', phenotype.replace('-', '_'))
        elif phenotype in PHENOTYPES['personality']:
            query = query.format(score_str, 'personality', phenotype.replace('-', '_'))
        else:
            return 'No description'
        cur.execute(query)
        try:
            return cur.fetchone()[0]
        except TypeError:
            return 'No description'


def getPhenotypeRecommendation(phenotype):
    with mdb.connect('localhost', 'root', 'toor', 'userdb') as cur:
        if num_suggestions(phenotype, cur):
            return random.choice(get_suggestions(phenotype, cur))
        else:
            return 'No recommendations yet..'


def getScores(phoneNumber, phenotypes):
    with mdb.connect('localhost', 'root', 'toor', 'userdb') as cur:
        return get_scores(phoneNumber, phenotypes, cur)


def getState(phoneNumber):
    with mdb.connect('localhost', 'root', 'toor', 'userdb') as cur:
        state = get_user_state(phoneNumber, cur)
        if state is not None:
            return str(state)


def setState(phoneNumber, state):
    with mdb.connect('localhost', 'root', 'toor', 'userdb') as cur:
        set_user_state(phoneNumber, state, cur)


def addUser(phoneNumber, name):
    with mdb.connect('localhost', 'root', 'toor', 'userdb') as cur:
        add_user(phoneNumber, name, cur)
        set_user_state(phoneNumber, ADDING_USER, cur)


def setName(phoneNumber, name):
    with mdb.connect('localhost', 'root', 'toor', 'userdb') as cur:
        set_user_name(phoneNumber, name, cur)


def reply(phoneNumber, body, state):
    if state == OFF:
        msg = ("Hi there! This is Uplift’s automated chat bot responding. "
               "I’m here to give you some useful insight about your genome as well as some tips to help you be the best you.")
        send_message(msg, phoneNumber)
        setState(phoneNumber, EXISTING_USER)
        # if isNewUser(phoneNumber):
        #     state = NEW_USER
        # else:
        #     state = getState(phoneNumber)
        # reply(phoneNumber, body, state)
    elif state == NEW_USER:
        msg = "Looks like you’re a new user. What’s your name?"
        send_message(msg, phoneNumber)
        addUser(phoneNumber, 'NULL')
        setState(phoneNumber, ADDING_USER)
    elif state == ADDING_USER:
        msg = "Nice to meet you, " + body +"."
        send_message(msg, phoneNumber)
        # Set name here with body
        setName(phoneNumber, body)
        # Change state to CATEGORY INPUT
        setState(phoneNumber, CATEGORY_INPUT)
        return reply(phoneNumber, body, CATEGORY_INPUT)
    elif state == EXISTING_USER:
        msg = "Welcome back!"
        send_message(msg, phoneNumber)
        # Change state to CATEGORY INPUT
        setState(phoneNumber, CATEGORY_INPUT)
    elif state == CATEGORY_INPUT:
        msg = "What would you like to learn about today? Here are some commands you can reply with to learn more about your phenotypes:"\
                "\n“1” to learn about your physical traits"\
                "\n“2” to learn about your personality"\
                "\n“3” to learn about your food and nutrition"\
                "\n“4” to learn about your allergies"\
                "\n“5” to learn about your diseases"\
                "\n“q or quit” to leave the conversation"
        send_message(msg, phoneNumber)
        # Change state to GETTING CATEGORY
        setState(phoneNumber, GETTING_CATEGORY)
    elif state == GETTING_CATEGORY:
        if body in categoriesCommands:
            # A WHOLE LOTTA SHIT HERE
            if body == "1":
                msg_1 = "Cool, you selected physical traits! Give me a second to grab your information."
                phenotypes = getScores(phoneNumber, PHENOTYPES['trait'])
                phenotype = random.choice(list(phenotypes.keys()))
                score = phenotypes[phenotype]
                msg_2 = "Here's an interesting one: " + phenotype
                msg_3 = getPhenotypeDescription(phoneNumber, phenotype)
                msg_4 = getPhenotypeRecommendation(phenotype)
                msg_5 = "Would you like to learn more about your phenotypes?"\
                    "\n“1” to learn about your physical traits"\
                    "\n“2” to learn about your personality"\
                    "\n“3” to learn about your food and nutrition"\
                    "\n“4” to learn about your allergies"\
                    "\n“5” to learn about your diseases"\
                    "\n“q or quit” to leave the conversation"
                send_message(msg_1, phoneNumber)
                send_message(msg_2, phoneNumber)
                send_message(msg_3, phoneNumber)
                send_message(msg_4, phoneNumber)
                send_message(msg_5, phoneNumber)
                # Set state to GETTING_CATEGORY
                setState(phoneNumber, GETTING_CATEGORY)
            elif body == "2":
                msg_1 = "Cool, you selected personality! Give me a second to grab your information."
                phenotypes = getScores(phoneNumber, PHENOTYPES['personality'])
                phenotype = random.choice(list(phenotypes.keys()))
                score = phenotypes[phenotype]
                msg_2 = "Here's an interesting one: " + phenotype
                msg_3 = getPhenotypeDescription(phoneNumber, phenotype)
                msg_4 = getPhenotypeRecommendation(phenotype)
                msg_5 = "Would you like to learn more about your phenotypes?"\
                    "\n“1” to learn about your physical traits"\
                    "\n“2” to learn about your personality"\
                    "\n“3” to learn about your food and nutrition"\
                    "\n“4” to learn about your allergies"\
                    "\n“5” to learn about your diseases"\
                    "\n“q or quit” to leave the conversation"
                send_message(msg_1, phoneNumber)
                send_message(msg_2, phoneNumber)
                send_message(msg_3, phoneNumber)
                send_message(msg_4, phoneNumber)
                send_message(msg_5, phoneNumber)
                # Set state to GETTING_CATEGORY
                setState(phoneNumber, GETTING_CATEGORY)
            elif body == "3":
                msg_1 = "Cool, you selected food and nutrition! Give me a second to grab your information."
                phenotypes = getScores(phoneNumber, PHENOTYPES['food_and_nutrition'])
                phenotype = random.choice(list(phenotypes.keys()))
                score = phenotypes[phenotype]
                msg_2 = "Here's an interesting one: " + phenotype
                msg_3 = getPhenotypeDescription(phoneNumber, phenotype)
                msg_4 = getPhenotypeRecommendation(phenotype)
                msg_5 = "Would you like to learn more about your phenotypes?"\
                    "\n“1” to learn about your physical traits"\
                    "\n“2” to learn about your personality"\
                    "\n“3” to learn about your food and nutrition"\
                    "\n“4” to learn about your allergies"\
                    "\n“5” to learn about your diseases"\
                    "\n“q or quit” to leave the conversation"
                send_message(msg_1, phoneNumber)
                send_message(msg_2, phoneNumber)
                send_message(msg_3, phoneNumber)
                send_message(msg_4, phoneNumber)
                send_message(msg_5, phoneNumber)
                # Set state to GETTING_CATEGORY
                setState(phoneNumber, GETTING_CATEGORY)
            elif body == "4":
                msg_1 = "Cool, you selected allergies! Give me a second to grab your information."
                phenotypes = getScores(phoneNumber, PHENOTYPES['allergy'])
                phenotype = random.choice(list(phenotypes.keys()))
                score = phenotypes[phenotype]
                if score == 0:
                    severity = 'a very low risk'
                elif score == 1:
                    severity = 'a low risk'
                elif score == 2:
                    severity = 'an intermediate risk'
                elif score == 3:
                    severity = 'a significant risk'
                elif score == 4:
                    severity = 'a high risk'
                else:
                    severity = ''
                msg_2 = "Here's an interesting one: " + phenotype
                msg_3 = 'You have ' + severity + ' of suffering from ' + phenotype + '.'
                msg_4 = "Would you like to learn more about your phenotypes?"\
                    "\n“1” to learn about your physical traits"\
                    "\n“2” to learn about your personality"\
                    "\n“3” to learn about your food and nutrition"\
                    "\n“4” to learn about your allergies"\
                    "\n“5” to learn about your diseases"\
                    "\n“q or quit” to leave the conversation"
                send_message(msg_1, phoneNumber)
                send_message(msg_2, phoneNumber)
                send_message(msg_3, phoneNumber)
                send_message(msg_4, phoneNumber)
                # Set state to GETTING_CATEGORY
                setState(phoneNumber, GETTING_CATEGORY)
            elif body == '5':
                msg_1 = "Cool, you selected diseases! Give me a second to grab your information."
                phenotypes = getScores(phoneNumber, PHENOTYPES['disease'])
                phenotype = random.choice(list(phenotypes.keys()))
                score = phenotypes[phenotype]
                msg_2 = "Here's an interesting one: " + phenotype
                msg_3 = getPhenotypeDescription(phoneNumber, phenotype)
                msg_4 = getPhenotypeRecommendation(phenotype)
                msg_5 = "Would you like to learn more about your phenotypes?"\
                    "\n“1” to learn about your physical traits"\
                    "\n“2” to learn about your personality"\
                    "\n“3” to learn about your food and nutrition"\
                    "\n“4” to learn about your allergies"\
                    "\n“5” to learn about your diseases"\
                    "\n“q or quit” to leave the conversation"
                send_message(msg_1, phoneNumber)
                send_message(msg_2, phoneNumber)
                send_message(msg_3, phoneNumber)
                send_message(msg_4, phoneNumber)
                send_message(msg_5, phoneNumber)
                # Set state to GETTING_CATEGORY
                setState(phoneNumber, GETTING_CATEGORY)
            elif body == '6':
                msg_1 = "You are most at risk for {}, {}, and {}."
                phenotypes = getScores(phoneNumber, PHENOTYPES['disease'])
                phenotypes = OrderedDict(sorted(phenotypes.items(), key=lambda t: t[1]))
                phenotypes_ = []
                scores_ = []
                for i in range(3):
                    key, val = phenotypes.popitem()
                    phenotypes_.append(key)
                    scores_.append(val)
                msg_1 = msg_1.format(phenotypes_[0], phenotypes_[1], phenotypes_[2])
                msg_2 = getPhenotypeDescription(phoneNumber, phenotypes_[0])
                msg_3 = getPhenotypeDescription(phoneNumber, phenotypes_[1])
                msg_4 = getPhenotypeDescription(phoneNumber, phenotypes_[2])
                msg_5 = getPhenotypeRecommendation(phenotypes_[0])
                msg_6 = getPhenotypeRecommendation(phenotypes_[1])
                msg_7 = getPhenotypeRecommendation(phenotypes_[2])
                msg_8 = "Would you like to learn more about your phenotypes?"\
                    "\n“1” to learn about your physical traits"\
                    "\n“2” to learn about your personality"\
                    "\n“3” to learn about your food and nutrition"\
                    "\n“4” to learn about your allergies"\
                    "\n“5” to learn about your diseases"\
                    "\n“q or quit” to leave the conversation"
                send_message(msg_1, phoneNumber)
                send_message(msg_2, phoneNumber)
                send_message(msg_3, phoneNumber)
                send_message(msg_4, phoneNumber)
                send_message(msg_5, phoneNumber)
                send_message(msg_6, phoneNumber)
                send_message(msg_7, phoneNumber)
                send_message(msg_8, phoneNumber)
                # Set state to GETTING_CATEGORY
                setState(phoneNumber, GETTING_CATEGORY)
        elif body in quitCommands:
            msg = "Thanks for listening! Hope to hear from you soon :)"
            send_message(msg, phoneNumber)
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
            send_message(msg_1, phoneNumber)
            send_message(msg_2, phoneNumber)
    return str(MessagingResponse())
