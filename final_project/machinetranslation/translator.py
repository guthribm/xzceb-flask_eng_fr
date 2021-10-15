"""
My French/English language translator
"""
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

from dotenv import load_dotenv

load_dotenv()



# Set up variables
apikey = os.environ['apikey']
url = os.environ['url']

# Set up Authenticator and Language Translator Instance
authenticator = IAMAuthenticator(f"{apikey}")
my_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

# Set up to my service URL
my_translator.set_service_url(f"{url}")



def english_to_french(english_text):
    """Function that takes english text and returns french text"""
    french_results = my_translator.translate(
        text=english_text,
        model_id='en-fr').get_result()
    french_text = french_results['translations'][0]['translation']
    return french_text


def french_to_english(french_text):
    """Function that takes french text and translates to english"""
    english_results = my_translator.translate(
        text=french_text,
        model_id='fr-en').get_result()
    english_text = english_results['translations'][0]['translation']
    return english_text



def english_to_spanish(eng_text):
    """Function that takes english text and translates to spanish"""
    eng_results = my_translator.translate(
        text=eng_text,
        model_id='en-es').get_result()
    spanish_text = eng_results['translations'][0]['translation']
    return spanish_text



# Print results
print("Hello, this is a French Translator")
print(english_to_french("Hello, this is a French Translator"))

