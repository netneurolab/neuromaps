#!/bin/bash -e

echo "Installing dependencies"

python -m pip install --upgrade pip build wheel
python -m pip install --upgrade -r requirements.txt

if [ -n "${OPTIONAL_DEPENDS}" ]; then
    for DEP in ${OPTIONAL_DEPENDS}; do
        if [ ${DEP} == "mayavi" ]; then
            python -m pip install numpy vtk
            sudo apt-get install -y xvfb \
                                    x11-utils \
                                    mencoder \
                                    libosmesa6 \
                                    libglx-mesa0 \
                                    libopengl0 \
                                    libglx0 \
                                    libdbus-1-3 \
                                    qt5-default
        fi
        python -m pip install $DEP || true
    done
fi

echo "Finished installed dependencies"
