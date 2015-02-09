# coding: utf-8
__author__ = 'Laouiti Elias Cédric'

"""
    Class de gestion de l'utilisateur
"""

try:
    import hashlib  # Librairie de Hashage des mots de passes
    from Class import sqlClass
except ImportError as Error:
    exit("Import Error : " + Error.message)


class User():

    def __init__(self):
        self.userEmail = ""
        self.userRole = ""

    def _connectuser(self, user_email, user_password):
        """
        Connexion de l'utilisateur.
        :param user_email: string
        :param user_password: string
        :return: array: code 0 si erreur code 1 si connexion reussie
        """

        password = hashlib.sha512(user_password).hexdigest()  # Hash du mot de passe
        sql = sqlClass.Sql()
        res = sql.login_req(user_email, password)
        if res[0] == 1:
            self.userEmail = user_email
            return [1, "OK"]
        else:
            return [0, "Identifiant / Mot de passe incorrecte"]

    """
        Puublic method
    """

    def connect_user(self, user_email, user_password):
        return self._connectuser(user_email, user_password)