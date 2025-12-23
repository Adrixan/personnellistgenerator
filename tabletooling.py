from classes import Teacher, Admin

def create_teacher_table(teachers):
    result = '''
    <table id="teachers" class="display" style="width:100%">
        <thead>
            <tr>
                <th>Laufnummer</th>
                <th>Name</th>
                <th>Kürzel</th>
                <th>Tag der Sprechstunde</th>
                <th>Sprechstunde</th>
                <th>KV:in</th>
                <th>KV:in (Stellvertretung)</th>
            </tr>
        </thead>
        <tbody>
    '''
    number = 0
    for t in teachers:
        name = t.name.replace(' ', '-')
        surname = t.surname.replace(' ', '-')
        tempnum = number
        short_name = t.build_name_short()
        if t.remarks is not None and "Schulleiter" in t.remarks:
            tempnum = -2
            short_name = "Schulleiter " + short_name
        if t.remarks is not None and "Administrator" in t.remarks:
            tempnum = -1
            short_name = "Administrator " + short_name

        result = result + f'''
            <tr>
                <td>{tempnum}</td>
                <td><a href=/schule/personal/{name.lower()}-{surname.lower()}/>{short_name}</a></td>
                <td>{t.untis}</td>
                <td>{t.officehour_day}</td>
                <td>{t.officehour_lesson}</td>
                <td>{t.kv}</td>
                <td>{t.kvstv}</td>
            </tr>
        '''
        number +=1

    result = result + '''
        </tbody>
        <tfoot>
            <tr>
                <th>Laufnummer</th>
                <th>Name</th>
                <th>Kürzel</th>
                <th>Tag der Sprechstunde</th>
                <th>Sprechstunde</th>
                <th>KV:in</th>
                <th>KV:in (Stellvertretung)</th>
            </tr>
        </tfoot>
    </table>
    '''
    return result

def create_admin_table(admins):
    result = '''
    <table id="admins" class="display" style="width:100%">
        <thead>
            <tr>
                <th>Name</th>
                <th>Funktion</th>
            </tr>
        </thead>
        <tbody>
    '''

    for a in admins:
        name = a.name.replace(' ', '-')
        surname = a.surname.replace(' ', '-')
        result = result + f'''
            <tr>
                <td><a href=/schule/personal/{name.lower()}-{surname.lower()}/>{a.build_name_short()}</a></td>
                <td>{a.function}</td>
            </tr>
        '''

    result = result + '''
        </tbody>
        <tfoot>
            <tr>
                <th>Name</th>
                <th>Funktion</th>
            </tr>
        </tfoot>
    </table>
    '''
    return result
