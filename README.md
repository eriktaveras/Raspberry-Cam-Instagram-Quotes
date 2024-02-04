
# 🌿 Social Media Bot for Nature Quotes

This project automates the process of capturing images from a Raspberry Pi camera and posting them on Twitter and Instagram with nature-inspired quotes. It's designed to run on a Raspberry Pi, utilizing the PiCamera for capturing images, Twython for Twitter interactions, and Instabot for Instagram posts.

## 📋 Requirements

- Raspberry Pi with internet connection 🌐
- PiCamera module installed and configured 📷
- Python 3.x 🐍
- Twython 🐦
- Instabot 📸
- A Twitter Developer account and created app for API keys 🔑
- An Instagram account for posting 📱

## 💾 Installation

1. **Set up Raspberry Pi and PiCamera**: Ensure your Raspberry Pi is set up correctly and the PiCamera is connected and enabled.
2. **Install Python Libraries**: Run the following command to install necessary Python libraries:

    ```bash
    pip install twython instabot picamera
    ```

3. **Configure API Keys**: Replace the placeholder values in the script for `APP_KEY`, `APP_SECRET`, `OAUTH_TOKEN`, and `OAUTH_TOKEN_SECRET` with your Twitter API keys. Similarly, fill in the Instagram username and password fields for Instabot login.

## 🚀 Usage

To run the script, simply execute:

```bash
python nature_post_bot.py
```

This will capture an image, select a random nature quote, and post it on both Twitter and Instagram.

## 🔍 How It Works

- The script initializes the camera and captures an image with a timestamp.
- A random quote about nature is selected from a predefined list.
- The image is posted to Twitter with the selected quote.
- The same image is then posted to Instagram with the quote as a caption.

Make sure you have the necessary permissions and have followed the guidelines of both Twitter and Instagram for posting content through automated scripts.

## 🤝 Contribution

Feel free to fork this project and contribute by adding more quotes or enhancing the functionality. Ensure that any contributions follow the best practices for coding and documentation.

## 📜 License

This project is open-sourced under the MIT License. See the LICENSE file for more details.
