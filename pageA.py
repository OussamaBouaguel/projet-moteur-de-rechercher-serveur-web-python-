#coding:utf-8
import cgi

print("Content-type: text/html; charset=utf-8\n")


html = """<!DOCTYPE html>
<HTML LANG = "fr">
<HEAD>
	<META CHARSET = "UTF-8">
	<TITLE> MOTEUR DE RECHERCHE NYO </title>
</HEAD>
<BODY>
	<h1> RECHERCHE </h1>
    
    <form method="post" action="pageB.py">
        <p><input type="text" name="motif">
        <input type="submit" value="Rechercher"></p>
    </form>
</BODY>
</HTML>
"""

print(html)