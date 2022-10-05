from ibm_watson import TextToSpeechV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

apikey = 'kPjbJKGTSd_eXGSckUA51-DHnteasGj6MAGhbUaPtjf0'
url = 'https://api.eu-gb.text-to-speech.watson.cloud.ibm.com/instances/5feb4f10-875f-42b4-853c-36b5100563da'


# Setup Service
authenticator = IAMAuthenticator(apikey)
# New TTS Service
tts = TextToSpeechV1(authenticator=authenticator)
# Set Service URL
tts.set_service_url(url)


#reading a file
with open('text/ishabh.txt', 'r') as f:
    text = f.readlines()
    text = [line.replace('\n', '') for line in text]
    text = ''.join(str(line) for line in text)

with open('speech./ishabh.mp3', 'wb') as audio_file:
    res = tts.synthesize(text, accept='audio/mp3',
                         voice='en-US_EmilyV3Voice').get_result()
    audio_file.write(res.content)
