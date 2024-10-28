from googletrans import Translator

translator = Translator()

def translate_to_english(text):
    """Translate user input to English using Google Translate."""
    try:
        result = translator.translate(text, dest='en')
        return result.text
    except Exception as e:
        return f"Translation failed: {str(e)}"
