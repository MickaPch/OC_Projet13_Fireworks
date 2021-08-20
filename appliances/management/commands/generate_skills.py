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
                    "name": "Java", "image": "skills/java.png", "related": None, "type": "0"
                }
            },
            {
                "model": model,
                "pk": 2,
                "fields": {
                    "name": "Python", "image": "skills/python.png", "related": None, "type": "0"
                }
            },
            {
                "model": model,
                "pk": 3,
                "fields": {
                    "name": "PHP", "image": "skills/php.png", "related": None, "type": "0"
                }
            },
            {
                "model": model,
                "pk": 4,
                "fields": {
                    "name": "C#", "image": "skills/c_cjMO89e.png", "related": None, "type": "0"
                }
            },
            {
                "model": model,
                "pk": 5,
                "fields": {
                    "name": "C", "image": "skills/c.png", "related": None, "type": "0"
                }
            },
            {
                "model": model,
                "pk": 6,
                "fields": {
                    "name": "C++", "image": "skills/c_IrEnLy6.png", "related": None, "type": "0"
                }
            },
            {
                "model": model,
                "pk": 7,
                "fields": {
                    "name": "JavaScript", "image": "skills/javascript.png", "related": None, "type": "0"
                }
            },
            {
                "model": model,
                "pk": 8,
                "fields": {
                    "name": "Objective-C", "image": "objective_c.png", "related": None, "type": "0"
                }
            },
            {
                "model": model,
                "pk": 9,
                "fields": {
                    "name": "R", "image": "skills/r.png", "related": None, "type": "0"
                }
            },
            {
                "model": model,
                "pk": 10,
                "fields": {
                    "name": "Swift", "image": "skills/swift.png", "related": None, "type": "0"
                }
            },
            {
                "model": model,
                "pk": 11,
                "fields": {
                    "name": "Matlab", "image": "skills/matlab.png", "related": None, "type": "0"
                }
            },
            {
                "model": model,
                "pk": 12,
                "fields": {
                    "name": "Ruby", "image": "skills/ruby.png", "related": None, "type": "0"
                }
            },
            {
                "model": model,
                "pk": 13,
                "fields": {
                    "name": "VBA", "image": "skills/vba.png", "related": None, "type": "0"
                }
            },
            {
                "model": model,
                "pk": 14,
                "fields": {
                    "name": "Visual Basic", "image": "skills/visual_basic.png", "related": None, "type": "0"
                }
            },
            {
                "model": model,
                "pk": 15,
                "fields": {
                    "name": "Scala", "image": "skills/scala.png", "related": None, "type": "0"
                }
            },
            {
                "model": model,
                "pk": 16,
                "fields": {
                    "name": "Perl", "image": "skills/perl.png", "related": None, "type": "0"
                }
            },
            {
                "model": model,
                "pk": 17,
                "fields": {
                    "name": "lua", "image": "skills/lua.png", "related": None, "type": "0"
                }
            },
            {
                "model": model,
                "pk": 18,
                "fields": {
                    "name": "Delphi", "image": "skills/delphi.png", "related": None, "type": "0"
                }
            },
            {
                "model": model,
                "pk": 19,
                "fields": {
                    "name": "Go", "image": "skills/go.png", "related": None, "type": "0"
                }
            },
            {
                "model": model,
                "pk": 20,
                "fields": {
                    "name": "Haskell", "image": "skills/haskell.png", "related": None, "type": "0"
                }
            },
            {
                "model": model,
                "pk": 21,
                "fields": {
                    "name": "Assembly", "image": "skills/assembly.png", "related": None, "type": "0"
                }
            },
            {
                "model": model,
                "pk": 22,
                "fields": {
                    "name": "VB.NET", "image": "skills/vb_net.png", "related": None, "type": "0"
                }
            },
            {
                "model": model,
                "pk": 23,
                "fields": {
                    "name": "Groovy", "image": "skills/groovy.png", "related": None, "type": "0"
                }
            },
            {
                "model": model,
                "pk": 24,
                "fields": {
                    "name": "SQL", "image": "skills/sql.png", "related": None, "type": "0"
                }
            },
            {
                "model": model,
                "pk": 25,
                "fields": {
                    "name": "iOS", "image": "skills/ios.png", "related": None, "type": "4"
                }
            },
            {
                "model": model,
                "pk": 26,
                "fields": {
                    "name": "HTML", "image": "skills/html.png", "related": None, "type": "0"
                }
            },
            {
                "model": model,
                "pk": 27,
                "fields": {
                    "name": "CSS", "image": "skills/css.png", "related": None, "type": "0"
                }
            },
            {
                "model": model,
                "pk": 28,
                "fields": {
                    "name": "Shell", "image": "skills/shell.png", "related": None, "type": "0"
                }
            },
            {
                "model": model,
                "pk": 29,
                "fields": {
                    "name": "Arduino", "image": "skills/arduino.png", "related": None, "type": "0"
                }
            },
            {
                "model": model,
                "pk": 30,
                "fields": {
                    "name": "Rust", "image": "skills/rust.png", "related": None, "type": "0"
                }
            },
            {
                "model": model,
                "pk": 31,
                "fields": {
                    "name": "Django", "image": "skills/django.png", "related": "2", "type": "1"
                }
            },
            {
                "model": model,
                "pk": 32,
                "fields": {
                    "name": "Bottle", "image": "skills/bottle.png", "related": "2", "type": "1"
                }
            },
            {
                "model": model,
                "pk": 33,
                "fields": {
                    "name": "CherryPy", "image": "skills/cherrypy.png", "related": "2", "type": "1"
                }
            },
            {
                "model": model,
                "pk": 34,
                "fields": {
                    "name": "Flask", "image": "skills/flask.png", "related": "2", "type": "1"
                }
            },
            {
                "model": model,
                "pk": 35,
                "fields": {
                    "name": "Pyramid", "image": "skills/pyramid.png", "related": "2", "type": "1"
                }
            },
            {
                "model": model,
                "pk": 36,
                "fields": {
                    "name": "TurboGears", "image": "skills/turbogears.png", "related": "2", "type": "1"
                }
            },
            {
                "model": model,
                "pk": 37,
                "fields": {
                    "name": "Twisted", "image": "skills/twisted.png", "related": "2", "type": "1"
                }
            },
            {
                "model": model,
                "pk": 38,
                "fields": {
                    "name": "Web2py", "image": "skills/web2py.png", "related": "2", "type": "1"
                }
            },
            {
                "model": model,
                "pk": 39,
                "fields": {
                    "name": "Zope", "image": "skills/zope.png", "related": "2", "type": "1"
                }
            },
            {
                "model": model,
                "pk": 40,
                "fields": {
                    "name": "Apache Lucene", "image": "skills/apache_lucene.png", "related": "1", "type": "1"
                }
            },
            {
                "model": model,
                "pk": 41,
                "fields": {
                    "name": "Apache Struts", "image": "skills/apache_struts.png", "related": "1", "type": "1"
                }
            },
            {
                "model": model,
                "pk": 42,
                "fields": {
                    "name": "Apache Tapestry", "image": "skills/apache_tapestry.png", "related": "1", "type": "1"
                }
            },
            {
                "model": model,
                "pk": 43,
                "fields": {
                    "name": "Google Guava", "image": "skills/guava.jpeg", "related": "1", "type": "1"
                }
            },
            {
                "model": model,
                "pk": 44,
                "fields": {
                    "name": "Hadoop", "image": "skills/hadoop.png", "related": "1", "type": "1"
                }
            },
            {
                "model": model,
                "pk": 45,
                "fields": {
                    "name": "Hibernate", "image": "skills/hibernate.png", "related": "1", "type": "1"
                }
            },
            {
                "model": model,
                "pk": 46,
                "fields": {
                    "name": "JavaFX", "image": "skills/javafx.png", "related": "1", "type": "1"
                }
            },
            {
                "model": model,
                "pk": 47,
                "fields": {
                    "name": "JavaServer Faces", "image": "skills/javaserver_faces.png", "related": "1", "type": "1"
                }
            },
            {
                "model": model,
                "pk": 48,
                "fields": {
                    "name": "JUnit", "image": "skills/junit.png", "related": "1", "type": "1"
                }
            },
            {
                "model": model,
                "pk": 49,
                "fields": {
                    "name": "Play Framework", "image": "skills/play_framework.png", "related": "1", "type": "1"
                }
            },
            {
                "model": model,
                "pk": 50,
                "fields": {
                    "name": "Qt Jambi", "image": "skills/qt_jambi.png", "related": "1", "type": "1"
                }
            },
            {
                "model": model,
                "pk": 51,
                "fields": {
                    "name": "Spring", "image": "skills/spring.png", "related": "1", "type": "1"
                }
            },
            {
                "model": model,
                "pk": 52,
                "fields": {
                    "name": "Zerocouplage", "image": "skills/zerocouplage.png", "related": "1", "type": "1"
                }
            },
            {
                "model": model,
                "pk": 53,
                "fields": {
                    "name": "Laravel", "image": "skills/laravel.png", "related": "3", "type": "1"
                }
            },
            {
                "model": model,
                "pk": 54,
                "fields": {
                    "name": "Symfony", "image": "skills/symfony.png", "related": "3", "type": "1"
                }
            },
            {
                "model": model,
                "pk": 55,
                "fields": {
                    "name": "CodeIgniter", "image": "skills/codeigniter.png", "related": "3", "type": "1"
                }
            },
            {
                "model": model,
                "pk": 56,
                "fields": {
                    "name": "Zend Framework", "image": "skills/zend.png", "related": "3", "type": "1"
                }
            },
            {
                "model": model,
                "pk": 57,
                "fields": {
                    "name": "Yii", "image": "skills/yii.png", "related": "3", "type": "1"
                }
            },
            {
                "model": model,
                "pk": 58,
                "fields": {
                    "name": "CakePHP", "image": "skills/cakephp.png", "related": "3", "type": "1"
                }
            },
            {
                "model": model,
                "pk": 59,
                "fields": {
                    "name": "Angular", "image": "skills/angular_KoBRI8k.png", "related": "7", "type": "1"
                }
            },
            {
                "model": model,
                "pk": 60,
                "fields": {
                    "name": "AngularJS", "image": "skills/angularjs.png", "related": "7", "type": "1"
                }
            },
            {
                "model": model,
                "pk": 61,
                "fields": {
                    "name": "Cappuccino", "image": "skills/cappuccino.png", "related": "7", "type": "1"
                }
            },
            {
                "model": model,
                "pk": 62,
                "fields": {
                    "name": "Ember.js", "image": "skills/emberjs.png", "related": "7", "type": "1"
                }
            },
            {
                "model": model,
                "pk": 63,
                "fields": {
                    "name": "Prototype", "image": "skills/prototype.png", "related": "7", "type": "1"
                }
            },
            {
                "model": model,
                "pk": 64,
                "fields": {
                    "name": "React.js", "image": "skills/react_js.png", "related": "7", "type": "1"
                }
            },
            {
                "model": model,
                "pk": 65,
                "fields": {
                    "name": "Vue.js", "image": "skills/vue_js.png", "related": "7", "type": "1"
                }
            },
            {
                "model": model,
                "pk": 66,
                "fields": {
                    "name": "Node.js", "image": "skills/nodejs.png", "related": "7", "type": "1"
                }
            },
            {
                "model": model,
                "pk": 67,
                "fields": {
                    "name": "jQuery", "image": "skills/jquery.png", "related": "7", "type": "1"
                }
            },
            {
                "model": model,
                "pk": 68,
                "fields": {
                    "name": "Bootstrap", "image": "skills/bootstrap.png", "related": "27", "type": "1"
                }
            },
            {
                "model": model,
                "pk": 69,
                "fields": {
                    "name": "Rails", "image": "skills/rails.png", "related": "12", "type": "1"
                }
            },
            {
                "model": model,
                "pk": 70,
                "fields": {
                    "name": "Drupal", "image": "skills/drupal.png", "related": "3", "type": "1"
                }
            },
            {
                "model": model,
                "pk": 71,
                "fields": {
                    "name": "BlueJ", "image": "skills/bluej.png", "related": "1", "type": "2"
                }
            },
            {
                "model": model,
                "pk": 72,
                "fields": {
                    "name": "Eclipse", "image": "skills/eclipse.png", "related": "1", "type": "2"
                }
            },
            {
                "model": model,
                "pk": 73,
                "fields": {
                    "name": "AWS Cloud", "image": "skills/aws_cloud.png", "related": None, "type": "2"
                }
            },
            {
                "model": model,
                "pk": 74,
                "fields": {
                    "name": "Windows", "image": "skills/windows.png", "related": None, "type": "4"
                }
            },
            {
                "model": model,
                "pk": 75,
                "fields": {
                    "name": "MacOS", "image": "skills/macos_7qpzWH9.png", "related": None, "type": "4"
                }
            },
            {
                "model": model,
                "pk": 76,
                "fields": {
                    "name": "Linux", "image": "skills/linux.png", "related": None, "type": "4"
                }
            },
            {
                "model": model,
                "pk": 77,
                "fields": {
                    "name": "Ubuntu", "image": "skills/ubuntu.png", "related": "76", "type": "4"
                }
            },
            {
                "model": model,
                "pk": 78,
                "fields": {
                    "name": "Debian", "image": "skills/debian.png", "related": "76", "type": "4"
                }
            },
            {
                "model": model,
                "pk": 79,
                "fields": {
                    "name": "Fedora", "image": "skills/fedora.png", "related": "76", "type": "4"
                }
            },
            {
                "model": model,
                "pk": 80,
                "fields": {
                    "name": "CodeLite", "image": "skills/codelite.png", "related": None, "type": "2"
                }
            },
            {
                "model": model,
                "pk": 81,
                "fields": {
                    "name": "UML", "image": "skills/uml.png", "related": None, "type": "5"
                }
            },
            {
                "model": model,
                "pk": 82,
                "fields": {
                    "name": "Agile", "image": "skills/agile.png", "related": None, "type": "5"
                }
            },
            {
                "model": model,
                "pk": 83,
                "fields": {
                    "name": "SCRUM", "image": "skills/scrum.png", "related": "82", "type": "5"
                }
            },
            {
                "model": model,
                "pk": 84,
                "fields": {
                    "name": "Kanban", "image": "skills/kanban.png", "related": "82", "type": "5"
                }
            },
            {
                "model": model,
                "pk": 85,
                "fields": {
                    "name": "NetBeans", "image": "skills/netbeans.png", "related": None, "type": "2"
                }
            },
            {
                "model": model,
                "pk": 87,
                "fields": {
                    "name": "PhpStorm", "image": "skills/phpstorm.png", "related": "3", "type": "2"
                }
            },
            {
                "model": model,
                "pk": 92,
                "fields": {
                    "name": "PyCharm", "image": "skills/pycharm.png", "related": "2", "type": "2"
                }
            },
            {
                "model": model,
                "pk": 93,
                "fields": {
                    "name": "AppCode", "image": "skills/appcode.png", "related": "25", "type": "2"
                }
            },
            {
                "model": model,
                "pk": 94,
                "fields": {
                    "name": "CLion", "image": "skills/clion.png", "related": "5", "type": "2"
                }
            },
            {
                "model": model,
                "pk": 95,
                "fields": {
                    "name": "DataGrip", "image": "skills/datagrip.png", "related": "24", "type": "2"
                }
            },
            {
                "model": model,
                "pk": 96,
                "fields": {
                    "name": "PostgreSQL", "image": "skills/postgresql.png", "related": "24", "type": "0"
                }
            },
            {
                "model": model,
                "pk": 97,
                "fields": {
                    "name": "MySQL", "image": "skills/musql.png", "related": "24", "type": "0"
                }
            },
            {
                "model": model,
                "pk": 98,
                "fields": {
                    "name": "MongoDB", "image": "skills/mongodb.png", "related": "24", "type": "0"
                }
            },
            {
                "model": model,
                "pk": 99,
                "fields": {
                    "name": "Oracle", "image": "skills/oracle.png", "related": "24", "type": "0"
                }
            },
            {
                "model": model,
                "pk": 100,
                "fields": {
                    "name": "SQL Server", "image": "skills/sql_server.png", "related": "24", "type": "0"
                }
            },
            {
                "model": model,
                "pk": 101,
                "fields": {
                    "name": "MariaDB", "image": "skills/mariadb.png", "related": "24", "type": "0"
                }
            },
            {
                "model": model,
                "pk": 102,
                "fields": {
                    "name": "GoLand", "image": "skills/goland.png", "related": "19", "type": "2"
                }
            },
            {
                "model": model,
                "pk": 103,
                "fields": {
                    "name": "IntelliJ", "image": "skills/intellij.png", "related": "1", "type": "2"
                }
            },
            {
                "model": model,
                "pk": 104,
                "fields": {
                    "name": "NumPy", "image": "skills/numpy.png", "related": "2", "type": "3"
                }
            },
            {
                "model": model,
                "pk": 105,
                "fields": {
                    "name": "Pandas", "image": "skills/pandas.png", "related": "2", "type": "3"
                }
            },
            {
                "model": model,
                "pk": 106,
                "fields": {
                    "name": "matplotlib", "image": "skills/matplotlib.png", "related": "2", "type": "3"
                }
            },
            {
                "model": model,
                "pk": 107,
                "fields": {
                    "name": "Anaconda", "image": "skills/anaconda.png", "related": "2", "type": "3"
                }
            },
            {
                "model": model,
                "pk": 108,
                "fields": {
                    "name": "Jupyter Notebook", "image": "skills/jupyter.png", "related": "2", "type": "3"
                }
            },
            {
                "model": model,
                "pk": 109,
                "fields": {
                    "name": "Kotlin", "image": "skills/kotlin.png", "related": None, "type": "0"
                }
            },
            {
                "model": model,
                "pk": 110,
                "fields": {
                    "name": "J2EE", "image": "skills/j2ee.png", "related": "1", "type": "3"
                }
            },
            {
                "model": model,
                "pk": 111,
                "fields": {
                    "name": "Jakarta EE", "image": "skills/jakarta_ee.png", "related": "1", "type": "3"
                }
            },
            {
                "model": model,
                "pk": 112,
                "fields": {
                    "name": "RubyMine", "image": "skills/rubymine.png", "related": "12", "type": "2"
                }
            },
            {
                "model": model,
                "pk": 113,
                "fields": {
                    "name": "Selenium", "image": "skills/selenium.png", "related": "115", "type": "2"
                }
            },
            {
                "model": model,
                "pk": 114,
                "fields": {
                    "name": "Test Driven Development", "image": "skills/tdd.png", "related": "115", "type": "5"
                }
            },
            {
                "model": model,
                "pk": 115,
                "fields": {
                    "name": "Tests", "image": "skills/tests.png", "related": None, "type": "5"
                }
            },
            {
                "model": model,
                "pk": 116,
                "fields": {
                    "name": "Android", "image": "skills/android.png", "related": None, "type": "4"
                }
            },
            {
                "model": model,
                "pk": 117,
                "fields": {
                    "name": "Git", "image": "skills/git.png", "related": None, "type": "5"
                }
            },
            {
                "model": model,
                "pk": 118,
                "fields": {
                    "name": "GitHub", "image": "skills/github.png", "related": None, "type": "5"
                }
            },
            {
                "model": model,
                "pk": 119,
                "fields": {
                    "name": "SVN", "image": "skills/svn.png", "related": None, "type": "5"
                }
            },
            {
                "model": model,
                "pk": 120,
                "fields": {
                    "name": "Turtoise SVN", "image": "skills/turtoise_svn.png", "related": "119", "type": "5"
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
