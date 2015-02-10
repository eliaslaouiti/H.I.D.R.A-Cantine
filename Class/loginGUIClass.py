# coding: utf-8
__author__ = 'Laouiti Elias Cédric'

try:
    from Class import loginClass
    import pygtk
    import gtk
    import os
except ImportError as Err:
    exit('Import Fail : ' + Err.message)


class LoginGUI:

    def __init__(self):
        interface = gtk.Builder()
        interface.add_from_file('GUI/login.glade')  # Recup du fichier d'interface

        self.login_loader = interface.get_object("login_window_loader")  # Loader
        self.login_username_input = interface.get_object("login_window_username_input")  # Username input
        self.login_password_input = interface.get_object("login_window_password_input")  # Password input
        self.login_window = interface.get_object("login_window")  # Window
        interface.connect_signals(self)  # Recuperation des events

    def on_login_window_btn_sub_clicked(self, widget):
        """
        Methode appelee quand on clique sur le bouton de connexion
        :param widget:
        :return:
        """
        self.login_loader.show()  # Affiche le loader
        user = loginClass.User()  # instance de User
        log = user.connect_user(self.login_username_input.get_text(), self.login_password_input.get_text())
        if log[0]:  # Si Connexion reussie
            self.login_window.hide()  # Cache la fenetre de login
            print("Connected")  # DEBUG
            # TODO : Affichage de la fenetre suivante
        else:  # Erreur de connexion
            # TODO : Gerer les erreur (afficher pop up)
            print("Auth error")  # DEBUG

    def on_login_window_destroy(self, argv):
        """
        Methode appelee quand on clique sur le bouton de fermeture de la fenetre
        :param argv:
        :return:
        """
        gtk.main_quit()  # Destruction de la fenetre
