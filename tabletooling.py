from classes import Teacher, Admin

def create_teacher_table(teachers):
    result = '''
    <table id="teachers" class="display" style="width:100%">
        <thead>
            <tr>
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

    for t in teachers:
        name = t.name.replace(' ', '-')
        surname = t.surname.replace(' ', '-')
        result = result + f'''
            <tr>
                <td><a href=/schule/personal/{name.lower()}-{surname.lower()}/>{t.build_name_short()}</a></td>
                <td>{t.untis}</td>
                <td>{t.officehour_day}</td>
                <td>{t.officehour_lesson}</td>
                <td>{t.kv}</td>
                <td>{t.kvstv}</td>
            </tr>
        '''

    result = result + '''
        </tbody>
        <tfoot>
            <tr>
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
