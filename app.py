# coding=utf-8
from twython import Twython
import random
from picamera import PiCamera
from time import gmtime, strftime
from datetime import datetime
from instabot import Bot 


APP_KEY        = ''
APP_SECRET     = ''
OAUTH_TOKEN        = ''
OAUTH_TOKEN_SECRET = ''

bot = Bot() 

bot.login(username = "",  
          password = "") 

camera = PiCamera()
camera.rotation = 180
timestamp = datetime.now().isoformat()
photo_path = "/home/pi/tweetcam/imagen" + timestamp + ".jpg"
camera.capture(photo_path)

twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

messages = [
      'Solo podemos dominar la naturaleza si la obedecemos.',
      'En todas las cosas de la naturaleza hay algo maravilloso.',
      'La belleza del mundo natural está en los detalles.',
      'Hay dos cosas que me llaman terriblemente la atención: la inteligencia de los animales y la bestialidad de los humanos.',
      'Mi deseo es quedarme así siempre: viviendo con tranquilidad en un pequeño rincón de la naturaleza.',
      'Mantén tu amor por la naturaleza, pues es la verdadera forma de entender el arte.',
      'Aunque supiera que mañana se acaba el mundo... hoy mismo plantaría un árbol.',
      'La naturaleza es la mejor maestra de la verdad.',
      'Aquellos que contemplan la belleza de la tierra, encuentran fuerzas que durarán para siempre.',

]

message = random.choice(messages)

photo = open(photo_path, 'rb')
response = twitter.upload_media(media=photo) 
twitter.update_status(status=message, media_ids=[response['media_id']])

camera.close()

bot.upload_photo(photo_path,  
           caption = "Y Recuerda: " + message) 
