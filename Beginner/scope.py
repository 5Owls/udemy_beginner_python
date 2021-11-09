''' Understanding scope: '''

enemies = 1

def increase_enemies():
    print(f"enemies inside function: {enemies}")
    return enemies + 1

enemies = increase_enemies()

print(f"enemies outside function: {enemies}")
#output:
# enemies inside function: 1
# enemies outside function: 2