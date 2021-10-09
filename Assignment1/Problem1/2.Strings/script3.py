# Mutations

def mutate_string(string, position, character):
    a = list(string)
    a[position] = character
    string = ''.join(a)

    return string
