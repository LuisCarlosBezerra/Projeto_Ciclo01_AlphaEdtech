import psycopg2 as p


class DatabaseConnection:
    """
    Class to manage the connection with PostgreSQL database.
    """

    def __init__(self, user, password, host, dbname):
        """
        Initializes the class with connection parameters.

        Args:
            user (str): Database user name.
            password (str): Database user's password.
            host (str): Database host address.
            dbname (str): Database name.
        """
        self.user = user
        self.password = password
        self.host = host
        self.dbname = dbname

    def connect(self):
        """
        Establishes a connection with the database.

        Returns:
            connection: Database connection object.
        """
        try:
            connection = p.connect(
                user=self.user,
                host=self.host,
                password=self.password,
                dbname=self.dbname,
            )
            print("INFO: Conexão estabelecida com o Banco de Dados.")
            return connection
        except Exception as e:
            print("INFO: Conexão com o Banco de Dados não foi realizada!")
            raise e

    def disconnect(self, connection):
        """
        Closes the connection with the database.

        Args:
            connection (connection): Database connection object.
        """
        try:
            connection.close()
            print("INFO: Conexão encerrada com o Banco de Dados.")
        except Exception as e:
            print("INFO: Erro ao encerrar conexão com o Banco de Dados!")
            raise e
