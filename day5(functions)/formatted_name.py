def get_formatted_name(first_name,last_name):
    """Return a fullname,neatly formatted."""
    full_name=f"{first_name} {last_name}"
    return full_name.title()

musician=get_formatted_name("damini","ogbolu")
print(musician)

def get_formatted_name_with_middlename(first_name,middle_name,last_name):
    """Return a full name,with middle nameneatly formatted"""
    full_name=f"{first_name} {middle_name} {last_name}"
    return full_name.title()

musician=get_formatted_name_with_middlename("bruce","lee","hooker")
print(musician)

def get_formatted_name_withandwithout_middlename(first_name,last_name,middle_name=""):
    """Return fullname with middle name set as string ,neatly formatted"""
    if middle_name:
        fullname=f"{first_name} {middle_name} {last_name}"
    else:
        fullname=f"{first_name} {last_name}"
    return fullname

musician=get_formatted_name_withandwithout_middlename("bashir","aremu")
print(musician)
musician=get_formatted_name_withandwithout_middlename("bashir","aremu","toyin")
print(musician)