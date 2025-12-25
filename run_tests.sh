#!/bin/bash

# Compile
g++ -o prog solution.cpp

# Test all cases
for i in {1..14}; do
  ./prog < $i.in > output.txt
  if diff -q output.txt $i.out > /dev/null; then
    echo "Test $i: ✓ PASS"
  else
    echo "Test $i: ✗ FAIL"
    echo "Expected:"
    cat $i.out
    echo "Got:"
    cat output.txt
    echo "---"
  fi
done

rm output.txt