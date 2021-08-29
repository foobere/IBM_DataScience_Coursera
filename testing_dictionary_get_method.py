# using the get method of dictionaries; using get method default value

name_for_user_id = { 
    382: "Alice",
    590: "Bob",
    951:"Dilbert",
}

def greeting(userid):
    """ takes in the key and returns a string that includes the value for the key"""
    return "Hi {}!".format(name_for_user_id.get(userid,"Felix")) # Felix is the default value if key is not present



print(greeting(590))










