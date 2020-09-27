from pydantic import BaseSettings


class Settings(BaseSettings):
    connection_string: str = "mongodb+srv://dbUser:APymv2lNwQeeGdi5@cluster0.xcsmd.azure.mongodb.net/connect4" \
                             "?retryWrites=true&w=majority"
    cluster_name: str = "connect4"
    collection_name: str = "game"

