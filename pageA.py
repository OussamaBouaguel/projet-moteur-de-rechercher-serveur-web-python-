#coding:utf-8
import cgi

print("Content-type: text/html; charset=utf-8\n")


# on entre un motif qui nous renvoie vers la page B qui affichera le resultat 

html = """<!DOCTYPE html>
<HTML LANG = "fr">
<HEAD>
	<META CHARSET = "UTF-8">
	<TITLE> PAGE A </title>
    <style>
        h1 {text-align: center;}
        p {text-align: center;}
    </style>
</HEAD>
<BODY>
	<h1> projet algo texte page A </h1>
    
    <form method="post" action="pageB.py">
        <p><input type="text" name="motif">
        <input type="submit" value="Rechercher"></p>
    </form>
</BODY>
</HTML>
"""

print(html)