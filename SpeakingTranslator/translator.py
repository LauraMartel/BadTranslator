from libraries import *
from translator_emoji import transform_word_to_emoji
from translator_translate import *


root = Tk()
root.title("Bad Translator")


##### Main Frame
translate_frame = Frame(root, background='#808080')
translate_frame.pack()


##### Text Boxes and Comboboxes indicating the languages you wamt to select
original_text = Text(translate_frame, height=10, width=60)
bad_translated = Text(translate_frame, height=10, width=60)
original_combo = ttk.Combobox(translate_frame, width=20, values=list(languages().values()), font='Courier 10', justify='center', background='black')
translated_combo = ttk.Combobox(translate_frame, width=20, values=list(languages().values()), font='Courier 10', justify='center')
original_combo.current(0) # current sets the language you want to be displayed
translated_combo.current(1)


##### Position of the combo boxes
original_text.grid(row=1, pady=10,padx=5, columnspan=3, sticky=S)
bad_translated.grid(row= 4, pady=10,padx=5, columnspan=3)
original_combo.grid(row=1, column=3, padx=5, pady=10)
translated_combo.grid(row=4, column=3, padx=5, pady=10)


##### Buttons
translate_button = Button(translate_frame, text="Translate!", font=("Courier", 5),
        command=lambda:[translate_it(original_text, bad_translated, original_combo, translated_combo),
        transform_word_to_emoji(bad_translated, translate_frame)], border=2, borderwidth=5)
translate_button.configure(font='Courier 12', foreground='white', bg = '#4E4F50', highlightbackground='black')
translate_button.grid(row=3, column=0,padx=2, sticky=N)


def clear_translate():
    original_text.delete(1.0, END),
    bad_translated.delete(1.0, END)

clear_button = Button(translate_frame, text="Clear", font=("Courier", 5),
        command=clear_translate, border=2, borderwidth=5)
clear_button.configure(font='Courier 12', foreground='white', bg = '#4E4F50', highlightbackground='black')
clear_button.grid(row=3, column=2, sticky=S)

##### Labels
label_holder = {}
pos_lab = {'click': [S, 2,0, 'Click Here 👇'], 'orig_text': [None, 0,1, 'Write a sentence here 👇'],
    'clear': [S, 2,2, 'Make it disappear 👇']}
for name_l in pos_lab:
    label_holder[str(name_l) + "_label"] = Label(translate_frame, text=pos_lab[name_l][3], font=("Courier", 8), background='white')
    label_holder[str(name_l) + "_label"].grid(row=pos_lab[name_l][1], column=pos_lab[name_l][2], sticky=pos_lab[name_l][0])

# Allows the window to be locked
root.resizable(0, 0)

root.mainloop()
