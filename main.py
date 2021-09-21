# How to open read and write files in python

data = [{'name': 'Carlos', 'company': 'Google', 'role': 'Front End'}, {'name': 'Jhon', 'company': 'Microsoft', 'role': 'Full-Stack'}, {'name': 'Doe', 'company': 'Amazon', 'role': 'Backend'}]

with open('coverletter.txt') as letter:
    letter_content = letter.read()
    for name in data:
        new_letter = letter_content.replace('[name]', name['name'])
        new_letter = new_letter.replace('[company]', name['company'])
        new_letter = new_letter.replace('[role]', name['role'])
        with open(f'{name}_letter.text', 'w+') as new:
            new.write(new_letter)
