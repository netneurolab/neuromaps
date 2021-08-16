#!/bin/bash -e

echo "Running tests"

echo CHECK_TYPE = $CHECK_TYPE

if [ "$CHECK_TYPE" == "style" ]; then
    flake8 neuromaps examples
elif [ "$CHECK_TYPE" == "doc" ]; then
    cd docs
    make html && make doctest
elif [ "$CHECK_TYPE" == "test" ]; then
    mkdir for_testing
    cd for_testing
    cp ../setup.cfg .
    $xvfbrun pytest --doctest-modules --cov neuromaps --cov-report xml \
                    --junitxml=test-results.xml -v --pyargs neuromaps
else
    false
fi

echo "Tests finished"
