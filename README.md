# Cookiecutter Kaggle Template

_A logical, reasonably standardized, but flexible project structure for doing Kaggle competitions._

Based on [drivendata.github.io/cookiecutter-data-science](http://drivendata.github.io/cookiecutter-data-science/)


### Requirements to use the cookiecutter template:
-----------
 - Python `>=3.9`
 - [Cookiecutter Python package](http://cookiecutter.readthedocs.org/en/latest/installation.html) >= 1.4.0: This can be installed with pip or by conda depending on how you manage your Python packages:
 - [Poetry Dependency Manager](https://github.com/python-poetry/poetry) >= 1.1.0

``` bash
pip install cookiecutter poetry
```

### To start a new project, run:

------------

    cookiecutter https://github.com/andrewsonin/cookiecutter-kaggle-template
Name your project with the name identical to the `<KAGGLE_NAME>` that appear in the command: `kaggle competitions download -c <KAGGLE_NAME>`.
Then run:

    cd <KAGGLE_NAME>
    make poetry
    poetry shell

And then run the following to download the Kaggle competition input files and install your python source files as a module:

    make download
    make pymodule

### The resulting directory structure
------------

The directory structure of your new project looks like this: 

```
├── LICENSE
├── Makefile               <- Makefile with commands like `make data` or `make train`
├── README.md              <- The top-level README for developers using this project.
├── data
│   ├── external           <- Data from third party sources.
│   ├── interim            <- Intermediate data that has been transformed.
│   ├── processed          <- The final, canonical data sets for modeling.
│   └── raw                <- The original, immutable data dump.
│
├── input                  <- Kaggle input files
│   │
│   ├── <KAGGLE_NAME>      <- Competition input files
│   │
│   └── src/<MODULE_NAME>  <- Source code for use in this project.
│       ├── __init__.py    <- Makes src/<MODULE_NAME> a Python module
│       │
│       ├── data           <- Scripts to download or generate data
│       │   └── make_dataset.py
│       │
│       ├── features       <- Scripts to turn raw data into features for modeling
│       │   └── build_features.py
│       │
│       ├── models         <- Scripts to train models and then use trained models to make
│       │   │                 predictions
│       │   ├── predict_model.py
│       │   └── train_model.py
│       │
│       ├── paths.py       <- File containing absolute paths to the useful directories
│       │
│       └── visualization  <- Scripts to create exploratory and results oriented visualizations
│           └── visualize.py
│
├── docs                   <- A default Sphinx project; see sphinx-doc.org for details
│
├── models                 <- Trained and serialized models, model predictions, or model summaries
│
├── output                 <- Kaggle output files
│
├── references             <- Data dictionaries, manuals, and all other explanatory materials.
│
├── reports                <- Generated analysis as HTML, PDF, LaTeX, etc.
│   └── figures            <- Generated graphics and figures to be used in reporting
│
├── requirements.txt       <- The requirements file for reproducing the analysis environment, e.g.
│                         generated with `pip freeze > requirements.txt`
│
├── tox.ini                <- tox file with settings for running tox; see tox.readthedocs.io
│
└── working                <- Jupyter notebooks. Naming convention is a number (for ordering), 
                           the creator's initials, and a short `-` delimited description, e.g.
                          `1.0-jqp-initial-data-exploration`.
```
