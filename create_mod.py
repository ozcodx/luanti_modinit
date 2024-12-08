import os
from datetime import datetime

def get_mod_data():
    """Collects necessary data for the mod creation."""
    name = input("Mod name (my_mod): ").strip()
    while not name:
        print("The name cannot be empty.")
        name = input("Mod name (my_mod): ").strip()

    default_title = name.replace("_", " ").title()
    title = input(f"Title [{default_title}]: ").strip() or default_title

    description = input("Description: ").strip()

    default_author = "ozcodx"
    author = input(f"Author [{default_author}]: ").strip() or default_author

    deps = input("Dependencies: ").strip()

    return {
        "name": name,
        "title": title,
        "description": description,
        "author": author,
        "deps": deps,
    }

def create_folder(name):
    """Creates a folder for the mod if it does not already exist."""
    if not os.path.exists(name):
        os.makedirs(name)
        print(f"Folder '{name}' created.")
    else:
        print(f"The folder '{name}' already exists.")

def create_mod_conf(mod_data):
    """Generates the mod.conf file with the provided data."""
    mod_conf_path = os.path.join(mod_data["name"], "mod.conf")
    with open(mod_conf_path, "w", encoding="utf-8") as conf_file:
        conf_file.write(f"name = {mod_data['name']}\n")
        conf_file.write(f"title = {mod_data['title']}\n")
        conf_file.write(f"description = {mod_data['description']}\n")
        conf_file.write(f"author = {mod_data['author']}\n")
        conf_file.write(f"depends = {mod_data['deps']}\n")
    print(f"'mod.conf' file created at '{mod_conf_path}'.")

def create_init_lua(name):
    """Generates the init.lua file with references to other Lua files."""
    init_lua_path = os.path.join(name, "init.lua")
    with open(init_lua_path, "w", encoding="utf-8") as lua_file:
        lua_file.write(f"""local modpath = minetest.get_modpath("{name}")
dofile(modpath .. "/crafts.lua")
dofile(modpath .. "/nodes.lua")
dofile(modpath .. "/items.lua")
dofile(modpath .. "/utils.lua")""")
    print(f"'init.lua' file created at '{init_lua_path}'.")

def create_empty_lua_files(name):
    """Creates empty Lua files: crafts.lua, nodes.lua, items.lua, and utils.lua."""
    lua_files = ["crafts.lua", "nodes.lua", "items.lua", "utils.lua"]
    for file in lua_files:
        file_path = os.path.join(name, file)
        with open(file_path, "w", encoding="utf-8") as lua_file:
            lua_file.write("")  # Empty file
        print(f"'{file}' file created at '{file_path}'.")

def create_readme_and_license(mod_data):
    """Generates README.md and LICENSE files with structured content."""
    year = datetime.now().year
    readme_path = os.path.join(mod_data["name"], "README.md")
    license_path = os.path.join(mod_data["name"], "LICENSE")
    
    # Generate README.md
    with open(readme_path, "w", encoding="utf-8") as readme_file:
        readme_file.write(f"# {mod_data['title']}\n")
        readme_file.write(f"{mod_data['description']}\n\n")
        readme_file.write("## Features\n")
        readme_file.write("- Adds a special block that do something.\n")
        readme_file.write("- Custom behaviors for nodes and items.\n\n")
        readme_file.write("## Ideas for Future Work\n")
        readme_file.write("- Add more block variations with unique mechanics.\n")
        readme_file.write("- Improve textures and animations.\n\n")
        readme_file.write("## License\n")
        readme_file.write("This mod is licensed under **MIT**. See the [LICENSE](LICENSE) file for more details.\n\n")
        readme_file.write(f"## Author\n**{mod_data['author']}**  \n")
        readme_file.write("Inspired by the creativity of the Luanti community.\n")
    print(f"'README.md' file created at '{readme_path}'.")

    # Generate LICENSE
    with open(license_path, "w", encoding="utf-8") as license_file:
        license_file.write("MIT License\n\n")
        license_file.write(f"Copyright (c) {year} {mod_data['author']}\n\n")
        license_file.write("Permission is hereby granted, free of charge, to any person obtaining a copy\n")
        license_file.write("of this software and associated documentation files (the \"Software\"), to deal\n")
        license_file.write("in the Software without restriction, including without limitation the rights\n")
        license_file.write("to use, copy, modify, merge, publish, distribute, sublicense, and/or sell\n")
        license_file.write("copies of the Software, and to permit persons to whom the Software is\n")
        license_file.write("furnished to do so, subject to the following conditions:\n\n")
        license_file.write("The above copyright notice and this permission notice shall be included in all\n")
        license_file.write("copies or substantial portions of the Software.\n\n")
        license_file.write("THE SOFTWARE IS PROVIDED \"AS IS\", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR\n")
        license_file.write("IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,\n")
        license_file.write("FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE\n")
        license_file.write("AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER\n")
        license_file.write("LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,\n")
        license_file.write("OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE\n")
        license_file.write("SOFTWARE.\n")
    print(f"'LICENSE' file created at '{license_path}'.")

def create_mod():
    """Main function that orchestrates mod creation."""
    mod_data = get_mod_data()  # Collect user inputs
    create_folder(mod_data["name"])  # Create mod folder
    create_mod_conf(mod_data)  # Generate mod.conf
    create_init_lua(mod_data["name"])  # Generate init.lua
    create_empty_lua_files(mod_data["name"])  # Create empty Lua files
    create_readme_and_license(mod_data)  # Generate README.md and LICENSE

if __name__ == "__main__":
    create_mod()
