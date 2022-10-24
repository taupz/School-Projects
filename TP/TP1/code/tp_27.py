#27
dict_etudiants1 = {
    208978 : "AGHALI" ,
    206780 : "AGUILLLON" ,
    207525 : "BAUDOIN" ,
    216928 : "BEBIN" ,
    194001 : "BORNET" ,
    191632 : "BOURNICHE" ,
    204909 : "BOUVIER" ,
    191772 : "BRISSET--BOE" ,
    196648 : "BUSSON" ,
    195613 : "CAILLE" ,
    201280 : "CHAUVEL" ,
    211457 : "CHEVALLIER" ,
    219714 : "CIMAZ" ,
    211442 : "CURIS" ,
    205327 : "DAVIAUD" ,
    216897 : "DONET" ,
    190797 : "DOUABLIN" ,
    213418 : "DURAND" ,
    218614 : "ECHASSERIEAU" ,
    192255 : "GAUTIER" ,
    201926 : "GODINEAU" ,
    212361 : "GOETGHELUCK" ,
    217195 : "GUEGUEN--VINCENT" ,
    193550 : "GULLIENT" ,
    201797 : "HADJAR" ,
    201566 : "HERVE" ,
    208092 : "JOURDROUIN" ,
    201162 : "JOURNE" ,
    196607 : "KADI" ,
    216366 : "KERVERDO" ,
    190865 : "KRUGLER" ,
    196217 : "LAFRANCESCA" ,
    214456 : "LAMARTHE" ,
    218620 : "CATLEY" ,
    190757 : "DJOKO-KOUAM" ,
    200500 : "HOUCKE" ,
    219410 : "JOSSO" ,
    218854 : "LAMY" ,
    207559 : "LARDE" ,
    218205 : "LE BIHAN" ,
    216053 : "LE DILAVREC" ,
    198998 : "LE GLOANEC" ,
    201257 : "LE GOALLER" ,
    191716 : "LE MOUEL" ,
    210210 : "LE SCORNET" ,
    198496 : "LECOQ" ,
    205205 : "LECORGNE" ,
    199445 : "LUCAS" ,
    213020 : "LUCE" ,
    210127 : "MAIRE-AMIOT" ,
    204179 : "MOISSON" ,
    194054 : "MOREAU" ,
    201426 : "NORTON" ,
    219843 : "PERRIN" ,
    201904 : "PLESSIS" ,
    204350 : "PORZIER" ,
    202427 : "THEAULT" ,
    218901 : "THIEBAUD" ,
    213231 : "TRIBUT" ,
    193374 : "TROALIC" ,
    200163 : "VAILLAND" ,
    196931 : "VERDIER" ,
    190231 : "VIEL" ,
    205101 : "WAJROCK" ,
    215963 : "ZAIED"
}

dict_morse={
    'A':'.-',
    'B':'-...',
    'C':'-.-.',
    'D':'-..',
    'E':'.',
    'F':'..-.',
    'G':'--.',
    'H':'....',
    'I':'..',
    'J':'.---',
    'K':'-.-',
    'L':'.-..',
    'M':'--',
    'N':'-.',
    'O':'---',
    'P':'.--.',
    'Q':'--.-',
    'R':'.-.',
    'S':'...',
    'T':'-',
    'U':'..-',
    'V':'...-',
    'W':'.--',
    'X':'-..-',
    'Y':'-.--',
    'Z':'--..',
}

reseau = {
"Arthur" : ["Benjamin", "Emmanuel"],
"Benjamin" : ["Arthur", "Gwenael", "Chloé"],
"Chloé" : ["Benjamin", "Gwenael"],
"Delphine" : ["Emmanuel", "Florian"],
"Emmanuel" : ["Arthur", "Gwenael", "Delphine"],
"Florian" : ["Delphine", "Gwenael"],
"Gwenael" : ["Florian", "Benjamin", "Emmanuel", "Chloé"],
"Hervé" : ["Inès"],
"Inès" : ["Hervé"]
}

def get_prenom(dico, key):
    val = dico.get(key)
    return val
print(get_prenom(dict_etudiants1, 204909))

def get_numero(dico, val):
    for k,v in dico.items():
        if v == val:
            return k
print(get_numero(dict_etudiants1, 'PERRIN'))

def get_nom_10(dico):
    val = []
    for k,v in dico.items():
        if k%10 == 0:
            val.append(v)
    return val
print(get_nom_10(dict_etudiants1))

def first_letter_b(dico):
    keys = []
    for k,v in dico.items():
        if v[0] == 'B':
            keys.append(k)
    return keys
print(first_letter_b(dict_etudiants1))