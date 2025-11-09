"""Project Management System

Estimated time: 120 minutes
Actual time:
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
            save_projects(filename, projects)
            print(f"Projects saved to {filename}")
        elif choice == "D":
            display_projects(projects)
        elif choice == "F":
            filter_projects_by_date(projects)
        elif choice == "A":
            add_new_project(projects)
        elif choice == "U":
            update_project(projects)
        elif choice == "Q":
            save_choice = input(f"Would you like to save to {PROJECT_FILENAME}? (Y/N)?").upper()
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

