#coding:utf-8
import cgi
import cgitb

cgitb.enable()
form = cgi.FieldStorage()


if form.getvalue("motif")
    motif = form.getvalue("motif")
else:
    raise Exception("Vous n'avez pas entré de motif")
    
    
print("Content-type: text/html; charset=utf-8\n")