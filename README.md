# SoncneElektrarne
Projektna naloga iz analize podatkov pri predmetu Programiranje 1

Zajel in analiziral bom navedene sončne elektrarne na spletnem mestu 
http://pv.fe.uni-lj.si/Seseznam.aspx in http://pv.fe.uni-lj.si/SESeznam_neto.aspx. 
V prvem spletnem mestu so navedene sončne elektrarne v ne samooskrbi, na drugem pa 
sončne elektrarne v samooskrbi. 

Zajel bom naslednje podatke:
* Ime sončne elektrarne, 
* Kraj postavitve sončne elektrarne, 
* Regijo,
* Leto izgradnje sončne elektrarne,
* Moč sončne elektrarne v kW.

Na podlagi teh podatkov nameravam preveriti: 
* Kako se spreminja število sončnih elektraren skozi leta.
* Po katerih regijah in krajih je največ interesa za sončne elektrarne in trend skozi leta. 
* Moč sončnih elektrarn po regijah in trend skozi leta.
* Je več šibkejših ali močnejših sončnih elektrarn.

Dodana je CSV datoteka s podatki, ki jih bom analiziral. Poleg tega, je v reporzitoriju 
še mapa z HTML datotekami strani s katerih sem prevzel podatke in python skripta, v kateri 
iz HTML datoteke izluščim podatke in jih pretvorim v CSV datoteko. HTML strani so kopirane, saj 
se pri filtrih ne spreminja URL spletne strani zato mi ni uspelo pridobiti podatkov s knjižnjico 
request.

Za pravilno delovanje je potrebno imeti nameščeno knjižnjico pandas. 
Za pravilno delovanje python skripte podatki.py je potrebno biti v takem directory-u, da lahko iz njega pridemo v 
mapo SoncneElektrarne. Torej, da je mapa SoncneElektrarne v trenutnem directoriyu. (Pot do datoteke naj bo predstavljena kot 
"SoncneElektrarne/...").
