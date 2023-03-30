from jinja2 import Template

PATH = './Output/'

class Outputter:
    def __init__(self, system) -> None:
        self.system = system
    
    def getLog(self):
        with open("./kinepolis/template.html", "r") as template_file:
            template = Template(template_file.read())
        
        temp = []
        self.system.getScreeningSystem().traverse(temp.append)
        screenings = []
        for screening in temp:
            screenings.append((screening, self.system.getMovieSystem().retrieve(screening.filmid)[0].title))
        events = self.system.getEventSystem().getEventList()
        time = self.system.clock
        return template.render(screenings=screenings, events=events, time=time)

    def generate(self, filename):
        f = open(PATH+filename, 'w')     

        html = f"""<!DOCTYPE html>
                    <html>
                        {self.getLog()}
                    </html>
                """
        f.write(html)
        f.close()
