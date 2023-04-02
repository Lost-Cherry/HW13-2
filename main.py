"""
Create file with some content. As example you can take this one
    Тому що ніколи тебе не вирвеш,
    ніколи не забереш,
    тому що вся твоя свобода
    складається з меж,
    тому що в тебе немає
    жодного вантажу,
    тому що ти ніколи не слухаєш,
    оскільки знаєш і так,
    що я скажу,
Create second file and copy content of the first file to the second file in upper case.

"""


f = open("demofile2.txt", "w")
f.write("Now the file has more content!")
f.close()

with open('demofile2.txt', 'r') as f1:
    # Read the content of the first file
    content = f1.read()


# Open the second file for writing
with open('file2.txt', 'w') as f2:
    # Write the content of the first file in upper case to the second file
    f2.write(content.upper())

