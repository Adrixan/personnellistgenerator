from dataclasses import dataclass

@dataclass
class Teacher:
    title_pre: str
    name: str
    surname: str
    title_post: str
    kv: str
    kvstv: str
    untis : str
    subjects: list
    courses_1: list
    courses_2: list
    coordinator: str
    officehour_day: str
    officehour_lesson: int
    officehour_room: str
    afternoon: bool
    remarks: str
    img: bool

    def build_name(self):
        name = ""
        if self.title_pre is not None:
            name = name + self.title_pre + " "
        name = name + self.surname + " " + self.name
        if self.title_post is not None:
            name = name + " " + self.title_post
        return(name)

    def build_name_short(self):
        return(self.surname + " " + self.name)

@dataclass
class Admin:
    function: str
    title_pre: str
    name: str
    surname: str
    email: str
    tel: str
    officehour: str
    img: bool

    def build_name(self):
            name = ""
            if self.title_pre is not None:
                name = name + self.title_pre + " "
            name = name + self.surname + " " + self.name
#            if self.title_post is not None:
#                name = name + " " + self.title_post
            return(name)

    def build_name_short(self):
        return(self.surname + " " + self.name)


