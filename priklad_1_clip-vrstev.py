import arcpy    # importovani knihovny, ktera umoznuje pouzivat funkce ArcGIS Pro

# nastaveni workspace - defaultniho ("domovskeho") adresare, tedy adresare, ve kterem budeme dale pracovat
# adresar muze byt typicky slozka nebo geodatabaze
# cesta k adresari musi byt v uvozovkach s klasickymi lomitky ".../..."
arcpy.env.workspace = "U:/2024-25/GIS_4/automatizace_python/autom_python/data_priklad/priklad_2"

# funkce, ktera vylistuje vsechny vrstvy (feature class nebo shapefile) v danem adresari (urcenem v predeslem kroku)
# funkce vraci vrstvy v podobe seznamu, ktery je ukladan do zvolene promenne, aby s nim mohlo byt dale pracovano
vrstvy = arcpy.ListFeatureClasses()

# vypis seznamu vrstev v zadanem adresari
print(vrstvy)


# for cyklus, ktery prochazi seznam vrstev z predchoziho kroku
# promenna v slouzi jako zastupna promenna pro dany prvek seznamu, ktery je zrovna prochazen
# postupne jsou do promenne v "dosazovany" jednotlive prvky (vrstvy) ze seznamu
# cyklus probehne tolikrat, kolik je vrstev v seznamu, resp. danem adresari
for v in vrstvy:
    print(v)    # vypise nazev dane vrstvy 

    # podminka, ve ktere je vyhodnoceno, jestli ma dana vrstva nazev "moje_obec.shp"
    # duvodem je, ze nechceme, aby byla funkce clip spustena se stejnou vstupni a orezavaci vrstvou
    # pokud se dana vrstva nejmenuje "moje_obec.shp", tak se vykona kod uvnitr podminky
    if v != 'moje_obec.shp':
        # vytvoreni promennych pro spusteni funkce clip
        # parametry funkce clip jsou 3: vstupni vrstva (in_f), orezavaci vrstva (clip_f) a vystup (out_f)
        in_f = v    # vstupni vrstva, ktera ma byt oriznuta - postupne jsou oriznuty vsechny vrstvy v adresari
        # v kazdem behu cyklu je oriznuta jina vrstva (v)
        clip_f = 'moje_obec.shp'    # orezavaci vrstva - tou je vrstva "moje_obec.shp"
        out_f = f"clip_{v}"     # vytvoreni nazvu vstupu ve tvaru "clip_nazev"
        # nazvy vrstev jsou psany pouze takto, bez cele cesty, jelikoz se nachazi v definovanem adresari
        
        # pokud bychom chteli vystup ulozit na jine misto, nebo pouzit napr. jinde umistejnou orezavaci vrstvu, 
        # tak je treba na ne odkazat celou jejich cestou,
        # napr: out_f = "U:/2024-25/GIS_4/automatizace_python/vystupy.gdb/vystup"

        # spusteni funkce clip s pripravenymi parametry
        arcpy.analysis.Clip(in_f, clip_f, out_f)




print("konec")