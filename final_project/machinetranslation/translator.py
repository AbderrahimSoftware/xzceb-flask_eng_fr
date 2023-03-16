import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
apikey = "hjL0sqotx59lCaXeJaVm0o173J-LAgP_SaU8AsELfFFd"
url = "https://api.au-syd.language-translator.watson.cloud.ibm.com/instances/93a71727-e597-49a3-9e78-66a238b967c8"
authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(url)
language_translator.set_disable_ssl_verification(True)

def englishToFrench(englishText):
    if not englishText:
       return None
    translation = language_translator.translate(text=englishText, model_id='en-fr').get_result()
    frenchText = translation["translations"][0]["translation"]
    return frenchText

def frenchToEnglish(frenchText):
    if not frenchText:
       return None
    translation = language_translator.translate(text=frenchText, model_id='fr-en').get_result()
    englishText = translation["translations"][0]["translation"]
    return englishText

