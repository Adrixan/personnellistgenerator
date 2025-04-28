from exceltooling import convert_excel_to_admins, convert_excel_to_teachers
from tabletooling import create_teacher_table, create_admin_table
from overview import create_overview
from detail import create_details
import datetime

x = datetime.datetime.now()
basedir = "../petersgasse.at/content/de/Schule/"
imgdir = "/images/personal/"
imgsourcedir = "../lehrerfotos/"
imgoutdir = "../petersgasse.at/static/images/personal/"

excelname = "../lehrerfotos/Lehrer_Verwaltung.xlsx"

teachers = convert_excel_to_teachers(excelname)
admins = convert_excel_to_admins(excelname)


with open(basedir + "personen.md", "w") as f:
    f.write(create_overview(teachers, admins))

create_details(teachers, basedir, imgdir, imgsourcedir, imgoutdir)