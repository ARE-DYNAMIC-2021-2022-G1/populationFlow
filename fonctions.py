# Bibliothèque des fonctions utilisées dans notre modele.


def initialisation(nb_individus, nb_pays, nb_annees):
    pays =      {i:[random.random(), random.random(), 20] for i in range(nb_pays)}
    individus = {i:[random.random(), random.random(), -1] for i in range(nb_individus)}

    historique_pays =      {i:[[] for i in range(nb_annees)] for i in range(nb_pays)}
    historique_individus = {i:[[] for i in range(nb_annees)] for i in range(nb_individus)}

    return individus, pays, historique_pays, historique_individus

# La fonction repartition_annuelle simule un mouvement migratoire sur 1 an des individus de la liste individus vers les pays de la liste pays. Elle utilise la formule "somme des (poids du critère i)*(note du critère i) pour 1 <= i <= n", avec n le nombre de critères utilisés.

def repartition_annuelle(pays, individus):
    for i in range(len(individus)):
        acc = 0.0
        p = individus[i][3]
        
        for j in range(len(pays)):
            n = individus[i][1]*pays[j][1] + individus[i][2]*pays[j][2]
            
            if n > acc and pays[j,3] > 0:
                acc = n
                p = j
                
        individus[i][3] = p
        pays[p,3] = pays[p,3] - 1

# La fonction changement effectue les changements possibles que peut subir un pays d'une année a une autre.

def changement_pays(pays):
    for i in range(len(pays)):
        pays[i][3] = 20;
        f = random.random()
        if f < 0.5:
            pays[i][1] = pays[i][1]*0.75 + 0.25*random.random();
            pays[i][2] = pays[i][2]*0.75 + 0.25*random.random();
            
# La fonction changement effectue les changements possibles que peut subir un individu d'une année a une autre.

def changement_individus(individus):
    for i in range(len(individus)):
        f = random.random()
        if f < 0.5:
            individus[i][1] = individus[i][1]*0.75 + 0.25*random.random();
            individus[i][2] = individus[i][2]*0.75 + 0.25*random.random();
            
def mise_a_jour_historique(pays):
    for i in range(len(pays)):
        pays[i][4].append([20 - pays[i][3], pays[i][1], pays[i][2]])

# La fonction migration simule un mouvement migratoire sur n années.

def migration(pays, individus, n):
    for i in range(n):
        plt.figure()
        repartition_annuelle(pays, individus)
        mise_a_jour_historique(pays)
        plt.hist(individus[:,3], bins = [i for i in range(len(pays)+1)])
        plt.show()
        changement_pays(pays)
        changement_individus(individus)






