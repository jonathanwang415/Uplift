categories = [1, 2, 3, 4, 5]

def getReply(body):
    if body in categories:
        return "You choose category: " + body
    else:
        return body + "Not a valid category. Please enter a category from 1 - 6."
        + "\nHere are the following categories: "
        + "\n1 - Physical Traits: "
        + "\n2 - Personality: "
        + "\n3 - Food and Nutrition: "
        + "\n4 - Allergies: "
        + "\n5 - Disease: "

