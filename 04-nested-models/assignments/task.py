from pydantic import BaseModel
from typing import List

# TODO: Create Course model
# Each Course has modules
# Each Module has lessons


class Lesson(BaseModel):
    lessons_id: int
    topic: str


class Module(BaseModel):
    modules_id: int
    name: str
    lessons: List[Lesson]


class Course(BaseModel):
    course_id: int
    title: str
    modules: List[Module]


course1 = Course(
    course_id=1,
    title="ICT Study",
    modules=[
        Module(
            modules_id=1,
            name="Junayed",
            lessons=[
                Lesson(
                    lessons_id=1,
                    topic="ICT",
                ),
            ],
        ),
    ],
)

print("\n\n", course1, "\n\n")
