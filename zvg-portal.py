import requests, mysql.connector as mysqli
from bs4 import BeautifulSoup

try:
    server = mysqli.connect(host="localhost", user="root", password="root")
except:
    raise Exception("There is something problem with MySQL Server..")
cursor = server.cursor()

cursor.execute("CREATE DATABASE IF NOT EXISTS website_info;")
cursor.execute("USE website_info;")
cursor.execute("CREATE TABLE IF NOT EXISTS `website_info`.`zvg-portal`(`id` VARCHAR(150) NOT NULL, `Amtsgericht` VARCHAR(255) NULL, `Objekt_lake` VARCHAR(255) NULL, `Verkehrswert_EUR` VARCHAR(30) NULL,`Termin` VARCHAR(100) NULL, `has_pdf` TINYINT(4) NULL, PRIMARY KEY (`id`)) ENGINE = InnoDB DEFAULT CHARACTER SET = utf8mb4;")

location = {'bw': 'Baden-Wuerttemberg', 'by':'Bayern','be':'Berlin', 'br':'Brandenburg', 'hb':'Bremen','hh':'Hamburg','he':'Hessen','mv':'Mecklenburg-Vorpommern','ni':'Niedersachsen','nw':'Nordrhein-Westfalen', 'rp':'Rheinland-Pfalz','sl':'Saarland','sn':'Sachsen', 'st':'Sachsen-Anhalt','sh':'Schleswig-Holstein', 'th':'Thuringen'}
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36", "Referer":"https://www.zvg-portal.de/index.php?button=Termine%20suchen"}
data={'land_abk':'{}', 'ger_id':0, 'order_by':2, 'ger_name': '-- Alle Amtsgerichte --'}
main_url = "https://www.zvg-portal.de/index.php?button=Suchen&all=1"