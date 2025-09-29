
class BaseCodeBuilder:
    def __init__(self):
        self.sections = []

    def add_section(self, section_text):
        self.sections.append(section_text)

    def build(self):
        return "\n".join(self.sections)
