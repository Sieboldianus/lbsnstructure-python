![pypi version](https://lbsn.vgiscience.org/structure/python/version.svg) ![pipeline status](https://gitlab.vgiscience.de/lbsn/structure/python/badges/master/pipeline.svg) from protobuf: ![version](https://lbsn.vgiscience.org/structure/protobuf/version.svg) 

# LBSNSTRUCTURE

A python compiled version of the [common location based social network (LBSN) data structure concept](https://gitlab.vgiscience.de/lbsn/concept) (ProtoBuf) to handle cross network Social Media data in Python.
There are several motivations for prividing a common LBSN interchange data structure. Firstly, the [GDPR](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32016R0679) directly requests Social Media Network operators to allow users to transfer accounts and data inbetween services. 
While there are attempts by Google, Facebook etc. (see [data-transfer-project](https://github.com/google/data-transfer-project)), it is not currently possible. With this structure concept, we follow an independent road.
A primary goal is to systematically characterize LBSN data aspects in a common scheme that enables privacy-by-design for connected software, transfer scripts and database design.

The Github-repository of this protobuf-derived package can be found here:
https://github.com/Sieboldianus/lbsnstructure-python

## Quick Start

Install with:  
```shell
pip install --upgrade lbsnstructure
```

Import to python project with:  
```python
import lbsnstructure as lbsn
post = lbsn.Post()
place = lbsn.Place()
```

.. or compile newest version from [Protofiles](https://gitlab.vgiscience.de/lbsn/concept)

1. Clone git Repository `git clone git@gitlab.vgiscience.de/lbsn/concept`
2. Install [Protocoll Buffers](https://github.com/google/protobuf/releases)
3. Compile structure to python package `protoc --python_out=examples/python lbsnstructure/structure.proto`  
4. Install with `pip install .` in examples/python

## Developers

For development & testing, make a local clone of this repository  
```shell
git clone git@gitlab.vgiscience.de:lbsn/structure/python.git
```

Go to subfolder `examples\python` and (e.g.) symlink the folder to your  
Python's site-packages folder with:  
```shell
pip install --editable .
```

Now, lbsnstructure should be available through your python path and directly link to the local git clone directory.

## Versioning

For the releases available, see the [tags on this repository](/../tags). 
The versioning (major.minor.patch) is automated using [python-semantic-release](https://github.com/relekang/python-semantic-release).
Commit messages that follow the [Angular Commit Message Conventions](https://github.com/angular/angular.js/blob/master/DEVELOPERS.md#-git-commit-guidelines) will be automatically interpreted, 
followed by version bumps if necessary. 

## License

This project is licensed under the  MIT License.
