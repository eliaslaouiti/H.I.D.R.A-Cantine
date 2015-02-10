#!/usr/bin/python
# coding: utf-8
__author__ = 'Laouiti Elias Cédric'

try:
    from Class import loginGUIClass
    import pygtk
    import gtk
    pygtk.require("2.0")
except ImportError as Err:
    exit("Import Error : " + Err.message)


try:
    loginGUIClass.LoginGUI()
    gtk.main()

except Exception as err:
    print(err)
    exit("Une erreur est survenue : " + err.message)
