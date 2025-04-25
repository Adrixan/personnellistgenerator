from dataclasses import dataclass

@dataclass
class Teacher:
    title_pre: str
    name: str
    surname: str
    title_post: str
    kv: str
    kvstv: str
    subjects: list
    courses_1: list
    courses_2: list
    coordinator: str
    officehour_day: str
    officehour_lesson: int
    afternoon: bool
    remarks: str

    def build_name(self):
        name = ""
        if self.title_pre is not None:
            name = name + self.title_pre + " "
        name = name + self.name + " " + self.surname
        if self.title_post is not None:
            name = name + " " + self.title_post
        return(name)

@dataclass
class Admin:
    function: str
    title_pre: str
    name: str
    surname: str
#    title_post: str
    def build_name(self):
            name = ""
            if self.title_pre is not None:
                name = name + self.title_pre + " "
            name = name + self.name + " " + self.surname
#            if self.title_post is not None:
#                name = name + " " + self.title_post
            return(name)