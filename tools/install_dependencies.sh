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

while true; do
    wget --retry-connrefused --waitretry=1 --read-timeout=20 --timeout=15 -t 0 --no-dns-cache -c \
        https://www.humanconnectome.org/storage/app/media/workbench/workbench-linux64-v1.5.0.zip && break
done
unzip workbench-linux64-v1.5.0.zip -d "${HOME}"
echo "${HOME}/workbench/bin_linux64" >> "${GITHUB_PATH}"

echo "Finished installed dependencies"
