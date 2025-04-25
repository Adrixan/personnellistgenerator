from tabletooling import create_teacher_table, create_admin_table
import datetime

x = datetime.datetime.now()

def create_overview(teachers, admins):
    datestring = x.strftime("%Y-%m-%d")

    result = '''
+++
identifier = "personen"
date = "'''

    result = result + datestring + '''"
draft = false
+++
{{< rawhtml >}}
<h1>Administratives Personal:</h1>


'''

    result = result + create_admin_table(admins) + '''

<h1>Lehrer:innen:</h1>
<p>Für mehr Informationen, bitte den Namen auswählen!</p>
'''

    result = result + create_teacher_table(teachers) + '''

    <script>
        new DataTable('#teachers');
        new DataTable('#admins', {order: [[2, 'desc']]});
    </script>
{{< /rawhtml >}}
'''

    return result