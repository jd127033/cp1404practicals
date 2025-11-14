"""Project Management System

Estimated time: 120 minutes
Actual time: 180 min
"""

import datetime
from project import Project

MENU = """
- (L)oad projects  
- (S)ave projects  
- (D)isplay projects  
- (F)ilter projects by date
- (A)dd new project  
- (U)pdate project
- (Q)uit"""

PROJECT_FILENAME = "projects.txt"


def main():
    """Main program for project management."""
    print("Welcome to Pythonic Project Management")
    projects = load_projects(PROJECT_FILENAME)
    print(f"Loaded {len(projects)} projects from {PROJECT_FILENAME}")
    choice = ""
    while choice != "Q":
        print(MENU)
        choice = input(">>> ").upper()

        if choice == "L":
            filename = input("Filename to load: ")
            projects = load_projects(filename)
            print(f"Loaded {len(projects)} projects from {filename}")
        elif choice == "S":
            filename = input("Filename to save: ")
            try:
                save_projects(filename, projects)
                print(f"Projects saved to {filename}")
            except FileNotFoundError:
                print("File not found. Please try again.")
        elif choice == "D":
            display_projects(projects)
        elif choice == "F":
            filter_projects_by_date(projects)
        elif choice == "A":
            add_new_project(projects)
        elif choice == "U":
            update_project(projects)
        elif choice == "Q":
            save_choice = input(f"Would you like to save to {PROJECT_FILENAME}? (Y/N)? ").upper()
            if save_choice == "Y":
                save_projects(PROJECT_FILENAME, projects)
                print(f"Projects saved to {PROJECT_FILENAME}")
            elif save_choice == "N":
                print("Projects were not saved.")
        else:
            print("Invalid choice")

    print("Thank you for using custom-built project management software.")


def load_projects(filename):
    """Load projects from a project data file."""
    projects = []
    with open(filename, 'r') as file:
        file.readline()  # Skip the header line
        for line in file:
            parts = line.strip().split('\t') # Splits items separated by tab into list.
            name = parts[0]
            start_date = datetime.datetime.strptime(parts[1], "%d/%m/%Y").date()
            priority = int(parts[2])
            cost_estimate = float(parts[3])
            completion_percentage = int(parts[4])
            projects.append(Project(name, start_date, priority, cost_estimate, completion_percentage)) # Add project to list
    return projects

def add_new_project(projects):
    """Adds new project to list."""
    print("Let's add a new project")
    name = input("Name: ")
    date_string = input("Start date (dd/mm/yy): ")
    start_date = datetime.datetime.strptime(date_string, "%d/%m/%Y").date()
    priority = int(input("Priority: "))
    cost_string = input("Cost estimate: $")
    cost_estimate = float(cost_string)
    completion_percentage = int(input("Percent complete: "))

    new_project = Project(name, start_date, priority, cost_estimate, completion_percentage)
    projects.append(new_project)

def save_projects(filename, projects):
    """ Save projects to data file. """
    with open(filename, 'w') as file:
        file.write("Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage\n") # Write header to file
        for i, project in enumerate(projects):
            file.write(f"{project.convert_file_format()}") # Write each project to the file in the correct file format
            if i < len(projects) -1:    # Trim the final empty line to prevent issues reloading program
                file.write("\n")


def display_projects(projects):
    """Display projects grouped by completion status, sorted by priority."""
    incomplete = [project for project in projects if not project.is_complete()] # produce unsorted list of incomplete projects
    complete = [project for project in projects if project.is_complete()] # produce unsorted list of complete projects
    # Sort lists of projects by priority
    incomplete.sort()
    complete.sort()

    print("Incomplete projects: ")
    for project in incomplete:
        print(f"  {project}")

    print("Completed projects: ")
    for project in complete:
        print(f"  {project}")

def get_start_date(project):
    """Return start date of a project for sorting."""
    return project.start_date

def filter_projects_by_date(projects):
    """Display projects starting after a specified inputted date. Then sorted by date."""
    date_string = input("Show projects that start after date (dd/mm/yy): ")
    filter_date = datetime.datetime.strptime(date_string, "%d/%m/%Y").date()
    # create filtered list of projects that occur after inputted start date
    filtered_projects = [project for project in projects if project.start_date >= filter_date]
    filtered_projects.sort(key=get_start_date) # sort projects by date (oldest to newest)

    for project in filtered_projects:
        print(project)

def update_project(projects):
    """Update a project's completion priority and/or percentage."""
    for i, project in enumerate(projects):
        print(f"{i} {project}")

    try:
        # Select a project from the list of projects
        project_choice = int(input("Project choice: "))
        project = projects[project_choice]
        print(project)
        # Ask for new completion percentage value
        new_percentage = input("New Percentage: ")
        if new_percentage:
            project.update_completion(int(new_percentage))
        # Ask for new project priority value
        new_priority = input("New Priority: ")
        if new_priority:
            project.update_priority(int(new_priority))
    except (ValueError, IndexError): # Error handling for cases where invalid list index or value is entered.
        print("Invalid input")


if __name__ == "__main__":
    main()