# Capitalize!


# Complete the solve function below.
def solve(s):
    result = []
    name = re.split(r'(\s+)', s)

    for i in range(len(name)):
        result.append(str(name[i]).capitalize())

    return ''.join(str(ele) for ele in result)
