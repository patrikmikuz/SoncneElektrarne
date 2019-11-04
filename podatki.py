import re
import pandas as pd

regije = ['Celjska', 'Dolenjska', 'Gorenjska', 'Goriska', 'OsrednjaSlovenija', 'Podravje', 'Prekmurje', 'Primorska']

def get_block(regija):
    datoteka = 'SoncneElektrarne/html/' + regija + '.html'
    with open (datoteka, 'r', encoding = 'utf8') as file:
        string = file.read()
        elektrarne = re.findall('(<td style=\"text-align:left;\">.*?<\/td>\s)', string, re.DOTALL)
    return elektrarne 

def get_dict(block):
    exp = '<td.*?;\">(?P<Ime>.*?)<\/td>.*<td>(?P<Kraj>.*?)<\/td><td .*?>(?P<Leto>.*?)<\/td><td .*?>(?P<Moc>.*?)<\/td>'
    data = re.search(exp, block, re.DOTALL)
    slovar = data.groupdict()
    return slovar

def get_block_samooskrba(regija):
    datoteka = 'SoncneElektrarne/html/' + regija + 'Samooskrba.html'
    with open (datoteka, 'r', encoding = 'utf8') as file:
        string = file.read()
        elektrarne = re.findall('(<td align="left">.*?<\/td>\s)', string, re.DOTALL)
    return elektrarne 

def get_dict_samooskrba(block):
    exp = '<td.*?>(?P<Kraj>.*?)<\/td><td.*?>(?P<Moc>.*?)<\/td><td.*?>(?P<Leto>.*?)<\/td>'
    data = re.search(exp, block, re.DOTALL)
    slovar = data.groupdict()
    return slovar

tipi = {'Ime': str, 'Kraj': str, 'Leto': int, 'Moc [kW]': float, 'Regija': str}

SoncneElektrarne = []
Stolpci = ['Ime', 'Kraj', 'Leto', 'Moc [kW]', 'Regija']

for regija in regije:
    elektrarne = get_block(regija)
    slovarji = [get_dict(elektrarna) for elektrarna in elektrarne]
    for slovar in slovarji:
        elektrarna = list(slovar.values())
        elektrarna.append(regija)
        SoncneElektrarne.append(elektrarna)

SoncneElektrarne = pd.DataFrame(SoncneElektrarne)
SoncneElektrarne.columns = Stolpci
SoncneElektrarne['Moc [kW]'] = [element.replace(',', '.') for element in SoncneElektrarne['Moc [kW]']]
SoncneElektrarne.astype(tipi)


SoncneElektrarneSamooskrba = []

for regija in regije:
    elektrarne = get_block_samooskrba(regija)
    slovarji = [get_dict_samooskrba(elektrarna) for elektrarna in elektrarne]
    for slovar in slovarji:
        elektrarna = ['Samooskrba'] + list(slovar.values())
        elektrarna.append(regija)
        SoncneElektrarneSamooskrba.append(elektrarna)

SoncneElektrarneSamooskrba = pd.DataFrame(SoncneElektrarneSamooskrba)
SoncneElektrarneSamooskrba.columns = ['Ime', 'Kraj', 'Moc [kW]', 'Leto', 'Regija']
SoncneElektrarneSamooskrba = SoncneElektrarneSamooskrba[['Ime', 'Kraj', 'Leto', 'Moc [kW]', 'Regija']]
SoncneElektrarneSamooskrba['Moc [kW]'] = [element.replace(',', '.') for element in SoncneElektrarneSamooskrba['Moc [kW]']]
SoncneElektrarneSamooskrba.astype(tipi)

SkupnaTabela = pd.concat([SoncneElektrarneSamooskrba, SoncneElektrarne]) 

SkupnaTabela.to_csv('SoncneElektrarne/podatki.csv')
