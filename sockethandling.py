import requests
try:
    r = requests.get("htttp://www.google.com")
    r.raise_for_status()
except requests.exceptions.HTTPError as err:
    print(f"Fehler: {err}")
except requests.exceptions.InvalidURL:
    print("Die URL ist ungültig!")
