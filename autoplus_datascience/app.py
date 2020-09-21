import requests 
import pickle 
import numpy as np  
import pandas as pd
import flask
# Making a get request 
#response = requests.get('{'aa': '4'}') 
  
# print response
#print(response) 

# print json content 

finalized_model = pickle.load(open('final_model.pkl', 'rb'))
Minmax = pickle.load(open('Minmax.pkl', 'rb'))


from flask import Flask, request
import json
import requests

app = Flask(__name__)
xy=0

@app.route('/api/foo/', methods=['GET'])
def foo():
    bar = request.args.to_dict()
    #japp_json = json.dumps(bar)


    marques=['alfa romeo','aro','audi','bmw','buick','cadillac','chevrolet','chrysler','citroen','corvette','dacia',
 'deawoo','dodge','fiat','ford','honda','hummer','hyundai','infiniti','isuzu','jaguar','jeep','kia','lada','lancia','land-rover',
'lexus','mahindra','mazda','mega','mercedes','mini','mitsubishi','nissan','opel','peugeot','porsche',
 'renault','rover','seat','skoda','smart','ssangyong','suzuki','toyota','volkswagen']

    modeles=['107','110','147','156','159','190','200','2008','205','206','206 sw',
'206 plus','206 sedan','207','207 cc','208','220','3008','300m','301','306',
'307','307 cc','307 sw','308','308 cc','323','403','406','407','407 sw',
'4runner','500','508','75','80','807','a1','a3','a3 sportback','a4','a5',
'a5 coupe','a6','ax','accent','actyon','alpine','altea','altea xl','amarok',
'astra','autres','avanza','aveo','aygo','bt-50 pick-up','babolilin','baleno',
'beetle','berlingo','bipper tepee','blazer','bora','bravo','break','c elysée',
'c-crosser','c1','c2','c3','c3 picasso','c4','c4 aircros','c4 picasso','c5',
'c6','cla','cr-v','cx - 7','cx-5','cx-9','caddy','cadenza','camry','carens',
'carisma','cayenne','cayman','ceed','cerato','classe a','classe b','classe c',
'classe cis','classe cla','classe clc','classe clk','classe e','classe s',
'clio','clio 2','clio 3','clio 4','clio 5','clio 6','clio 7','clio campus',
'club berline','colt','compass','cooper','corboda','corolla','corsa',
'countryman cooper','coupe','cruze','d- max','ds3','ds4','ds5','dakota',
'defender','delta','doblo','dokker','dune buggy','duster','eos','elantra',
'escalade','escort','evoque','expert','express','fabia','family','faster',
'fiesta','figo','fiorino qubo','fluence','focus','focus c-max','forfour',
'fortwo','freelander','frontera','fusion','goa pick clip','gt','gtv',
'giulietta','golf','golf 2','golf 3','golf 4','golf 5','golf 6','golf 7','golf plus','grand vitara','grand cherokee','grand i10','grande punto','h-1','h3','hiace','hilux','i10','i20','ix35','ibiza','insignia','jetta','jimny',
'juke','jumper','jumpy','ka','kangoo','koleos','korando','l200','ls','laguna',
'laguna 2','laguna 3','lancer','land cruiser','lantra','leon','linea','logan',
'ml','mr','marea','mazda2','mazda3','mazda6','megane','megane 2',
 'megane 2 coupe','megane 3','megane break','megane classic','megane coupe',
'meriva','micra','mito','modus','mondeo','multipla','murano','megane sedan',
'navara','nemo','nubira','octavia','omega','one','one  d','optima','optra',
 'other','pajero','palio','panda','partner','partner tepee','passat',
 'passat cc','passion','pathfinder','patrol','picanto','picasso','polo',
 'polo 3','polo 4','polo 5','polo 6','polo 7','prado','primera','punto',
 'punto evo','q5','qashqai','r19','r4','rcz','rio','range rover','ranger',
'rav 4','rexto n','s-type','s4','serie 1','serie 3','serie 5','serie 7',
 'samurai','sandero','saxo','scenic','scenic 2','scirocco','seirra','siena',
 'sonic','spark','splash','sporento','sportages','stilo','strento','sunny',
 'superb','swing','symbol','tt','tahoe','terra','terrano','tiguan','toledo',
 'touareg','touran','tourneo vp','trafic','transporter','trapeurs','trooper',
 'twingo','uno','veloster','vento','viand','vitara','x-trail','x-type',
 'x1','x3','x5','x6','xc 60','xf','xsara','yaris','ypsilon','capture','civic'
 ]

    transmission= ['automatique','manuelle']

    body_condtion=['trés bon','assez bon','bon','dorigine','en marche','en panne',	'excellent']

    enrgie=['diesel',	'essence',	'gpl']

    for j in marques:
        if j == list(bar.values())[3]:
            a1=marques.index(list(bar.values())[3])

    for i in modeles:
        if i == list(bar.values())[4]:
            a2=modeles.index(list(bar.values())[4])
    for k in transmission:
        if k == list(bar.values())[5]:
            a3=transmission.index(list(bar.values())[5])
    for h in body_condtion :
        if h ==list(bar.values())[6]:
            a4=body_condtion.index(list(bar.values())[6])
    for q in enrgie:
        if q==list(bar.values())[7]:
            a5=enrgie.index(list(bar.values())[7])



    puissance1=list(bar.values())[0]
    kilometers1=list(bar.values())[1]
    age1=2020-int(list(bar.values())[2])


    m1=np.concatenate((np.zeros(a1),np.ones(1)), axis=0)
    m2=np.concatenate((m1,np.zeros(len(marques)-a1-1)), axis=0)
    marque1=m2



    mo1=np.concatenate((np.zeros(a2),np.ones(1)), axis=0)
    mo2=np.concatenate((mo1,np.zeros(len(modeles)-a2-1)), axis=0)
    modele1=mo2


    tr1=np.concatenate((np.zeros(a3),np.ones(1)), axis=0)
    tr2=np.concatenate((tr1,np.zeros(len(transmission)-a3-1)), axis=0)
    transm1=tr2

    bod1=np.concatenate((np.zeros(a4),np.ones(1)), axis=0)
    bod2=np.concatenate((bod1,np.zeros(len(body_condtion)-a4-1)), axis=0)
    bodyco1=bod2

    eng1=np.concatenate((np.zeros(a5),np.ones(1)), axis=0)
    eng2=np.concatenate((eng1,np.zeros(len(enrgie)-a5-1)), axis=0)
    enrgie1=eng2


    g6=pd.DataFrame(pd.Series(puissance1))
    g7=pd.DataFrame(pd.Series(kilometers1))
    g8=pd.DataFrame(pd.Series(age1))
    g9=pd.DataFrame(pd.Series(marque1))


    g10=pd.DataFrame(pd.Series(modele1))
    g11=pd.DataFrame(pd.Series(transm1))
    g12=pd.DataFrame(pd.Series(bodyco1))
    g13=pd.DataFrame(pd.Series(enrgie1))

    gd=pd.concat([g6,g7,g8,g9,g10,g11,g12,g13],axis=0)

    bn=Minmax.transform(gd.values.reshape(1,-1))
    z=finalized_model.predict(np.array(bn[0]).reshape(1,-1))

    zmin=z-(z*0.12)
    zmax=z+(z*0.12)
    #japp_json = json.dumps(bar)

    p={ 'prix_min' : str(zmin[0]),'prix' : str(z[0]) ,'prix_max' : str(zmax[0])}

    response = app.response_class(
        response=json.dumps(p),
        status=200,
        mimetype='application/json'
      
    )
    #return response
    
    
    #print(zmin)
    #print(z)

    #print(zmax)
  

    return response







if __name__ == '__main__':   
    app.run(debug=False,port=)
