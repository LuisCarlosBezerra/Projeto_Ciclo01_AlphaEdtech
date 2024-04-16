from db.connection import DatabaseConnection
from models.application import Application
from models.application import DigitalDocument


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

    def get_document_by_certificate_number(self, certificate_number):
        """
        Retrieves a DigitalDocument instance from the database based on the provided certificate number.

        Args:
            certificate_number (str): The certificate number to search for.

        Returns:
            DigitalDocument or None: The DigitalDocument instance retrieved from the database
                that matches the provided certificate number. Returns None if no matching document is found.
        """
        return DigitalDocument.from_db_by_certificate_number(
            self.db, certificate_number
        )

    def get_document_by_choice(
        self,
        ct_date_init=None,
        ct_date_last=None,
        ag_name=None,
        cr_value_init=None,
        cr_value_last=None,
        cl_name=None,
    ):
        """
        Retrieves DigitalDocument instances from the database based on the provided criteria.

        Args:
            ct_date_init (str, optional): The initial contract date to search for.
            ct_date_last (str, optional): The last contract date to search for.
            ag_name (str, optional): The agent name to search for.
            cr_value_init (float, optional): The initial credit value to search for.
            cr_value_last (float, optional): The last credit value to search for.
            cl_name (str, optional): The client name to search for.

        Returns:
            list[DigitalDocument] or None: A list of DigitalDocument instances retrieved from the database
                based on the provided criteria. Returns None if no matching documents are found.
        """
        return DigitalDocument.from_db_by_choice(
            self.db,
            ct_date_init=ct_date_init,
            ct_date_last=ct_date_last,
            cr_value_init=cr_value_init,
            cr_value_last=cr_value_last,
            ag_name=ag_name,
            cl_name=cl_name,
        )

    def __del__(self) -> None:
        """
        Closes the database connection when the Repository object is deleted.
        """
        try:
            self.db.close_connection()
        except Exception as e:
            pass


#
