#!/usr/bin/env bash
# hehe
workon ci-cd
pip install -r requirements.txt
python ./ci_cd/tests/test_use_testsuite.py