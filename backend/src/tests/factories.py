import factory

from backend.database import session
from backend.src.models import Project

sample_geo_data = {
    "type": "Feature",
    "geometry": {
        "type": "MultiPolygon",
        "coordinates": [
            [
                [
                    [-52.8430645648562, -5.63351005831322],
                    [-52.8289481608136, -5.674529420529012],
                    [-52.8114438198008, -5.6661010219506664],
                    [-52.797327415758296, -5.654301057317909],
                    [-52.788292917171, -5.651491506446291],
                    [-52.7803877309072, -5.640815088854069],
                    [-52.7555428597923, -5.641377010471558],
                    [-52.738603174941204, -5.63800547260297],
                    [-52.729568676354, -5.631262338119598],
                    [-52.719404865443295, -5.626204935899693],
                    [-52.709241054532704, -5.616089999567166],
                    [-52.6708444355369, -5.569446637469866],
                    [-52.6787496218007, -5.558206718303779],
                    [-52.687784120388, -5.534602190108217],
                    [-52.7098057106944, -5.5390983634896],
                    [-52.7244867708986, -5.546404572245265],
                    [-52.7600601090859, -5.5722565836830285],
                    [-52.7843403240391, -5.584058210883924],
                    [-52.8074912266689, -5.589115978388449],
                    [-52.823301599196604, -5.618337778382639],
                    [-52.8385473155626, -5.620585548523252],
                    [-52.8430645648562, -5.63351005831322],
                ]
            ]
        ],
    },
}


class ProjectFactory(factory.alchemy.SQLAlchemyModelFactory):
    class Meta:
        model = Project
        sqlalchemy_session = session.Session
        sqlalchemy_session_persistence = "commit"

    id = factory.Sequence(lambda i: i)
    name = factory.Faker("pystr")
    description = factory.Faker("pystr")
    date_start = factory.Faker("date_time")
    date_end = factory.Faker("date_time")
    geo_json = sample_geo_data
