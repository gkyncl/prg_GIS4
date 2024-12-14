import arcpy

arcpy.env.workspace = "U:/2024-25/GIS_4/automatizace_python/autom_python/data_priklad/priklad_2"

vrstvy = arcpy.ListFeatureClasses()

# for cyklus prochazejici postupne jednotlive vrstvy v seznamu vrstev
for v in vrstvy:
    # pouziti funkce Describe, ktera vraci objekt s nekolika vlastnostmi dane vrstvy (napr. typ geometrie, ...)
    # zjednodusene: funkce Describe vrati "kolekci" informaci o dane vrstve (neco jako "slozitejsi seznam")
    # tuto celou "kolekci" informaci si ukladame do promenne d
    # promenna d tedy obsahuje sadu informaci o dane (zrovna prochazene vrstve - v)
    d = arcpy.Describe(v)

    # pokud z teto sady informaci chceme ziskat nejakou konkretni pouzivame k tomu nize uvedeny zapis
    # tedy, ze za promennou reprezentujici onu kolekci napiseme tecku a oznaceni dane informace
    # pokud chceme ziskat informaci o typu geometrie, tak pouzivame klicove slovo "shapeType"
    # vystup ulozime do nove promenne
    typ_geometrie = d.shapeType

    # nechame vypsat typ geometrie dane vrstvy
    print(typ_geometrie)


    # upraveni vypisu, aby byl ve tvaru "nazev vrstvy": "typ geometrie"
    print(f"{v}: {d.shapeType}")
