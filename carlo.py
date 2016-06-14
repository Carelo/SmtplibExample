#!/usr/bin/python
# -*- coding: utf-8 -*-
#; Copyright 2016 <Carlo>
#; https://github.com/Carelo/
#; Creation date [14.06.2016]

from Mailer import Mailer

server   = 'klimlive.de'
port     = 587
user     = 'carlo@klimlive.de'
pwd      = 'AKoBBoxyPkxX7Dk9SCn7'
fromaddr = user
toaddr   = "carlo.niessen32@gmail.com"
title    = "test"
msg      = 'hallo test'
MyMail = Mailer(server, port, user, pwd)
MyMail.head(toaddr, fromaddr, title)
MyMail.message(msg)
MyMail.connect()
if (MyMail.send()):
    print ("Success!")
else :
    print ("Failed!")
del MyMail
