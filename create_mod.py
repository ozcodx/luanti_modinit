import os

def create_mod():
    name = input("Mod name (my_mod): ").strip()
    while not name:
        print("The name cannot be empty.")
        name = input("Mod name (my_mod): ").strip()

    default_title = name.replace("_", " ").title()
    title = input(f"Title [{default_title}]: ").strip()
    if not title:
        title = default_title

    description = input("Description: ").strip()

    default_author = "ozcodx"
    author = input(f"Author[{default_author}]: ").strip()
    if not author:
        author = default_author

    deps = input("Dependencies: ").strip()

    if not os.path.exists(name):
        os.makedirs(name)
        print(f"Folder '{name}' created.")
    else:
        print(f"The folder '{name}' already exists.")

    mod_conf_path = os.path.join(name, "mod.conf")
    with open(mod_conf_path, "w", encoding="utf-8") as conf_file:
        conf_file.write(f"name = {name}\n")
        conf_file.write(f"title = {title}\n")
        conf_file.write(f"description = {description}\n")
        conf_file.write(f"author = {author}\n")
        conf_file.write(f"depends = {deps}\n")
    print(f"'mod.conf' file created at '{mod_conf_path}'.")

    init_lua_path = os.path.join(name, "init.lua")
    with open(init_lua_path, "w", encoding="utf-8") as lua_file:
        lua_file.write("")
    print(f"'init.lua' file created at '{init_lua_path}'.")

if __name__ == "__main__":
    create_mod()