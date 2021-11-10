#!/bin/bash -e

echo "Installing dependencies"

python -m pip install --upgrade pip build wheel
python -m pip install --upgrade -r requirements.txt

sudo apt-get update
sudo apt-get install -y libglu1-mesa

if [ -n "${OPTIONAL_DEPENDS}" ]; then
    for DEP in ${OPTIONAL_DEPENDS}; do
        if [ ${DEP} == "mayavi" ]; then
            python -m pip install numpy vtk
            sudo apt-get update
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

wget https://www.humanconnectome.org/storage/app/media/workbench/workbench-linux64-v1.5.0.zip
unzip workbench-linux64-v1.5.0.zip -d "${HOME}"
echo "${HOME}/workbench/bin_linux64" >> "${GITHUB_PATH}"

echo "Finished installed dependencies"
