from database.DB_connect import ConnessioneDB
from model.museoDTO import Museo

"""
    Museo DAO
    Gestisce le operazioni di accesso al database relative ai musei (Effettua le Query).
"""

class MuseoDAO:
    def __init__(self):
        pass
    def get_musei(self):
        musei = []
        cnx = ConnessioneDB.get_connection()
        if cnx is None:
            print("Errore nella connessione")
            return musei
        try:
            cursor = cnx.cursor(dictionary=True, buffered=True)
            query = "SELECT id,nome,tipologia FROM museo"
            cursor.execute(query)
            for row in cursor:
                musei.append(Museo(id=row['id'], nome =row['nome'], tipologia=row['tipologia']))
            cursor.close()
            cnx.close()
        except Exception as e:
            print(f"Errore durante la lettura dei musei:{e}")
        return musei
    # TODO
