# Validating Email Addresses With a Filter

def fun(email):
    # return True if s is a valid email, else return False
    try:
        username, url = email.split('@')
        website, extension = url.split('.')
    except ValueError:
        return False

    if username.replace('-', '').replace('_', '').isalnum() is False:
        return False
    elif website.isalnum() is False:
        return False
    elif len(extension) > 3:
        return False
    else:
        return True
