# Ukol: vytvorte skript, ktery projde vrstvy v danem adresari a zkopiruje z nej pouze ty, ktere nejsou prazdne
# pro ucely prikladu vytvorte databazi, do ktere budete chtit vystupy ulozit
# databaze pro testovani: priklad_4.gdb


# import knihovny arcpy


# nastaveni vstupniho adresare (workspace)


# vytvoreni seznamu vrstev v danem adresari


# for cyklus prochazejici vrstvy v danem adresari
    # zjisteni poctu prvku v dane vrstve
    # vyzkousejte:
        # pocet = arcpy.management.GetCount(v)
        # print(pocet)
        # print(type(pocet))
        # print(pocet[0])
        # print(type(pocet[0]))
        # jak prevest na cislo?

    # pokud je pocet vetsi nez 0 - kopirovani vrstvy
    # arcpy.CopyFeatures_management(..., ...)




#####################################
# UKOLY NAVIC:
# 1) upravte skript tak, aby databazi pro ulozeni neprazdnych vrstev vytvoril sam
# 2) upravte skript, aby na konci vypsal seznam a pocet prazdnych vrstev

