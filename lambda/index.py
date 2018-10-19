from main import execute


def handler(event, context):
    name = 'lambda'
    execute(name)
    
    return "success!"
