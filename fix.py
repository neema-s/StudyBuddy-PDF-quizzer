import nbformat

nb = nbformat.read("study_buddy.ipynb", as_version=4)

if "widgets" in nb.metadata:
    del nb.metadata["widgets"]

nbformat.write(nb, "study_buddy.ipynb")
