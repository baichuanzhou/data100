#! /bin/bash
for D in */; do sed '1i OK_FORMAT=True' "${D}"/tests/*.py -i; done
