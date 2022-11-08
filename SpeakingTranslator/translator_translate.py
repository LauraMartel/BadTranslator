from libraries import *


def languages():
    languages = {'en': 'english', 'fr': 'french', 'de': 'german', 'zh-cn': 'chinese (simplified)'}
    return languages

def translate_it(otext, btran, ocombo, tcombo):
    #translated_text.delete(1.0, END)
    btran.delete(1.0, END)
    try:
        for key, value in languages().items():
            if (value == ocombo.get()):
                from_language_key = key
        for key, value in languages().items():
            if (value == tcombo.get()):
                to_language_key = key


        words = textblob.TextBlob(otext.get(1.0, END))
        words = words.translate(from_lang = from_language_key, to = to_language_key)
        btran.insert(1.0, words)

    except Exception as e:
        messagebox.showerror("Translator", e)
