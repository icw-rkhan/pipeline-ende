export ENDE_HOME="$HOME/rkhan/pipeline-ende"
test="raja_khan"
x="$(python3 "$ENDE_HOME/ende.py" --encr $test)"
y="$(python3 "$ENDE_HOME/ende.py" --decr $x)"
echo $test

if [ "$test" = "$y" ]; then
    echo "Test Passed"
else
    echo "Test Failed: $y"
fi
