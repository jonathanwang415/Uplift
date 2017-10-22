categoriesCommands = [1, 2, 3, 4, 5]
categories = ["traits", "personality", "food_and_nutrition", "allergies", "diseases"]

def getReply(body):
    try: 
        cmd = int(body)
        if cmd in categoriesCommands:
            # TODO: Add more responses here.
            if cmd is 1:
                return "You choose category: " + categories[cmd-1]
            elif cmd is 2:
                return "You choose category: " + categories[cmd-1]
            elif cmd is 3:
                return "You choose category: " + categories[cmd-1]
            elif cmd is 4:
                return "You choose category: " + categories[cmd-1]
            else:
                return "You choose category: " + categories[cmd-1]
        else:
            return body + " is not a valid category."\
            "\nPlease enter a category from 1 - 6." \
            "\nHere are the following categories: " \
            "\n1 - Physical Traits: " \
            "\n2 - Personality: " \
            "\n3 - Food and Nutrition: " \
            "\n4 - Allergies: " \
            "\n5 - Disease: "
   
    except ValueError:
        # Set up code here
        if body is "start":
            return "Hi! Welcome to Uplift."\
            "\nPlease enter a category from 1 - 6." \
            "\nHere are the following categories: " \
            "\n1 - Physical Traits: " \
            "\n2 - Personality: " \
            "\n3 - Food and Nutrition: " \
            "\n4 - Allergies: " \
            "\n5 - Disease: "
        # More elif here
        else:    
            return "New command I haven't added yet: " + body
