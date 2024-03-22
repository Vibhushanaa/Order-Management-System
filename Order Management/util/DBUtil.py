import pyodbc

class DBUtil:
    @staticmethod
    def getDBConn():
        try:
            # Replace with your actual SQL Server database credentials
            db_params = {
                'server': 'SHARA\\SQLEXPRESS',
                'database': 'codingchallenge',
                'trusted_connection': 'yes'  # Use Windows authentication
            }

            # Establish a connection
            conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};'
                                   f'SERVER={db_params["server"]};'
                                   f'DATABASE={db_params["database"]};'
                                   f'TRUSTED_CONNECTION={db_params["trusted_connection"]}')

            # Return the connection
            return conn

        except Exception as e:
            print(f"Error connecting to the database: {e}")
            return None

# Example usage
db_conn = DBUtil.getDBConn()
if db_conn:
    print("Database connection established successfully!")
    # Perform database operations here
    db_conn.close()
else:
    print("Failed to establish a database connection.")
