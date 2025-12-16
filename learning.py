# # import math

# # def life_in_weeks(age):
# #     weeks_left = math.floor(90-age)*52
# #     print(f"You have {weeks_left} weeks left.")

# # life_in_weeks(38)

# def greet_with_name(name, location):
#     print(f"Hello {name}")
#     print(f"what is it like in {location}")

# greet_with_name("Deepak Kumar", "New Delhi")

def calculate_love_score(name1, name2):
    combined = (name1 + name2).lower()
    
    true_count = 0
    for letter in "true":
        true_count += combined.count(letter)
    print(true_count)

    true_love = 0
    for letter in "love":
        true_love += combined.count(letter)
    print(true_love)

    score = str(true_count) + str(true_love)
    print(score)

calculate_love_score("smriti","Deepak")





