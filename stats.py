caractere: list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
effectif: list = [1, 0, 0, 3, 2, 6, 3, 8, 2, 2, 3];

# --------------- TOTAL EFFECTIFS ---------------

def totalEffectifs(effectif):
    effectifTotal = 0
    for i in range(len(effectif)):
        effectifTotal += effectif[i]
    return effectifTotal

print("Effectif total :")
print(totalEffectifs(effectif))

# --------------- MOYENNE ---------------

def moyenne(caractere, effectif):
    totalCaractere = 0
    effectifTotal = totalEffectifs(effectif)
    for i in range(len(caractere)):
        totalCaractere += caractere[i]*effectif[i]
    return round(totalCaractere/effectifTotal, 2)

print("Moyenne :")
print(moyenne(caractere, effectif))

# -------------------- RANG --------------------

def rang(effectif):
    effectifTotal = totalEffectifs(effectif)
    return (effectifTotal + 1) / 2

print("Rang :")
print(rang(effectif))

# --------------- CUMUL EFFECTIFS ---------------

def cumulEffectifs(effectif):
    effectifActuel = 0
    effectifCumule: list = []

    for i in range(len(effectif)):
        effectifActuel += effectif[i]
        effectifCumule.append(effectifActuel)
    return effectifCumule

print("Effectif cumulé :")
print(cumulEffectifs(effectif))

# --------------- MEDIANE ---------------

def mediane(caractere, effectif):
    rangStat = rang(effectif)                            # Mediane : 15.5
    # rangStat = 16
    effectifCumule = cumulEffectifs(effectif)

    rangNeg = rangStat - 0.5                                # Rang - : 15
    rangPos = rangStat + 0.5                                # Rang + : 16

    # si rang est un integer
    if isinstance(rangStat, int):
        for i in range(len(effectif)):
            if rangStat <= effectifCumule[i]:
                return caractere[i]
            elif effectifCumule[i] > rangStat:
                return caractere[i-1]
                
    # si rang n'est pas un integer
    else:
        for i in range(len(effectif)):
            if effectifCumule[i] > rangNeg and effectifCumule[i] >= rangPos:
                return (caractere[i] + caractere[i-1]) / 2

print("Médiane :")
print(mediane(caractere, effectif))