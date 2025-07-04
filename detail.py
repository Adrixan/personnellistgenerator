from classes import Teacher
import datetime, os, sys, shutil
from PIL import Image

x = datetime.datetime.now()

def create_details(teachers, basedir, imgdir, imgsourcedir, imgoutdir):
    for teacher in teachers:
        name = teacher.name.replace(' ', '-')
        surname = teacher.surname.replace(' ', '-')
        with open(basedir + "personal/" + name + "-" + surname + ".md", "w") as f:
            f.write(create_detail(teacher, imgdir, imgsourcedir, imgoutdir))

def prepare_image(name, imgsourcedir, imgoutdir, img):
    size = 400, 400
    outfile = imgoutdir + name + ".jpg"
    sourceimage = imgsourcedir + name+".jpg"
    if not os.path.isfile(sourceimage) or not img:
        sourceimage = sourceimage.replace(".jpg", ".JPG").replace('ß','ss')
#        print(sourceimage)
        if not os.path.isfile(sourceimage) or not img:
            print(f"No image for: {name}")
            shutil.copy(imgsourcedir + "_generic_teacher.jpg", imgoutdir + name + ".jpg")
            return

    try:
        im = Image.open(sourceimage)
        im.thumbnail(size, Image.Resampling.LANCZOS)
        im.save(outfile, "JPEG")
    except IOError:
        print("cannot create thumbnail for '%s'" % sourceimage)
    


def create_detail(teacher, imgdir, imgsourcedir, imgoutdir):
#    print(f"Working on {teacher.surname}")
    datestring = x.strftime("%Y-%m-%d")


    prepare_image(teacher.surname, imgsourcedir, imgoutdir, teacher.img)

    result = f'''
+++
identifier = "{teacher.name.lower}-{teacher.surname.lower}"
date = "{datestring}"
draft = false
+++

 [Zurück zur Übersicht](/schule/lehrpersonal/)

<div class="row">
<div class="column">
<img src="{imgdir}{teacher.surname}.jpg" alt="{teacher.name} {teacher.surname}"> 
</div>
<div class="column">

# {teacher.build_name()}

Sprechstunde am {teacher.officehour_day} um {teacher.officehour_lesson}

Fächer: {', '.join(teacher.subjects)}

{f"KV der {teacher.kv}" if teacher.kv else ""}

{f"KV (Stellvertretung) der {teacher.kvstv}" if teacher.kvstv else ""}

{"## Kurse" if teacher.courses_1 or teacher.courses_2 else ""}

{f"Unterstufe: {', '.join(teacher.courses_1)}" if teacher.courses_1 else ""}

{f"Oberstufe: {', '.join(teacher.courses_2)}" if teacher.courses_2 else ""}

{f"Koordination für: {teacher.coordinator}" if teacher.coordinator else ""}

{f"Nachmittagsbetreuung" if teacher.afternoon else ""}

</div>
</div> 

'''


    return result
