import requests 
import json

def emotion_detector(text_to_analyse): 
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    myobj = { "raw_document": { "text": text_to_analyse } }  
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    response = requests.post(url, json = myobj, headers=header)
    formatted_response = json.loads(response.text)
   
    
    
    # Si el código de estado de la respuesta es 200, extrae el label y el score de la respuesta
    if response.status_code == 200:
        anger_score= formatted_response['emotionPredictions'][0]['emotion']['anger']
        disgust_score= formatted_response['emotionPredictions'][0]['emotion']['disgust']
        fear_score= formatted_response['emotionPredictions'][0]['emotion']['fear']
        joy_score= formatted_response['emotionPredictions'][0]['emotion']['joy']
        sadness_score= formatted_response['emotionPredictions'][0]['emotion']['sadness']
        emotions = {
            'anger': anger_score,
            'disgust': disgust_score,
            'fear': fear_score,
            'joy': joy_score,
            'sadness': sadness_score,
        }
        dominant_emotion = max(emotions, key=emotions.get)
        emotions['dominant_emotion'] = dominant_emotion

    # Si el código de estado de la respuesta es 400, establece label y score en None
    elif response.status_code == 400:
        emotions = {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None,
        }
    return emotions