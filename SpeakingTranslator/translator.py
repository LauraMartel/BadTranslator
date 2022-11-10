from libraries import *
from translator_translate import *
from translator_speech import *

root = Tk()
root.title("Bad Translator")


##### Main Frame
translate_frame1 = Frame(root, background="#848884")
translate_frame1.pack()

translate_frame2 = Frame(root, background="#E5E4E2")
translate_frame2.pack()


##### Text Boxes and Comboboxes indicating the languages you wamt to select
original_text = Text(translate_frame1, height=10, width=60,
                        background="black", foreground="#1FC742", font="Comic")
original_text.insert(1.0, speak_to_text())
bad_translated = Text(translate_frame2,
                        height=10, width=60,
                        background="black", foreground="#1FC742", font= "Comic")
original_combo = ttk.Combobox(translate_frame1, width=20,
                            values=list(languages().values()), font="Comic",
                            justify="center")
translated_combo = ttk.Combobox(translate_frame2, width=20,
                                values=list(languages().values()),
                                font= "Comic", justify="center")
original_combo.current(0) # current sets the language you want to be displayed
translated_combo.current(1)


##### Position of the combo boxes
original_text.grid(row=1, pady=5,padx=5, columnspan=3, sticky=S)
bad_translated.grid(row= 4, pady=5,padx=5, columnspan=3)
original_combo.grid(row=0, column=0, padx=5, pady=5,sticky=W+S)
translated_combo.grid(row=3, column=0, padx=5, pady=5, sticky=W+S)

##### Buttons

translate_button = Button(translate_frame2, text="Translate!", font=("Comic", 5),
        command=lambda:[translate_it(original_text, bad_translated, original_combo, translated_combo),
        text_to_speak(bad_translated.get("1.0",END), translated_combo)] , border=2, borderwidth=5)
translate_button.configure(font="Comic 12", foreground="white", bg = "#4E4F50", highlightbackground="black")
translate_button.grid(row=0, column=1,padx=2, sticky=S)


def clear_translate():
    original_text.delete(1.0, END),
    bad_translated.delete(1.0, END)

clear_button = Button(translate_frame2, text="Clear", font=("Comic", 5),
        command=clear_translate, border=2, borderwidth=5)
clear_button.configure(font="Comic 12", foreground="white", bg = "#4E4F50", highlightbackground="black")
clear_button.grid(row=3, column=1, sticky=S)



# Allows the window to be locked
root.resizable(0, 0)

root.mainloop()
