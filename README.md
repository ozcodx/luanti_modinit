# Luanti Mod Initializer

**luanti_modinit** is a Python-based tool designed to help you quickly initialize mods for the **Luanti game engine**. The tool creates the necessary folder structure and configuration files for your mod with default values and simple prompts. It generates the following files:

- `mod.conf`: Contains configuration details like the mod's name, title, description, author, and dependencies.
- `init.lua`: A blank Lua file ready for your mod's initialization code.

## Features

- Prompts you for basic information like mod name, title, description, author, and dependencies.
- Automatically generates a folder with the mod's name.
- Creates the `mod.conf` file with the provided details.
- Creates an empty `init.lua` file to get you started with your mod.

## Installation

1. Clone this repository or download the `create_mod.py` script.

2. Ensure you have Python 3.x installed on your system.

3. Run the script from the command line:
   ```bash
   python create_mod.py
   ```

4. The script will ask for input values and create the necessary folder and files for your mod.

## Usage

Run the script from the command line and provide the following details when prompted:

- **name**: The name of your mod (this will also be the name of the folder).
- **title**: The title of your mod (by default, it is derived from the name by replacing underscores with spaces and using Title Case).
- **description**: A short description of your mod.
- **author**: Your name or the name of the mod author (defaults to `ozcodx`).
- **deps**: List of dependencies for your mod (optional).

Example:
```bash
python create_mod.py
```

## License

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for more details.
