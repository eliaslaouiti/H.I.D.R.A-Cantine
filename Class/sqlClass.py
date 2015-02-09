# coding: utf-8
__author__ = 'Laouiti Elias Cédric'
"""
    Class de gestion des requetes sql
"""

try:
    import mysql.connector as mysql
    from mysql.connector import errorcode
    from functions import parseConfig
except ImportError as Error:
    exit("Error import SQL Class : " + Error.message)

config = parseConfig.parse_config("config.ini")


class Sql:

    def __init__(self):
        try:
            self.conn = mysql.connect(user=config['DB_USER'], password=config['DB_PASSWORD'], host=config['DB_SERVER'],
                                      database=config['DB_NAME'])  # Connexion à la base de données
            self.cursor = self.conn.cursor()
        except mysql.connector.Error as err:
            exit("Connection failed : " + err.msg)

    def login_req(self, user, password):
        """
        Methode de connexion de l'utilisateur.
        :param user: string
        :param password: string
        :return: array
        """
        try:
            req = "SELECT count(usr.id)as count, usr.id as user_id  FROM personnel as usr JOIN " \
                  "acces_personnel_hidra as aph JOIN acces_hidra as ah " \
                  "ON aph.id_personnel = usr.id AND ah.id_acces_hidra = aph.id_acces_hidra WHERE usr.login = %(usr)s " +\
                  "AND usr.mot_de_passe = %(pass)s AND (ah.role_acces_hidra = 'administrateur' OR " \
                  "ah.role_acces_hidra = 'preparateur')"

            self.cursor.execute(req, {'usr': user, 'pass': password})
            row = self.cursor.fetchone()
            self.cursor.close()
        except mysql.connector.Error as err:
            exit("Query failed : " + err.msg)

        return row
