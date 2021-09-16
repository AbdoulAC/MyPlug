#!/usr/bin/python3
# -*-coding:Utf-8 -*

import webbrowser



Sites = {
         "Noir fonce":"https://www.noirfonce.fr/",
         "AFEW":"https://de.afew-store.com/collections/sneaker-releases",
         "12amrun":"https://www.12amrun.com/",
         "ATCS":"https://www.abovethecloudsstore.com/",
         "addict Miami":"https://www.addictmiami.com/",
         "alife":"https://alifenewyork.co.uk/",
         "Alumni":"https://www.tha-alumni.com/",
         "amamaniere":"https://www.a-ma-maniere.com/?lang=fr",
         "amongstfew":"https://www.amongstfew.com/",
         "ASSC":"https://www.antisocialsocialclub.com/",
         "APBstore":"https://www.apbstore.com/",
         "AstoreIsgood":"",
         "Atmosny":"https://fr-atmosny.glopalstore.com/?utm_campaign=hp_r&utm_source=https://atmosny.com&utm_medium=wi_proxy&utm_content=en_US&utm_term=a",
         "bape":"https://www.bapeonline.com/",
         "bapefr":"https://bapefrance.com/",
         "bb branded":"https://www.bbbranded.com/",
         "BBC":"https://www.bbcicecream.com/",
         "bodega":"https://bdgastore.com/",
         "bianca chandon":"https://biancachandon.com/",
         "blends":"https://www.blendsus.com/",
         "BAAB":"https://www.bowsandarrowsberkeley.com/",
         "BRS":"https://burnrubbersneakers.com/",
         "Capsuletoronto":"https://www.capsuletoronto.com/",
         "centre":"https://www.centretx.com/",
         "City Blue":"https://www.cityblueshop.com/",
         "Cncpts":"https://cncpts.com/",
         "cmwftg":"https://commonwealth-ftgg.com/",
         "concrete":"https://concrete.store/",
         "concretenl":"https://concrete.nl/",
         "courtsidesnkrs":"https://www.courtsidesneakers.com/",
         "deadstock":"https://www.deadstock.ca/",
         "doomsday":"https://doomsdayco.com/",
         "dopefactory":"https://www.dope-factory.com/",
         "dsmflashjp":"https://shop.doverstreetmarket.com/jp/",
         "dsmflashuk":"https://shop.doverstreetmarket.com/whats-new",
         "dsmflashus":"https://eflash-us.doverstreetmarket.com/password",
         "dsmflashsg":"https://shop.doverstreetmarket.com/sg/",
         "exclucity":"https://shop.exclucitylife.com/",
         "extrabutterny":"https://extrabutterny.com/",
         "FSB":'https://feature.com/',
         "fice gallery":"https://www.ficegallery.com/",
         "freshrgfl":"https://freshragsfl.com/",
         "funico shop":"https://www.funko.com/",
         "FTP":"https://fuckthepopulation.com/",
         "gag":"https://goodasgoldshop.com/",
         "hamon":"https://www.hanon-shop.com/",
         "hal":"https://www.highsandlows.net.au/",
         "hombreamsterdam":"https://www.hombreofficial.com/",
         "hunting lodge":"https://www.huntinglodge.no/",
         "john Elliott":"https://www.johnelliott.com/",
         "justdon":"https://justdon.com/",
         "kith":"https://kith.com/",
         "kong":"https://www.kongonline.co.uk/",
         "kyliecsm":"https://www.kyliecosmetics.com/",
         "OVO UK":"https://uk.octobersveryown.com/",
         "offthehook":"https://offthehook.ca/",
         "oipolloi":"https://www.oipolloi.com/",
         "oneness 287":"https://www.onenessboutique.com/",
         "packer shoes":"https://packershoes.com/",
         "palace eu":"https://shop.palaceskateboards.com/",
         "pampamldn":"https://pampamlondon.com/",
         "proper lbc":"https://properlbc.com/",
         "reigning champ":"https://reigningchamp.com/",
         "renarts":"https://renarts.com/",
         "rime NYC":"https://www.rimenyc.com/",
         "rise 45":"https://crusoeandsons.com/",
         "rock city kicks":"https://rockcitykicks.com/",
         "rsvp gallery":"https://rsvpgallery.com/",
         "shiekh":"https://www.shiekh.com/",
         "westnyc":"https://www.westnyc.com/",
         "wishatl":"https://wishatl.com/",
         "Xhibition":"https://www.xhibition.co/",
         "yeezysupeu":"https://www.yeezysupply.com/",
          }

while True:
    print("Sur quel site allons nous ?")
    print("\n")
    print("press q to quit")
    for keys in Sites:
        print(keys)

    print("\n")
    site=input()

    if site in Sites:
        url = (Sites[site])




        # MacOS
        #chrome_path = 'open -a /Applications/Google\ Chrome.app %s'

        # Windows
        # chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'

        #Linux
        chrome_path = '/usr/bin/google-chrome %s'
        webbrowser.get(chrome_path).open(url)
        print("\n")
    elif site == "q":
        sys.exit()
    else :
        break            
