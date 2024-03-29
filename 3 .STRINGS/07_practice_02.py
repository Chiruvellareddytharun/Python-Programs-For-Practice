Name = input("enter the name: ")
date = input("enter the date: ")

template = '''
dear <|name|>
you are selected
<|date|>
'''
print(template.replace('<|name|>',Name).replace('<|date|>',date))