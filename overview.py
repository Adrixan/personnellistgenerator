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
<p>Für mehr Informationen, bitte den Namen auswählen!</p>
'''

    result = result + create_teacher_table(teachers) + '''

    <script>
        new DataTable('#teachers');
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


'''

    result = result + create_admin_table(admins) + '''

    <script>
        new DataTable('#admins', {order: [[2, 'desc']]});
    </script>
{{< /rawhtml >}}
'''

    return result