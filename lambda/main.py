from time import sleep


def execute(name=None):
    print(f"Waiting 60s. '{name}' running!")
    sleep(60)
    print(f"'{name}': finished!")