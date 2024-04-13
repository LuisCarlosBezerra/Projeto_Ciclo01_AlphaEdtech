from db.connection import DatabaseConnection
from models.application import Application


class Repository:
    """
    A repository class for managing interactions with a PostgreSQL database.

    This class provides methods for saving and retrieving application data from the database.

    Attributes:
        db (DatabaseConnection): An instance of the DatabaseConnection class for managing
        database connections.
    """

    def __init__(self, dbname, user, password, host="localhost", port=5432):
        """
        Initializes the Repository with connection parameters.

        Args:
            dbname (str): The name of the database.
            user (str): The username for accessing the database.
            password (str): The password for accessing the database.
            host (str, optional): The hostname of the database server. Defaults to "localhost".
            port (int, optional): The port number of the database server. Defaults to 5432.
        """
        self.db = DatabaseConnection(
            dbname=dbname, user=user, password=password, host=host, port=port
        )

    def save_applicacation(self, app):
        """
        Saves an application to the database.

        Args:
            app (Application): The application object to be saved to the database.
        """
        app.save_to_database(self.db)

    def get_application(self, app_id):
        """
        Retrieves an application from the database.

        Args:
            app_id (int): The ID of the application to retrieve.

        Returns:
            Application: The application object retrieved from the database.
        """
        return Application.from_database(self.db, app_id)

    def __del__(self) -> None:
        """
        Closes the database connection when the Repository object is deleted.
        """
        try:
            self.db.close_connection()
        except Exception as e:
            pass


#
