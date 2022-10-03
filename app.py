
from flask import Flask
import requests
import os
from os.path import isfile
from flask import request, render_template, make_response
import shutil

#import numpy as np



app = Flask(__name__)



##############################################
# ACCUEIL DU SERVEUR 
##############################################
@app.route('/index',methods=['get','post']) 
@app.route("/") 
def index():
  path_logo   ='./static/logo.png'
  
  
  return render_template('index.html',logo= path_logo)

##############################################
#  TEST DE  L'AZURE FUCTION 
#############################################
@app.route('/ResultRecom',methods=['post'])
def ResultRecom():
  
  print("IN RESULT ====================")
  # on récupere le numéro de utilisateur 
  user_selected=request.form['user_id']
   # on récupere l'url cible (endpoint)'
  Url_endpoint=request.form['url_api']
  print("user_id", user_selected)
  print("url endpoint", Url_endpoint)
  #construction de l'url final
  final_url=Url_endpoint+"/?user_id="+user_selected
  print("final end point :" ,final_url )

  
 # ENVOIE DE LA REQUETE A l'AP
  # declaration du header  
  if(Url_endpoint!="none"):
     headers = { 
        'Content-Type': "text/plain"     
     } 
  response = requests.request("POST", final_url, headers=headers, data=user_selected)
  print("PRINT_REPONSE=",response.text )
  result_recom= response.text
  print("article recommande :",result_recom)
  result =result_recom.split(";")
  print(result)
  
  reco1=result[0]
  reco2=result[1]
  reco3=result[2]
  reco4=result[3]
  reco5=result[4]

  return render_template('ResultRecom.html', user_id=user_selected,   reco0=reco1,reco1=reco2, reco2=reco2 ,  reco3=reco3, reco4=reco4, reco5=reco5 )

 
if __name__ == '__main__':
   app.run(host='127.0.0.2', debug = True)

