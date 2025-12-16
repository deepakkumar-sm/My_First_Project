def calculate_love_score(name1, name2):
    combined = (name1 + name2).lower()

    true_count = 0
    for letter in "true":
        true_count += combined.count(letter)

    true_love = 0
    for word in "love":
        true_love += combined.count(word)

    score = str(true_count) + str(true_love)
    print(f"Your Love Score is: {score}") 




calculate_love_score("vijai", "ratna")






