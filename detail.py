from classes import Teacher
import datetime, os, sys
from PIL import Image

x = datetime.datetime.now()

def create_details(teachers, basedir, imgdir, imgsourcedir, imgoutdir):
    for teacher in teachers:
        with open(basedir + "personal/" + teacher.name + "-" + teacher.surname + ".md", "w") as f:
            f.write(create_detail(teacher, imgdir, imgsourcedir, imgoutdir))

def prepare_image(name, sourceimage, imgoutdir):
    size = 400, 400
    outfile = imgoutdir + name + ".jpg"
    if not os.path.isfile(sourceimage):
        sourceimage = sourceimage.replace(".jpg", ".JPG")
        print(sourceimage)
        if not os.path.isfile(sourceimage):
            print(f"No image for: {name}")
            return

    try:
        im = Image.open(sourceimage)
        im.thumbnail(size, Image.Resampling.LANCZOS)
        im.save(outfile, "JPEG")
    except IOError:
        print("cannot create thumbnail for '%s'" % sourceimage)
    


def create_detail(teacher, imgdir, imgsourcedir, imgoutdir):
    print(f"Working on {teacher.surname}")
    datestring = x.strftime("%Y-%m-%d")

    prepare_image(teacher.surname, imgsourcedir + teacher.surname+".jpg", imgoutdir)

    result = f'''
+++
identifier = "{teacher.name.lower}-{teacher.surname.lower}"
date = "{datestring}"
draft = false
+++

<div class="row">
<div class="column">
<img src="{imgdir}{teacher.surname}.jpg" alt="{teacher.name} {teacher.surname}"> 
</div>
<div class="column">

# {teacher.name} {teacher.surname}

Sprechstunde am {teacher.officehour_day} um {teacher.officehour_lesson}

Fächer: {', '.join(teacher.subjects)}

{f"KV der {teacher.kv}" if teacher.kv else ""}

{f"KV (Stellvertretung) der {teacher.kvstv}" if teacher.kvstv else ""}

{"## Kurse" if teacher.courses_1 or teacher.courses_2 else ""}

{f"Unterstufe: {', '.join(teacher.courses_1)}" if teacher.courses_1 else ""}

{f"Oberstufe: {', '.join(teacher.courses_2)}" if teacher.courses_2 else ""}

{f"Koordination für: {teacher.coordinator}" if teacher.coordinator else ""}

</div>
</div> 

'''
# TODO Add Nachmittagsbetreuung
# Nachmittagsbetreuung: {teacher.afternoon}

    return result
