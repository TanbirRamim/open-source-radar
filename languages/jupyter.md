# Jupyter Notebook quickstart

Jupyter notebooks are interactive documents that combine code, notes and results. A notebook runs code in a kernel, usually in the Python environment you selected.

Open Jupyter Notebook issues: [Jupyter issue list](../issues/by-language/jupyter.md)

## Setup

Install Python, then create and activate an isolated environment for the project:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

On Windows PowerShell, activate it with:

```powershell
.venv\Scripts\Activate.ps1
```

Install the notebook interface and Python kernel in that environment:

```bash
python -m pip install --upgrade pip
python -m pip install notebook ipykernel
```

For other installation options, see [Project Jupyter's install guide](https://jupyter.org/install).

## Common commands

| Task | Usual command |
| --- | --- |
| Install the Notebook interface and Python kernel | `python -m pip install notebook ipykernel` |
| Start the Notebook server | `jupyter notebook` |
| Strip output from a notebook | `nbstripout path/to/notebook.ipynb` |
| Clear output with nbconvert | `jupyter nbconvert --clear-output --inplace path/to/notebook.ipynb` |

## Run a notebook

From the project directory, start the server:

```bash
jupyter notebook
```

The browser opens the notebook dashboard. Choose **New → Python 3** to create a notebook, or open an existing `.ipynb` file. Run the current cell with **Shift+Enter**. Keep the notebook in the same environment where you installed its project dependencies.

## Clear outputs before committing

Notebook outputs can make diffs large or include local results. Strip them before committing:

```bash
python -m pip install nbstripout
nbstripout path/to/notebook.ipynb
```

Alternatively, use nbconvert if it is installed:

```bash
jupyter nbconvert --clear-output --inplace path/to/notebook.ipynb
```

See the [nbstripout usage guide](https://github.com/kynan/nbstripout#usage) and [nbconvert configuration options](https://nbconvert.readthedocs.io/en/stable/config_options.html).

## Before you push

- [ ] Run the notebook with the intended kernel and check that its cells work in order.
- [ ] Clear generated outputs and review the diff for unintended changes or sensitive results.
- [ ] Follow the project’s own contribution guide and tests.

Back to [all languages](README.md) · [Guide](../guide/README.md)
