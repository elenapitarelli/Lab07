from database.DB_connect import ConnessioneDB
from model.artefattoDTO import Artefatto

"""
    ARTEFATTO DAO
    Gestisce le operazioni di accesso al database relative agli artefatti (Effettua le Query).
"""

class ArtefattoDAO:
    def __init__(self):
        pass

    # TODO
    def get_artefatti_filtrati(self, museo, epoca):
        artefatti = []
        cnx = ConnessioneDB.get_connection()
        if cnx is None:
            print("No database connected")
            return artefatti
        cursor = None
        try:

            cursor = cnx.cursor(dictionary=True, buffered=True)
            if museo is not None:
                museo =int(museo)
            query= ("SELECT * FROM artefatto "
                    "WHERE id_museo = COALESCE(%s, id_museo) "
                    "AND epoca = COALESCE(%s, epoca))")
            cursor.execute(query, (museo, epoca))
            for row in cursor:
                a = Artefatto(id =row['id'],nome =row['nome'],
                                           tipologia=row['tipologia'],
                                           epoca=row['epoca'],
                                           id_museo=row['id_museo'])
                artefatti.append(a)
        finally:
            cursor.close()
            cnx.close()
        return artefatti

    def get_epoca(self):
        epoca = []
        cnx = ConnessioneDB.get_connection()
        if cnx is None:
            return epoca
        cursor =cnx.cursor(dictionary=True, buffered=True)
        query = "SELECT DISTINCT epoca FROM artefatto"
        cursor.execute(query)
        for row in cursor:
            epoca.append(row['epoca'])

        cursor.close()
        cnx.close()
        return epoca



