from mongoengine import connect
import os

def init_mongo():
    connect(
        db="oyhdb",
        host=os.environ.get("MONGO_URI"),
        alias="default",
        uuidRepresentation="standard"
    )

