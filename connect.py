class Engine:
    def __init__(self, username, password, host, port, database):
        self.username = username
        self.password = password
        self.host = host
        self.port = port
        self.database = database

    def connection(self):
        import sqlalchemy
        db = f'postgresql://{self.username}:{self.password}@{self.host}:{self.port}/{self.database}'
        engine = sqlalchemy.create_engine(db)
        return engine.connect()

