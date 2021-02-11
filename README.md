# srw2ho ppmpmessage Library

### For all steps set username first (if not already set by system)
```bash

```

### Installation from Repository (online)
```bash

pip install git+https://github.com/srw2ho/ppmpmessage.git
```

### Build distributable package (without dependencies -> online installation)
```bash
python setup.py bdist_wheel
```

### Download all dependencies (for offline installation)
```bash
cd dist

pip wheel git+https://github.com/srw2ho/ppmpmessage.git

# copy dist to offline device

# install (on offline device)
pip install --no-index --find-links=.\ppmpmessage-xxx.whl
```

### Usage


Build Docker
    docker build  . -t ppmpmessage

    
```
