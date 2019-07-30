import os
import glob
import imp
modules = {}
for path in glob.glob('test/[!_]*.py'):
    name, ext = os.path.splitext(os.path.basename(path))
    modules[name] = imp.load_source(name, path)

for module in modules:
    print(modules[module].moin())