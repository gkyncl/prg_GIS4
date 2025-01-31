# Ukol: napiste skript, ktery spocita pocty jednotlivych vrstev dle typu geometrie
# skript tedy projde dany adresar a na konci vypise pocet bodovych / liniovych / polygonovych vrstev

# import knihovny arcpy


# nastaveni vstupniho adresare (workspace)


# vytvoreni seznamu vrstev v danem adresari


# vytvoreni promennych pro zapisovani poctu jednotlivych typu geometrie
# promenne budou mit na zacatku hodnotu 0 a pokud bude nalezena vrstva daneho typu geometrie, tak se pricte k dane promenne 1


# for cyklus, ktery bude prochazet vrstvy v danem adresari

    # urceni geometrie dane vrstvy
    # napoveda: 
    # d = arcpy.Describe(vstupni_vrstva)
    # typ_geometrie = d.shapeType

    # 3 podmínky pro rozliseni typu geometrie
    # dana vrstva je bod
        # k promenne urcujici pocet bodu prictu 1
    # dana vrstva je linie
        # k promenne urcujici pocet linii prictu 1
    # dana vrstva je polygon
        # k promenne urcujici pocet polygonu prictu 1

# vypis vysledku


#####################################
# UKOLY NAVIC:
# 1) upravte skript, aby data rozradil do 3 zadanych databazi dle typu geometrie - tedy, ze kazdy typ geometrie skonci v prislusne databazi
