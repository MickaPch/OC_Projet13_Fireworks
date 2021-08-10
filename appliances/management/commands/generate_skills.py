import os
import json
import random

from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """Command to create appliance skills fixture for tests"""

    def handle(self, *args, **kwargs):
        """Create appliance skills fixture"""

        print('Appliance skills fixture creation ...')

        model = "appliances.Skill"

        skills = [
            {
                "model": model,
                "pk": 1,
                "fields": {
                    "name": "Java", "image": "", "related": None, "type": "0"
                }
            },
            {
                "model": model,
                "pk": 2,
                "fields": {
                    "name": "Python", "image": "", "related": None, "type": "0"
                }
            },
            {
                "model": model,
                "pk": 3,
                "fields": {
                    "name": "PHP", "image": "", "related": None, "type": "0"
                }
            },
            {
                "model": model,
                "pk": 4,
                "fields": {
                    "name": "C#", "image": "", "related": None, "type": "0"
                }
            },
            {
                "model": model,
                "pk": 5,
                "fields": {
                    "name": "C", "image": "", "related": None, "type": "0"
                }
            },
            {
                "model": model,
                "pk": 6,
                "fields": {
                    "name": "C++", "image": "", "related": None, "type": "0"
                }
            },
            {
                "model": model,
                "pk": 7,
                "fields": {
                    "name": "JavaScript", "image": "", "related": None, "type": "0"
                }
            },
            {
                "model": model,
                "pk": 8,
                "fields": {
                    "name": "Objective-C", "image": "", "related": None, "type": "0"
                }
            },
            {
                "model": model,
                "pk": 9,
                "fields": {
                    "name": "R", "image": "", "related": None, "type": "0"
                }
            },
            {
                "model": model,
                "pk": 10,
                "fields": {
                    "name": "Swift", "image": "", "related": None, "type": "0"
                }
            },
            {
                "model": model,
                "pk": 11,
                "fields": {
                    "name": "Matlab", "image": "", "related": None, "type": "0"
                }
            },
            {
                "model": model,
                "pk": 12,
                "fields": {
                    "name": "Ruby", "image": "", "related": None, "type": "0"
                }
            },
            {
                "model": model,
                "pk": 13,
                "fields": {
                    "name": "VBA", "image": "", "related": None, "type": "0"
                }
            },
            {
                "model": model,
                "pk": 14,
                "fields": {
                    "name": "Visual Basic", "image": "", "related": None, "type": "0"
                }
            },
            {
                "model": model,
                "pk": 15,
                "fields": {
                    "name": "Scala", "image": "", "related": None, "type": "0"
                }
            },
            {
                "model": model,
                "pk": 16,
                "fields": {
                    "name": "Perl", "image": "", "related": None, "type": "0"
                }
            },
            {
                "model": model,
                "pk": 17,
                "fields": {
                    "name": "lua", "image": "", "related": None, "type": "0"
                }
            },
            {
                "model": model,
                "pk": 18,
                "fields": {
                    "name": "Delphi", "image": "", "related": None, "type": "0"
                }
            },
            {
                "model": model,
                "pk": 19,
                "fields": {
                    "name": "Go", "image": "", "related": None, "type": "0"
                }
            },
            {
                "model": model,
                "pk": 20,
                "fields": {
                    "name": "Haskell", "image": "", "related": None, "type": "0"
                }
            },
            {
                "model": model,
                "pk": 21,
                "fields": {
                    "name": "Assembly", "image": "", "related": None, "type": "0"
                }
            },
            {
                "model": model,
                "pk": 22,
                "fields": {
                    "name": "VB.NET", "image": "", "related": None, "type": "0"
                }
            },
            {
                "model": model,
                "pk": 23,
                "fields": {
                    "name": "Groovy", "image": "", "related": None, "type": "0"
                }
            },
            {
                "model": model,
                "pk": 24,
                "fields": {
                    "name": "SQL", "image": "", "related": None, "type": "0"
                }
            },
            {
                "model": model,
                "pk": 25,
                "fields": {
                    "name": "iOS", "image": "", "related": None, "type": "4"
                }
            },
            {
                "model": model,
                "pk": 26,
                "fields": {
                    "name": "HTML", "image": "", "related": None, "type": "0"
                }
            },
            {
                "model": model,
                "pk": 27,
                "fields": {
                    "name": "CSS", "image": "", "related": None, "type": "0"
                }
            },
            {
                "model": model,
                "pk": 28,
                "fields": {
                    "name": "Shell", "image": "", "related": None, "type": "0"
                }
            },
            {
                "model": model,
                "pk": 29,
                "fields": {
                    "name": "Arduino", "image": "", "related": None, "type": "0"
                }
            },
            {
                "model": model,
                "pk": 30,
                "fields": {
                    "name": "Rust", "image": "", "related": None, "type": "0"
                }
            },
            {
                "model": model,
                "pk": 31,
                "fields": {
                    "name": "Django", "image": "", "related": "2", "type": "1"
                }
            },
            {
                "model": model,
                "pk": 32,
                "fields": {
                    "name": "Bottle", "image": "", "related": "2", "type": "1"
                }
            },
            {
                "model": model,
                "pk": 33,
                "fields": {
                    "name": "CherryPy", "image": "", "related": "2", "type": "1"
                }
            },
            {
                "model": model,
                "pk": 34,
                "fields": {
                    "name": "Flask", "image": "", "related": "2", "type": "1"
                }
            },
            {
                "model": model,
                "pk": 35,
                "fields": {
                    "name": "Pyramid", "image": "", "related": "2", "type": "1"
                }
            },
            {
                "model": model,
                "pk": 36,
                "fields": {
                    "name": "TurboGears", "image": "", "related": "2", "type": "1"
                }
            },
            {
                "model": model,
                "pk": 37,
                "fields": {
                    "name": "Twisted", "image": "", "related": "2", "type": "1"
                }
            },
            {
                "model": model,
                "pk": 38,
                "fields": {
                    "name": "Web2py", "image": "", "related": "2", "type": "1"
                }
            },
            {
                "model": model,
                "pk": 39,
                "fields": {
                    "name": "Zope", "image": "", "related": "2", "type": "1"
                }
            },
            {
                "model": model,
                "pk": 40,
                "fields": {
                    "name": "Apache Lucene", "image": "", "related": "1", "type": "1"
                }
            },
            {
                "model": model,
                "pk": 41,
                "fields": {
                    "name": "Apache Struts", "image": "", "related": "1", "type": "1"
                }
            },
            {
                "model": model,
                "pk": 42,
                "fields": {
                    "name": "Apache Tapestry", "image": "", "related": "1", "type": "1"
                }
            },
            {
                "model": model,
                "pk": 43,
                "fields": {
                    "name": "Google Guava", "image": "", "related": "1", "type": "1"
                }
            },
            {
                "model": model,
                "pk": 44,
                "fields": {
                    "name": "Hadoop", "image": "", "related": "1", "type": "1"
                }
            },
            {
                "model": model,
                "pk": 45,
                "fields": {
                    "name": "Hibernate", "image": "", "related": "1", "type": "1"
                }
            },
            {
                "model": model,
                "pk": 46,
                "fields": {
                    "name": "JavaFX", "image": "", "related": "1", "type": "1"
                }
            },
            {
                "model": model,
                "pk": 47,
                "fields": {
                    "name": "JavaServer Faces", "image": "", "related": "1", "type": "1"
                }
            },
            {
                "model": model,
                "pk": 48,
                "fields": {
                    "name": "JUnit", "image": "", "related": "1", "type": "1"
                }
            },
            {
                "model": model,
                "pk": 49,
                "fields": {
                    "name": "Play Framework", "image": "", "related": "1", "type": "1"
                }
            },
            {
                "model": model,
                "pk": 50,
                "fields": {
                    "name": "Qt Jambi", "image": "", "related": "1", "type": "1"
                }
            },
            {
                "model": model,
                "pk": 51,
                "fields": {
                    "name": "Spring", "image": "", "related": "1", "type": "1"
                }
            },
            {
                "model": model,
                "pk": 52,
                "fields": {
                    "name": "Zerocouplage", "image": "", "related": "1", "type": "1"
                }
            },
            {
                "model": model,
                "pk": 53,
                "fields": {
                    "name": "Laravel", "image": "", "related": "3", "type": "1"
                }
            },
            {
                "model": model,
                "pk": 54,
                "fields": {
                    "name": "Symfony", "image": "", "related": "3", "type": "1"
                }
            },
            {
                "model": model,
                "pk": 55,
                "fields": {
                    "name": "CodeIgniter", "image": "", "related": "3", "type": "1"
                }
            },
            {
                "model": model,
                "pk": 56,
                "fields": {
                    "name": "Zend Framework", "image": "", "related": "3", "type": "1"
                }
            },
            {
                "model": model,
                "pk": 57,
                "fields": {
                    "name": "Yii", "image": "", "related": "3", "type": "1"
                }
            },
            {
                "model": model,
                "pk": 58,
                "fields": {
                    "name": "CakePHP", "image": "", "related": "3", "type": "1"
                }
            },
            {
                "model": model,
                "pk": 59,
                "fields": {
                    "name": "Angular", "image": "", "related": "7", "type": "1"
                }
            },
            {
                "model": model,
                "pk": 60,
                "fields": {
                    "name": "AngularJS", "image": "", "related": "7", "type": "1"
                }
            },
            {
                "model": model,
                "pk": 61,
                "fields": {
                    "name": "Cappuccino", "image": "", "related": "7", "type": "1"
                }
            },
            {
                "model": model,
                "pk": 62,
                "fields": {
                    "name": "Ember.js", "image": "", "related": "7", "type": "1"
                }
            },
            {
                "model": model,
                "pk": 63,
                "fields": {
                    "name": "Prototype", "image": "", "related": "7", "type": "1"
                }
            },
            {
                "model": model,
                "pk": 64,
                "fields": {
                    "name": "React.js", "image": "", "related": "7", "type": "1"
                }
            },
            {
                "model": model,
                "pk": 65,
                "fields": {
                    "name": "Vue.js", "image": "", "related": "7", "type": "1"
                }
            },
            {
                "model": model,
                "pk": 66,
                "fields": {
                    "name": "Node.js", "image": "", "related": "7", "type": "1"
                }
            },
            {
                "model": model,
                "pk": 67,
                "fields": {
                    "name": "jQuery", "image": "", "related": "7", "type": "1"
                }
            },
            {
                "model": model,
                "pk": 68,
                "fields": {
                    "name": "Bootstrap", "image": "", "related": "27", "type": "1"
                }
            },
            {
                "model": model,
                "pk": 69,
                "fields": {
                    "name": "Rails", "image": "", "related": "12", "type": "1"
                }
            },
            {
                "model": model,
                "pk": 70,
                "fields": {
                    "name": "Drupal", "image": "", "related": "3", "type": "1"
                }
            },
            {
                "model": model,
                "pk": 71,
                "fields": {
                    "name": "BlueJ", "image": "", "related": "1", "type": "2"
                }
            },
            {
                "model": model,
                "pk": 72,
                "fields": {
                    "name": "Eclipse", "image": "", "related": "1", "type": "2"
                }
            },
            {
                "model": model,
                "pk": 73,
                "fields": {
                    "name": "AWS Cloud", "image": "", "related": None, "type": "2"
                }
            },
            {
                "model": model,
                "pk": 74,
                "fields": {
                    "name": "Windows", "image": "", "related": None, "type": "4"
                }
            },
            {
                "model": model,
                "pk": 75,
                "fields": {
                    "name": "MacOS", "image": "", "related": None, "type": "4"
                }
            },
            {
                "model": model,
                "pk": 76,
                "fields": {
                    "name": "Linux", "image": "", "related": None, "type": "4"
                }
            },
            {
                "model": model,
                "pk": 77,
                "fields": {
                    "name": "Ubuntu", "image": "", "related": "76", "type": "4"
                }
            },
            {
                "model": model,
                "pk": 78,
                "fields": {
                    "name": "Debian", "image": "", "related": "76", "type": "4"
                }
            },
            {
                "model": model,
                "pk": 79,
                "fields": {
                    "name": "Fedora", "image": "", "related": "76", "type": "4"
                }
            },
            {
                "model": model,
                "pk": 80,
                "fields": {
                    "name": "CodeLite", "image": "", "related": None, "type": "2"
                }
            },
            {
                "model": model,
                "pk": 81,
                "fields": {
                    "name": "UML", "image": "", "related": None, "type": "5"
                }
            },
            {
                "model": model,
                "pk": 82,
                "fields": {
                    "name": "Agile", "image": "", "related": None, "type": "5"
                }
            },
            {
                "model": model,
                "pk": 83,
                "fields": {
                    "name": "SCRUM", "image": "", "related": "82", "type": "5"
                }
            },
            {
                "model": model,
                "pk": 84,
                "fields": {
                    "name": "Kanban", "image": "", "related": "82", "type": "5"
                }
            },
            {
                "model": model,
                "pk": 85,
                "fields": {
                    "name": "NetBeans", "image": "", "related": None, "type": "2"
                }
            },
            {
                "model": model,
                "pk": 87,
                "fields": {
                    "name": "PhpStorm", "image": "", "related": "3", "type": "2"
                }
            },
            {
                "model": model,
                "pk": 92,
                "fields": {
                    "name": "PyCharm", "image": "", "related": "2", "type": "2"
                }
            },
            {
                "model": model,
                "pk": 93,
                "fields": {
                    "name": "AppCode", "image": "", "related": "25", "type": "2"
                }
            },
            {
                "model": model,
                "pk": 94,
                "fields": {
                    "name": "CLion", "image": "", "related": "5", "type": "2"
                }
            },
            {
                "model": model,
                "pk": 95,
                "fields": {
                    "name": "DataGrip", "image": "", "related": "24", "type": "2"
                }
            },
            {
                "model": model,
                "pk": 96,
                "fields": {
                    "name": "PostgreSQL", "image": "", "related": "24", "type": "0"
                }
            },
            {
                "model": model,
                "pk": 97,
                "fields": {
                    "name": "MySQL", "image": "", "related": "24", "type": "0"
                }
            },
            {
                "model": model,
                "pk": 98,
                "fields": {
                    "name": "MongoDB", "image": "", "related": "24", "type": "0"
                }
            },
            {
                "model": model,
                "pk": 99,
                "fields": {
                    "name": "Oracle", "image": "", "related": "24", "type": "0"
                }
            },
            {
                "model": model,
                "pk": 100,
                "fields": {
                    "name": "SQL Server", "image": "", "related": "24", "type": "0"
                }
            },
            {
                "model": model,
                "pk": 101,
                "fields": {
                    "name": "MariaDB", "image": "", "related": "24", "type": "0"
                }
            },
            {
                "model": model,
                "pk": 102,
                "fields": {
                    "name": "GoLand", "image": "", "related": "19", "type": "2"
                }
            },
            {
                "model": model,
                "pk": 103,
                "fields": {
                    "name": "IntelliJ", "image": "", "related": "1", "type": "2"
                }
            },
            {
                "model": model,
                "pk": 104,
                "fields": {
                    "name": "NumPy", "image": "", "related": "2", "type": "3"
                }
            },
            {
                "model": model,
                "pk": 105,
                "fields": {
                    "name": "Pandas", "image": "", "related": "2", "type": "3"
                }
            },
            {
                "model": model,
                "pk": 106,
                "fields": {
                    "name": "matplotlib", "image": "", "related": "2", "type": "3"
                }
            },
            {
                "model": model,
                "pk": 107,
                "fields": {
                    "name": "Anaconda", "image": "", "related": "2", "type": "3"
                }
            },
            {
                "model": model,
                "pk": 108,
                "fields": {
                    "name": "IPython Notebook", "image": "", "related": "2", "type": "3"
                }
            },
            {
                "model": model,
                "pk": 109,
                "fields": {
                    "name": "Kotlin", "image": "", "related": None, "type": "0"
                }
            },
            {
                "model": model,
                "pk": 110,
                "fields": {
                    "name": "J2EE", "image": "", "related": "1", "type": "3"
                }
            },
            {
                "model": model,
                "pk": 111,
                "fields": {
                    "name": "Jakarta EE", "image": "", "related": "1", "type": "3"
                }
            },
            {
                "model": model,
                "pk": 112,
                "fields": {
                    "name": "RubyMine", "image": "", "related": "12", "type": "2"
                }
            },
            {
                "model": model,
                "pk": 113,
                "fields": {
                    "name": "Selenium", "image": "", "related": "115", "type": "2"
                }
            },
            {
                "model": model,
                "pk": 114,
                "fields": {
                    "name": "Test Driven Development", "image": "", "related": "115", "type": "5"
                }
            },
            {
                "model": model,
                "pk": 115,
                "fields": {
                    "name": "Tests", "image": "", "related": None, "type": "5"
                }
            },
            {
                "model": model,
                "pk": 116,
                "fields": {
                    "name": "Android", "image": "", "related": None, "type": "4"
                }
            },
            {
                "model": model,
                "pk": 117,
                "fields": {
                    "name": "Git", "image": "", "related": None, "type": "5"
                }
            },
            {
                "model": model,
                "pk": 118,
                "fields": {
                    "name": "GitHub", "image": "", "related": None, "type": "5"
                }
            },
            {
                "model": model,
                "pk": 119,
                "fields": {
                    "name": "SVN", "image": "", "related": None, "type": "5"
                }
            },
            {
                "model": model,
                "pk": 120,
                "fields": {
                    "name": "Turtoise SVN", "image": "", "related": "119", "type": "5"
                }
            }
        ]

        path_file = os.path.join(
            os.path.dirname(
                os.path.dirname(
                    os.path.dirname(__file__)
                )
            ),
            'fixtures',
            'skills.json'
        )

        with open(path_file, 'w') as file_skills:
            file_skills.write(json.dumps(skills))
