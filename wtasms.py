import webbrowser
import urllib.parse

phone = "+8801822206206" # Use country code
message = "Hello, i'm siam from Python on Android!"

# Encode the message for a URL
encoded_msg = urllib.parse.quote(message)
url = f"https://api.whatsapp.com/send?phone={phone}&text={encoded_msg}"

# This opens your mobile browser/WhatsApp app
webbrowser.open(url)
