"""
FILENAME = "projects.txt"
Menu = "- (L)oad projects\n- (S)ave projects\n- (D)isplay projects\n"
        "- (F)ilter projects by date\n- (A)dd new project\n- (U)pdate project\n- (Q)uit"
function main()
    display "Welcome to Pythonic Project Management"
    projects = load_projects(FILENAME)
    display length of projects, FILENAME
    display Menu
    get choice
    while choice not equal to "q"
        if choice = 'l'
            get filename
            load_projects(filename)
        else if choice = 's'
            get filename
            save_projects(filename, projects)
        else if choice = 'd'
            display_projects(projects)
        else if choice = 'f'
            filter_projects_by_date(projects)
        else if choice = 'a'
            add_project(projects)
        else if choice = 'u'
            update_project(projects)
        display "Welcome to Pythonic Project Management"
        projects = load_projects(FILENAME)
        display length of projects, FILENAME
        display Menu
        get choice
    get save
    if save
        save_projects(FILENAME, projects)
        display "Thank you for using custom-built project management software."



function load_projects(filename)
    projects is an empty list
    with open filename and read as file
        lines = read each lines in file from 2 to end
        repeat line in lines
            output parts
            if length of parts = 5
                append Project(*parts) in projects
    return projects


function save_projects(filename, projects)
    with open filename and write as file
         write ("Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage\n") in file
        repeat  project in projects
            write (project.to_tab_delimited() + "\n") in file


function display_projects(projects)
    incomplete = sorted([project for project in projects if not project.is_complete()])
    complete = sorted([project for project in projects if project.is_complete()])
    display "Incomplete projects:"
    repeat  project in incomplete
        display project
    display "Completed projects:"
    repeat project in complete
        display project


function filter_projects_by_date(projects)
    get date_string
    filter_date = datetime.strptime(date_string, "%d/%m/%Y").date()
    filtered = sorted([project for project in projects if project.start_date >= filter_date], key=lambda project: project.start_date)
    repeat project in filtered
        display project


function add_project(projects)
    display "Let's add a new project"
    get name
    get start_date
    get priority
    get estimate
    get completion
    append Project(name, start_date, priority, estimate, completion) in projects


function update_project(projects)
    for project in projects and index i = 1
        display project, i
    get choice
    project =  the choice element in projects
    display project
    display new_completion
    display new_priority
    if new_completion
        project.completion = integer(new_completion)
    if new_priority
        project.priority = integer(new_priority)


main()

"""
from project import Project
from datetime import datetime

FILENAME = "projects.txt"
Menu = ("- (L)oad projects\n- (S)ave projects\n- (D)isplay projects\n"
        "- (F)ilter projects by date\n- (A)dd new project\n- (U)pdate project\n- (Q)uit")


def main():
    """Main function to run the project management menu."""
    print("Welcome to Pythonic Project Management")
    projects = load_projects(FILENAME)
    print(f"Loaded {len(projects)} projects from {FILENAME}")
    print(Menu)
    choice = input(">>> ").lower()
    while choice != "q":
        if choice == 'l':
            filename = input("Filename: ")
            load_projects(filename)
        elif choice == 's':
            filename = input("Filename: ")
            save_projects(filename, projects)
        elif choice == 'd':
            display_projects(projects)
        elif choice == 'f':
            filter_projects_by_date(projects)
        elif choice == 'a':
            add_project(projects)
        elif choice == 'u':
            update_project(projects)
        print("Welcome to Pythonic Project Management")
        projects = load_projects(FILENAME)
        print(f"Loaded {len(projects)} projects from {FILENAME}")
        print(Menu)
        choice = input(">>> ").lower()
    save = input(f"Would you like to save to {FILENAME}? ").lower()
    if save:
        save_projects(FILENAME, projects)
        print("Thank you for using custom-built project management software.")





def load_projects(filename):
    """Load projects from a file."""
    projects = []
    with open(filename, "r") as file:
        lines = file.readlines()[1:]
        for line in lines:
            parts = line.strip().split("\t")
            if len(parts) == 5:
                projects.append(Project(*parts))
    return projects


def save_projects(filename, projects):
    """Save the list of projects to a file in tab-delimited format."""
    with open(filename, "w") as file:
        file.write("Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage\n")
        for project in projects:
            file.write(project.to_tab_delimited() + "\n")


def display_projects(projects):
    """Display all projects, separated into incomplete and complete projects."""
    incomplete = sorted([project for project in projects if not project.is_complete()])
    complete = sorted([project for project in projects if project.is_complete()])
    print("Incomplete projects:")
    for project in incomplete:
        print(f"  {project}")
    print("Completed projects:")
    for project in complete:
        print(f"  {project}")


def filter_projects_by_date(projects):
    """Filter and display projects that start after a given date."""
    date_string = input("Show projects that start after date (dd/mm/yyyy): ")
    filter_date = datetime.strptime(date_string, "%d/%m/%Y").date()
    filtered = sorted([project for project in projects if project.start_date >= filter_date], key=lambda project: project.start_date)
    for project in filtered:
        print(project)


def add_project(projects):
    """Prompt user to add a new project and append it to the projects list."""
    print("Let's add a new project")
    name = input("Name: ")
    start_date = input("Start date (dd/mm/yyyy): ")
    priority = int(input("Priority: "))
    estimate = float(input("Cost estimate: $"))
    completion = int(input("Percent complete: "))
    projects.append(Project(name, start_date, priority, estimate, completion))


def update_project(projects):
    """Allow user to select a project and update its completion percentage and/or priority."""
    for i, project in enumerate(projects):
        print(f"{i} {project}")
    choice = int(input("Project choice: "))
    project = projects[choice]
    print(project)
    new_completion = input("New Percentage: ")
    new_priority = input("New Priority: ")
    if new_completion:
        project.completion = int(new_completion)
    if new_priority:
        project.priority = int(new_priority)


main()
