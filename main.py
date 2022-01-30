from fastapi import FastAPI, status, HTTPException, Response
from schemas import GetAddress
from config import settings
import googlemaps


gmaps = googlemaps.Client(key=settings.api)
app = FastAPI()

@app.post('/getaddress', status_code=status.HTTP_200_OK)
def getaddress(add:GetAddress):
    if not add.address and not add.output_format:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"enter a valid address and output type")
    if not add.address:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"enter a valid address")
    if not add.output_format:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"enter a valid output type")

    latlng = gmaps.geocode(add.address)[0]['geometry']['viewport']['southwest']
    lat = latlng['lat']
    lng = latlng['lng']
    if add.output_format == "xml":
        data = f"""
        <?xml version="1.0" encoding="UTF-8"?>
            <root>
                <address>{add.address}</address>
                <coordinates>
                    <lat>{lat}</lat>
                    <lng>{lng}</lng>
            </coordinates>
        </root>
        """
        return Response(content=data, media_type="application/xml")
    elif add.output_format == "json":
        return {"coordinates":{"lat":lat,"lng":lng}, "address":add.address}
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"enter a valid output type")    
    