test="raja_khan"
x="$(python3 ende.py --encr $test)"
y="$(python3 ende.py --decr $x)"
echo $test

if [ "$test" = "$y" ]; then
    echo "Test Passed"
else
    echo "Test Failed: $y"
fi
