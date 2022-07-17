import os


class Config:
    PG_USER = os.environ.get("PG_USER", "system_serv_one")
    PG_PASS = os.environ.get("PG_PASS", "serv_one123")
    PG_HOST = os.environ.get("PG_HOST", "localhost")
    PG_DB = os.environ.get("PG_DB", "service_one")
