import subprocess
import tempfile

def _exec_notebook(path):
    with tempfile.NamedTemporaryFile(suffix=".ipynb") as fout:
        args = ["jupyter", "nbconvert", "--to", "notebook", "--execute",
                "--ExecutePreprocessor.timeout=1000",
                "--output", fout.name, path]
        subprocess.check_call(args)

def test():
    _exec_notebook('Python_Object_and_Data_Structure_Basics/numbers.ipynb',)
    _exec_notebook('Python_Object_and_Data_Structure_Basics/variable_assignments.ipynb', )
    _exec_notebook('Python_Object_and_Data_Structure_Basics/strings.ipynb', )
