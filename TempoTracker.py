import requests
import spotipy
import spotipy.util as util
from requests import post

keys = {0: "C", 1: "C#", 2: "D", 3: "D#", 4: "E", 5: "F",
        6: "F#", 7: "G", 8: "G#", 9: "A", 10: "A#", 11: "B"}

username = 'aditya2265'
client_id = '66b7e387a83848598889b323bd36569a'
client_secret = 'f157408a120a4cd3a9413fce1f750a16'
redirect_uri = 'http://localhost:8888/callback'

scope = "playlist-modify-public"
token = util.prompt_for_user_token(
    username, scope, client_id, client_secret, redirect_uri)

SPOTIFY_ACCESS_TOKEN = token

TRACK_ID = "6Ec5LeRzkisa5KJtwLfOoW?si=9f3c66c63e1a4367"

ANALYSIS_API_ENDPOINT = f"https://api.spotify.com/v1/audio-analysis/{TRACK_ID}"

headers = {"Authorization": f"Bearer {SPOTIFY_ACCESS_TOKEN}"
}
response = requests.get(ANALYSIS_API_ENDPOINT, headers=headers)

if response.status_code == 200:
    analysis_data = response.json()
    tempo = analysis_data["track"]["tempo"]
    tempo_confidence = analysis_data["track"]["tempo_confidence"]
    key = analysis_data["track"]["key"]
    key_confidence = analysis_data["track"]["key_confidence"]

    print("\nDisplaying Analysis Data of Track ID: {}".format(TRACK_ID))
    print(f"\nTempo: {tempo} BPM")
    print(f"Tempo Confidence Level: {tempo_confidence}")
    print("Key: {}".format(keys[key]))
    print(f"Key Confidence Level: {key_confidence}\n")


else:
    print("Failed to fetch tempo data")