bio_so_far = 'Biography info:\n----------------------------\n'

question_num = 1
question = "What's your name?"
name = input(bio_so_far + str(question_num) + '. ' + question)
bio_so_far = bio_so_far +'Name: ' + name + '\n'

question_num = 2
question = "What's your address?"
address = input(bio_so_far + str(question_num) + '. ' + question)
bio_so_far = bio_so_far +'Address: ' + address + '\n'

question_num = 3
question = "What's your age?"
age = input(bio_so_far + str(question_num) + '. ' + question)
bio_so_far = bio_so_far +'Age: ' + age + '\n'

question_num = 4
question = "What is your favourite food?"
favourite_food = input(bio_so_far + str(question_num) + '. ' + question)
bio_so_far = bio_so_far +'Favourite Food: ' + favourite_food + '\n'

question_num = 5
question = "What is your favourite place?"
favourite_place = input(bio_so_far + str(question_num) + '. ' + question)
bio_so_far = bio_so_far +'Favourite Place: ' + favourite_place + '\n'

question_num = 6
question = "Which is your favourite color?"
favourite_color = input(bio_so_far + str(question_num) + '. ' + question)
bio_so_far = bio_so_far + 'Favourite Color: ' + favourite_color + '\n'

question_num = 7
question = "How many members are there in your family?"
members = input(bio_so_far + str(question_num) + '. ' + question)
bio_so_far = bio_so_far +'Family Members: ' + members + '\n'


print(bio_so_far)

