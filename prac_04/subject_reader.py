"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    """Program to load and display subject data from file."""
    subjects = load_subjects(FILENAME)
    display_subjects(subjects)


def load_subjects(filename=FILENAME):
    """Read data from file formatted like: subject,lecturer,number of students."""
    input_file = open(filename)
    all_subjects = []
    for line in input_file:
        line = line.strip()
        parts = line.split(',')
        subject_details = [parts[0], parts[1], int(parts[2])]
        all_subjects.append(subject_details)
    input_file.close()
    return all_subjects

def display_subjects(subject_list):
    """Display subject data from list."""
    for subject in subject_list:
        print(f"{subject[0]} is taught by {subject[1]} and has {subject[2]} students.")


main()