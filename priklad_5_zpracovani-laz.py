# Ukol: vytvorte skript, ktery vytvori rastrovy DMR na zaklade vstupnich LAZ souboru (viz ukol 1 z GIS)
# pro testovani pouzijte vstupni data: priklad_5.zip, ktera obsahuji 6 LAZ souboru

# pripomenuti postupu zpracovani:
# 1) prevod LAZ na LAS, fce CONVERT LAS
# 2) prevod LAS na bodovou vrstvu, fce LAS TO MULTIPOINT
# 3) tvorba TINu z bodove vrstvy, fce CREATE TIN
# 4) prevod TINu na rastr, fce TIN TO RASTER 


# import knihovny arcpy


# nastaveni vstupniho adresare (je treba promyslet, kam nastavit ...?)


# vytvoreni seznamu *.laz souboru v danem adresari
# k vytvoreni seznamu lze vyuzit konstrukci arcpy.ListFiles(???) - podivejte se do napovedy, jak zaridit, aby vznikl seznam pouze *.laz souboru


# tisk seznamu *.laz souboru pro kontrolu
# meli byste dostat: ['DECI65.laz', 'DECI66.laz', 'DECI67.laz', 'DECI75.laz', 'DECI76.laz', 'DECI77.laz']


# for cyklus, ktery bude prochazet *.laz soubory ve vytvorenem seznamu
    # funkce CONVERT LAS, ktera vzdy prevede soubor z formatu *.laz na *.las
    # promyslete, jake parametry funkce je treba vyplnit a najdete v napovede, jak to udelat
    # soubory *.las ukladejte do samostatne slozky, ktera nebude obsahovat nic jineho
    # pokud potrebujete zadat souradnicovy system, lze to zapsat nasledovne: arcpy.SpatialReference(5514), 5514 je EPSG kod s. systemu


# funkce LAS TO MULTIPOINT pro prevod *.las souboru na body
# vstupem bude slozka obsahujici *.las soubory (a nic jineho) a dalsi parametry ???


# funkce CREATE TIN pro vytvoreni TINu z vytvorene bodove vrstvy
# parametr in_features musi obsahovat informaci o vstupni vrstve, atributu s jeho nadmorskou vyskou a typ dat
# ve vasem pripade lze pouzit zapis "vstupni_body Shape.Z masspoints"


# funkce TIN TO RASTER pro prevod TINu na raster
# funkci nastavte, aby mel vysledny rastr prostorove rozliseni (velikost pixelu) 5 m


#####################################
# UKOLY NAVIC:
# 1) upravte skript tak, aby nazvy vystupu a cesty pro ulozeni potrebnych dat, resp. cesta ke vstupnim datum byly zadany na zacatku jako promenne, tj. aby sly snadno zmenit na prvnich radcich skriptu
# navrh promennych:
# - cesta k adresari se vstupnimi daty
# - cesta k adresari pro ukladani *.las souboru¨
# - cesta pro ulozeni bodove vrstvy (vystup fce LAS TO MULTIPOINT)
# - cesta pro ulozeni vysledneho TINu
# - cesta pro ulozeni vysledneho rastr
# - velikost pixelu vysledneho rastru

