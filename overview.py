from tabletooling import create_teacher_table, create_admin_table
import datetime

x = datetime.datetime.now()

def create_overview_teachers(teachers):
    datestring = x.strftime("%Y-%m-%d")

    result = '''
+++
identifier = "lehrpersonal"
date = "'''

    result = result + datestring + '''"
draft = false
+++

'''

    result = result +  '''
{{< rawhtml >}}
<h1>Lehrer:innen:</h1>
<p>Die Kommunikation zwischen Erziehungsberechtigten und der Lehrerschaft erfolgt ausschließlich über WebUntis.</p> 
<p>Sollte WebUntis nicht zur Verfügung stehen, können Sie uns jederzeit per E-Mail - Vorname.Nachname@petersgasse.at - kontaktieren.</p>
<p>Für mehr Informationen, bitte den Namen auswählen!</p>
'''

    result = result + create_teacher_table(teachers) + '''

    <script>
        new DataTable('#teachers', { columnDefs: [{ target: 0, visible: false, searchable: false}]});
    </script>
{{< /rawhtml >}}
'''

    return result

def create_overview_admins(admins):
    datestring = x.strftime("%Y-%m-%d")

    result = '''
+++
identifier = "adminpersonen"
date = "'''

    result = result + datestring + '''"
draft = false
+++
{{< rawhtml >}}
<h1>Administratives Personal:</h1>

Für Kontaktmöglichkeiten, sowie Sprechstundentermine, klicken Sie bitte auf die entsprechende Person!


'''

    result = result + create_admin_table(admins) + '''

    <script>
        new DataTable('#admins', {order: [[2, 'desc']]});
    </script>
{{< /rawhtml >}}
'''

    return result
