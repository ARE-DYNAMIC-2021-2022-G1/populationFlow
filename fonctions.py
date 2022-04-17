# La fonction initialisation crée les données utilisées pour la simulation (pays, individus) ainsi que des historiques

def initialisation(nb_pays, nb_individus, nb_annees):
    pays =      {i:[random.random(), random.random(), 100] for i in range(nb_pays)}
    individus = {i:[random.random(), random.random(), -1] for i in range(nb_individus)}

    historique_pays =      {i:[] for i in range(nb_pays)}
    historique_individus = {i:[] for i in range(nb_individus)}

    return pays, individus, historique_pays, historique_individus

# La fonction repartition_annuelle simule un mouvement migratoire sur 1 an des individus de la liste individus vers les pays de la liste pays. Elle utilise la formule "somme des (poids du critère i)*(note du critère i) pour 1 <= i <= n", avec n le nombre de critères utilisés.

def repartition_annuelle(pays, individus):
    for k1 in individus.keys():
        acc = 0.0
        p = individus[k1][2]
        
        for k2 in pays.keys():
            n = individus[k1][0]*pays[k2][0] + individus[k1][1]*pays[k2][1]
            
            if n > acc and pays[k2][2] > 0:
                acc = n
                p = k2
        individus[k1][2] = p
        pays[p][2] = pays[p][2] - 1
        
# La fonction changement_pays effectue les changements possibles que peut subir un pays d'une année a une autre.

def changement_pays(pays):
    for k in pays.keys():
        pays[k][2] = 100;
        f = random.random()
        if f < 0.5:
            pays[k][0] = pays[k][0]*0.75 + 0.25*random.random()
            pays[k][1] = pays[k][1]*0.75 + 0.25*random.random()
            
# La fonction changement_individus effectue les changements possibles que peut subir un individu d'une année a une autre.

def changement_individus(individus):
    for k in individus.keys():
        f = random.random()
        if f < 0.5:
            individus[k][0] = individus[k][0]*0.75 + 0.25*random.random()
            individus[k][1] = individus[k][1]*0.75 + 0.25*random.random()
            
# Historique_pays -> Pays : [Niveau de vie pays, Stabilité politique, nombre d'habitants]   
# Historique_individus -> Individu : [Pays de séjour la première année, pays de séjour la deuxième année, ...] 
            
def mise_a_jour_historique(pays, individus, historique_pays, historique_individus):
    for k1 in historique_pays.keys():
        historique_pays[k1].append([pays[k1][0], pays[k1][1], 100-pays[k1][2]])
        
    for k2 in historique_individus.keys():
        historique_individus[k2].append(individus[k2][2])

# La fonction migration simule un mouvement migratoire sur plusieurs années.

def migration(data, nb_annees):
    for i in range(nb_annees):
        print("Année #", i+1)
        plt.figure()
        repartition_annuelle(data[0], data[1])
        mise_a_jour_historique(data[0], data[1], data[2], data[3])
        plt.hist([data[1][k][2] for k in data[1].keys()], bins = [i for i in range(len(data[0]) + 1)])
        plt.show()
        changement_pays(data[0])
        changement_individus(data[1])
    
