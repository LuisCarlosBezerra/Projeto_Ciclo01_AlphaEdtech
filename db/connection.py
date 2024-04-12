import psycopg2 as p


class DatabaseConnection:
    """
    Class to manage the connection with PostgreSQL database.
    """

    def __init__(self, user, password, dbname, host="localhost", port=5432):
        """
        Initializes the class with connection parameters.

        Args:
            user (str): Database user name.
            password (str): Database user's password.
            host (str): Database host address.
            dbname (str): Database name.
        """
        # self.user = user
        # self.password = password
        # self.host = host
        # self.dbname = dbname
        try:
            self.conn = p.connect(
                dbname=dbname, user=user, password=password, host=host, port=port
            )
            self.cur = self.conn.cursor()
            print("INFO: Conexão estabelecida com o Banco de Dados.")
        except Exception as e:
            print("INFO: Conexão com o Banco de Dados não foi realizada!")
            raise e

    def execute_query(self, query, type_query, *args):
        try:
            self.cur.execute(query, args)
            print(f"INFO: Sucesso ao executar '{type_query}' no banco de dados.")
            self.conn.commit()
        except Exception as e:
            print(f"INFO: Erro ao executar {type_query} do banco de dados.")
            print(f"ERROR: {e}")
            self.conn.rollback()

    def fetch_data(self, query, *args):
        self.cur.execute(query, args)
        return self.cur.fetchall()

    # def connect(self):
    #     """
    #     Establishes a connection with the database.

    #     Returns:
    #         connection: Database connection object.
    #     """
    #     try:
    #         connection = p.connect(
    #             user=self.user,
    #             host=self.host,
    #             password=self.password,
    #             dbname=self.dbname,
    #         )
    #         print("INFO: Conexão estabelecida com o Banco de Dados.")
    #         return connection
    #     except Exception as e:
    #         print("INFO: Conexão com o Banco de Dados não foi realizada!")
    #         raise e

    # def disconnect(self, connection):
    #     """
    #     Closes the connection with the database.

    #     Args:
    #         connection (connection): Database connection object.
    #     """
    #     try:
    #         connection.close()
    #         print("INFO: Conexão encerrada com o Banco de Dados.")
    #     except Exception as e:
    #         print("INFO: Erro ao encerrar conexão com o Banco de Dados!")
    #         raise e

    def close_connection(self):

        try:
            self.cur.close()
            self.conn.close()

            print("INFO: Conexão encerrada com o Banco de Dados.")
        except Exception as e:
            print("INFO: Erro ao encerrar conexão com o Banco de Dados!")
            raise e
