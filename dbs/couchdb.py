import couchdb
from utils.util import get_env


class CouchDB:
    host: str
    port: int
    username: str
    password: str
    database: str

    def __init__(self) -> None:
        self.host = get_env("COUCHDB_HOST")
        self.port = get_env("COUCHDB_PORT")
        self.username = get_env("COUCHDB_USERNAME")
        self.password = get_env("COUCHDB_PASSWORD")
        self.database_name = get_env("COUCHDB_DATABASE")
        self.db = self._connect()

    def _connect(self):
        self.server = couchdb.Server(
            f"http://{self.username}:{self.password}@{self.host}:{self.port}"
        )
        if self.database in self.server:
            return self.server[self.database]
        return self.server.create(self.database)

    def insert_many(self, documents: list):
        for document in documents:
            self.db.save(document)
    