import jwt
import datetime
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("VIDEOSDK_API_KEY")
SECRET = os.getenv("VIDEOSDK_SECRET_KEY")
expiration_in_seconds = 7200
expiration = datetime.datetime.utcnow() + datetime.timedelta(seconds=expiration_in_seconds)

token = jwt.encode(
    payload={
        "exp": expiration,
        "apikey": API_KEY,
        "permissions": ["allow_join"],
        "version": 2,
        "roomId": "2kyv-gzay-64pg",
        "participantId": "lxvdplwt",
        "roles": ["crawler", "rtc"],
    },
    key=SECRET,
    algorithm="HS256",
)

print(token)