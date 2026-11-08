import re

class Project:
    def __init__(self, name, description, license, authors, python, dependencies, dev_dependencies):
        self.name = name
        self.description = description
        self.license = license
        self.authors = authors
        self.python = python
        self.dependencies = dependencies
        self.dev_dependencies = dev_dependencies

    def _stringify_dependencies(self, dependencies):
        newlist = []
        if len(self.python) > 0:
            newlist.append("python");
        for item in dependencies:
            newlist.append(re.split(r'[>=]+', item)[0])
        
        return "\n- ".join(newlist) if len(newlist) > 0 else "-"

    def _stringify_authors(self, authors):
        newList = []
        for author in authors:
            newList.append(author["name"])
        return "\n- ".join(newList) if len(newList) > 0 else "-"

    def __str__(self):
        return (
            f"Name: {self.name}"
            f"\nDescription: {self.description or '-'}"
            f"\nLicense: {self.license or '-'}"
            "\n"
            f"\nAuthors: \n- {self._stringify_authors(self.authors)}\n"
            f"\nDependencies: \n- {self._stringify_dependencies(self.dependencies)}\n"
            f"\nDevelopment dependencies: {self._stringify_dependencies(self.dev_dependencies)}"
        )
