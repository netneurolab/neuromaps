#!/bin/bash -e

echo "Running tests"

echo CHECK_TYPE = $CHECK_TYPE

if [ "$CHECK_TYPE" == "style" ]; then
    flake8 brainnotation examples
elif [ "$CHECK_TYPE" == "doc" ]; then
    cd docs
    make html && make doctest
elif [ "$CHECK_TYPE" == "test" ]; then
    mkdir for_testing
    cd for_testing
    cp ../setup.cfg .
    $xvfbrun pytest --doctest-modules --cov brainnotation --cov-report xml \
                    --junitxml=test-results.xml -v --pyargs brainnotation
else
    false
fi

echo "Tests finished"
