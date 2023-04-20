from jinja2 import Template

PATH = "./Output/"


class Outputter:
    def __init__(self, system) -> None:
        """
        Initializes an outputter

        :param system: Kinepolis object
        Pre-condition: /
        Post-condition: Creates an ouputter system
        """
        self.system = system

    def getLog(self):
        """
        Returns the log

        Pre-condition : Outputter is initialized
        Post-condition : Returns the log of the system
        """
        with open("./kinepolis/template.html", "r") as template_file:
            template = Template(template_file.read())

        temp = []
        self.system.getScreeningSystem().traverse(temp.append)
        screenings = []
        for screening in temp:
            if screening is not None:
                screenings.append(
                    (
                        screening,
                        self.system.getMovieSystem()
                        .retrieve(screening.filmsearchkey)[0]
                        .title,
                    )
                )
        events = self.system.getEventSystem().getEventList()
        time = self.system.clock
        return template.render(screenings=screenings, events=events, time=time)

    def generate(self, filename):
        """
        Generates the log into a html file

        :param filename: Name of the file
        Pre-condition : Outputter is initialized
        Post-condition : Output file is generated
        """
        f = open(PATH + filename, "w")

        html = f"""<!DOCTYPE html>
                    <html>
                        {self.getLog()}
                    </html>
                """
        f.write(html)
        f.close()
