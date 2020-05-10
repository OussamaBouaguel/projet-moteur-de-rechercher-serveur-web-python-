#coding:utf-8
import cgi
import cgitb
import index_inverse_temp

cgitb.enable()
form = cgi.FieldStorage()


print("Content-type: text/html; charset=utf-8\n")

#si motif vide on renvoie la page A sinon on affiche la liste de resultat de la fonction index_inverse

try:
    if "motif" not in form:
        html2 = """<!DOCTYPE html>
        <HTML>
        <meta http-equiv="Refresh" content="0.1; url=http://localhost/pageA.py">
        </HTML>
        """
        print(html2)
    else:
        motif = form.getvalue("motif")
except:
    print("<p>fail<p>");
    

html = """<!DOCTYPE html>
<HTML LANG = "fr">
<HEAD>
	<META CHARSET = "UTF-8">
	<TITLE> PAGE B </title>
    <style>
        h1 {text-align: center;}
        h2 {text-align: center;}
        p {text-align: center;}
    </style>
</HEAD>
<BODY>
    <h1> projet algo texte page B </h1>
    <form method="post" action="pageB.py">
        <p><input type="text" name="motif">
        <input type="submit" value="Rechercher"></p>
    </form>
"""

print(html)

print("<h2>Resultat : " + index_inverse_temp.ii(motif) + "<h2>")

html = """	
    
</BODY>
</HTML>
"""

print(html)