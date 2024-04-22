import psycopg2 as p


class DatabaseConnection:
    """
    Class to manage the connection with a PostgreSQL database.

    Attributes:
        conn: psycopg2 connection object.
        cur: psycopg2 cursor object.
    """

    def __init__(self, user, password, dbname, host="localhost", port=5432):
        """
        Initializes the class with connection parameters.

        Args:
            user (str): Database user name.
            password (str): Database user's password.
            host (str): Database host address.
            dbname (str): Database name.
            port (int): Database port number. Default is 5432.
        """
        try:
            self.conn = p.connect(
                dbname=dbname, user=user, password=password, host=host, port=port
            )
            self.cur = self.conn.cursor()
            print("INFO: Conexão estabelecida com o Banco de Dados.")
        except Exception as e:
            print("INFO: Conexão com o Banco de Dados não foi realizada!")
            print(e)
            print(
                "INFO: Programa Encerrado, por problemas na conexão com o Bando de Dados!"
            )
            exit()

    def execute_query(self, query, type_query, *args):
        """
        Execute a SQL query and commit the transaction.

        Args:
            query (str): SQL query string.
            type_query (str): Type of SQL query (e.g., 'SELECT', 'INSERT', 'UPDATE', 'DELETE').
            *args: Parameters to be passed to the query.

        Raises:
            Exception: If an error occurs while executing the query.
        """

        try:
            self.cur.execute(query, args)
            print(f"INFO: Sucesso ao executar '{type_query}' no banco de dados.")
            self.conn.commit()
        except Exception as e:
            print(f"INFO: Erro ao executar {type_query} do banco de dados.")
            print(f"ERROR: {e}")
            self.conn.rollback()

    def fetch_data(self, query, *args):
        """
        Execute a SQL query and fetch the results.

        Args:
            query (str): SQL query string.
            *args: Parameters to be passed to the query.

        Returns:
            list: A list containing the fetched data.

        Raises:
            Exception: If an error occurs while fetching the data.
        """
        try:
            self.cur.execute(query, args)
            return self.cur.fetchall()
        except Exception as e:
            self.conn.rollback()
            print(f"Erro: {e}")
            return []

    def close_connection(self):
        """
        Close the connection with the database.

        Raises:
            Exception: If an error occurs while closing the connection.
        """

        try:
            self.cur.close()
            self.conn.close()

            print("INFO: Conexão encerrada com o Banco de Dados.")
        except Exception as e:
            print("INFO: Erro ao encerrar conexão com o Banco de Dados!")
            raise e
