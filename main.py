from msilib import schema
from fastapi import FastAPI
from . import schemas
from .config import Settings
import googlemaps


gmaps = googlemaps.Client(key=Settings.api)
app = FastAPI()

@app.post('getaddress')
def getaddress(add:schemas.GetAddress):
    
    return gmaps.geocode(add.address)[0]['geometry']['viewport']['southwest']