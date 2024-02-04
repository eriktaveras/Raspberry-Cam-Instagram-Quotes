# coding=utf-8
from twython import Twython
import random
from picamera import PiCamera
from datetime import datetime
from instabot import Bot

# Twitter API credentials
APP_KEY = ''
APP_SECRET = ''
OAUTH_TOKEN = ''
OAUTH_TOKEN_SECRET = ''

# Instagram login credentials
INSTAGRAM_USERNAME = ""
INSTAGRAM_PASSWORD = ""

# Initialize Instagram bot
bot = Bot()
bot.login(username=INSTAGRAM_USERNAME, password=INSTAGRAM_PASSWORD)

# Initialize and configure PiCamera
camera = PiCamera()
camera.rotation = 180  # Adjust as per your setup

# Capture an image with a timestamp
timestamp = datetime.now().isoformat()
photo_path = f"/home/pi/tweetcam/imagen{timestamp}.jpg"
camera.capture(photo_path)

# Initialize Twython for Twitter interaction
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

# Select a random message
message = random.choice(messages)

# Post the image and message on Twitter
with open(photo_path, 'rb') as photo:
    response = twitter.upload_media(media=photo)
    twitter.update_status(status=message, media_ids=[response['media_id']])

# Cleanup: Close the camera resource
camera.close()

# Post the image and message on Instagram
bot.upload_photo(photo_path, caption="Y Recuerda: " + message)
