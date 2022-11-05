from libraries import *


def transform_word_to_emoji(txt, frame):
    global my_label
    
    list_emojis_1 = ["😀","😁", "😂", "🤣", "😃", "😎", "😍", "🥰", "😗", "🥲", "🤔",
        "🤩", "🤗", "🙂", "🫡", "🤨", "🙄", "😏", "😣", "😮", "🫥", "😴"]
    list_emojis_2 = ["🌭", "🍣", "🍤", "🍲", "🥘", "🧆", "🍢", "🥮", "🍥", "🫕", "🍝",
        "🥣", "🥧", "🍦", "🍰", "🎂", "🍪", "🍩", "🍻"]
    list_emojis_3 = ["◶", "◵", "◸", "◹", "◿", "◺", "◴", "◷", "◰", "◳", "◫", "⊟", "◬",
            "◭", "◮", "◘", "◩", "◈", "►", "◄", "△", "▲", "⩓", "⩕", "⩔", "⩑", "⩎", "⩋", "⩌", "⩍", "⩊"]
    
    for emoji1, emoji2, emoji3 in zip((random.sample(list_emojis_1, 1)), (random.sample(list_emojis_2, 1)), (random.sample(list_emojis_3, 1))):
        emoji_1 = emoji1
        emoji_2 = emoji2
        emoji_3 = emoji3

    
    if len(txt.get("1.0",END)) !=0:
        rand_nb = random.randint(0, len((txt.get("1.0",END)).split()))
        print(rand_nb)
        word = random.sample((txt.get("1.0",END)).split(), rand_nb)
        print(len(word))
        my_label = Label(frame)
        my_label.grid_forget()
        my_label.grid(row=1, column=3, sticky=N)
    else:
        print("Enter something")

    text_1 = f"{emoji_1} Smile-y"
    text_2 = f"{emoji_2} You are hungry"
    text_3 = f"{emoji_3} Why so complicated?!"
    
    if len(word) in range(0, 50):
        my_label.config(text=text_1, font=("Courier", 24))
        return  my_label
    elif len(word) in range(50, 200, 1):
        my_label.config(text=text_2, font=("Courier", 24))
        return my_label
    else:
        my_label.config(text=text_3, font=("Courier", 24))
        return my_label
    
    