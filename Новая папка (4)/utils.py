from googletrans import Translator


async def translat_user_text(text, lang):
    result = translator.translate(text=text, dest=lang)

    return result.text