import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
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


# Function that takes english text and returns french text
def englishToFrench(englishText):
    frenchResults = my_translator.translate(
        text=englishText,
        model_id='en-fr').get_result()
    frenchText = frenchResults['translations'][0]['translation']        
    return frenchText


# Function that takes french text and translates to english
def frenchToEnglish(frenchText):
    englishResults = my_translator.translate(
        text=frenchText,
        model_id='fr-en').get_result()
    englishText = englishResults['translations'][0]['translation'] 
    return englishText


# Function that takes english text and translates to spanish
def englishToSpanish(engText):
    engResults = my_translator.translate(
        text=engText,
        model_id='en-es').get_result()
    spanishText = engResults['translations'][0]['translation'] 
    return spanishText



# Print results
print(englishToFrench("Hello what is your name?"))
print(englishToSpanish("Hello what is your name?"))
