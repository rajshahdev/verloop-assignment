from pydantic import BaseModel

class GetAddress(BaseModel):
    address:str
    # output_format:str