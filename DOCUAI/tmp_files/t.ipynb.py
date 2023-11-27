#!/usr/bin/env python
# coding: utf-8

# In[5]:


from nbconvert import PythonExporter
import nbformat

exporter = PythonExporter()

with open("test.ipynb", "r") as f:
    data = f.read()

code, _ = exporter.from_notebook_node(nbformat.reads(data, as_version=4))

print(code)

