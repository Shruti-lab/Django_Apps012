def chapter_body(name):
    with open(name, 'rb') as fh:
        print(fh.read())

# Read the contents of the file `chapter1.txt`
chapter_body('./chap.txt')