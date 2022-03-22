# python package
  ------


#### 1. Create package and project
  - `process` : will be the package that we want to import into a new project
  -  `project1` :  will contain a module wich import the process package

  Directory should looks like this :
```
├── process
│   ├── process
│   │   ├── __init__.py
│   │   ├── process.py
│   │   └── __pycache__
│   ├── process.egg-info
│   │   ├── dependency_links.txt
│   │   ├── PKG-INFO
│   │   ├── SOURCES.txt
│   │   └── top_level.txt
│   ├── README.md
│   └── setup.py
└── project1
    ├── src
    │   └── main.py
    └── venv
```

#### 2. Import package in python venv
```bash
cd project1
source venv/bin/activate
# Install process package (-e means that we can modify package without import again)
pip install -e ../process
```

then import package in `main.py`
```python
from process.process import process
```
