# JINC (Jupyter Interactive Notebook Creator)

## Purpose

JINC (Jupyter Interactive Notebook Creator) is a utility project that provides a simple way to convert Python scripts with specially formatted comments into Jupyter notebooks. It's particularly useful for data scientists and analysts who prefer to write their initial code in a text editor but want to present their work in a more interactive and visually appealing Jupyter notebook format.

## What does JINC stand for?

- J: Jupyter
- I: Interactive
- N: Notebook
- C: Creator

## Features

- Converts Python scripts to Jupyter notebooks (.ipynb files)
- Supports markdown and code cells
- Easy to use command-line interface
- Smart output naming: By default, uses the input filename with a .ipynb extension
- Option for customizable output file name

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/vedanta/jinc.git
   cd jinc
   ```

2. Install the required dependencies:
   ```
   pip install nbformat
   ```

## Usage

1. Prepare your Python script with special comments to denote markdown and code cells:

   - Use `# MARKDOWN CELL` to start a markdown cell
   - Use `# CODE CELL` to start a code cell
   - Regular Python comments in code cells will be preserved

   Example:
   ```python
   # MARKDOWN CELL
   # # My Analysis
   # This notebook demonstrates some data analysis.

   # CODE CELL
   import pandas as pd
   import numpy as np

   # Load the data
   data = pd.read_csv('data.csv')

   # MARKDOWN CELL
   # ## Data Preview
   # Let's take a look at the first few rows of our data.

   # CODE CELL
   print(data.head())
   ```

2. Run the script:
   ```
   python jinc.py your_script.py
   ```

   This will create `your_script.ipynb` in the same directory.

3. To specify a custom output file name, use the `-o` or `--output` option:
   ```
   python jinc.py your_script.py -o My_Custom_Notebook.ipynb
   ```

## Smart Output Naming

JINC now features smart output naming:

- If you don't specify an output filename, JINC will automatically use the input filename and change the extension to `.ipynb`.
  For example, `python jinc.py analysis.py` will create `analysis.ipynb`.

- You can still specify a custom output name using the `-o` or `--output` option if you prefer.

This feature makes it easier to keep your Python scripts and the resulting Jupyter notebooks organized with matching names.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
