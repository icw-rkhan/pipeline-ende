test="raja_khan"
x="$(py ende.py --encr $test)"
y="$(py ende.py --decr $x)"
echo $test

if [ "$test" = "$y" ]; then
    echo "Test Passed"
else
    echo "Test Failed: $y"
fi