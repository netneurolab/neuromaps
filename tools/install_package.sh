#!/bin/bash -e

echo "Building and installing brainnotation"

python -m build

if [ "$INSTALL_TYPE" == "setup" ]; then
  python -m pip install .
elif [ "$INSTALL_TYPE" == "sdist" ]; then
  python -m pip install dist/*.tar.gz
elif [ "$INSTALL_TYPE" == "wheel" ]; then
  python -m pip install dist/*.whl
else
  false
fi

python -c 'import brainnotation; print(brainnotation.__version__)'

pip install "brainnotation[$CHECK_TYPE]"

echo "Done installing brainnotation"
