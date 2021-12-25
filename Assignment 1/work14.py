#Write a Python script to check if a given key already exists in a dictionary.

shrijan={1:4,2:7,44:34}
def keypresent():
    if 1 in shrijan:
        print("key exists")
    if 2 in shrijan:
        print("key exists")
    if 44 in shrijan:
        print("key exists")

    else:
        print("key absent")
keypresent()
