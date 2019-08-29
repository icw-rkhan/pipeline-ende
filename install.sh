echo
echo "If you re-install this program, your old EnDe keys will be invalid. Do you wish to install this program ?"

select yn in "Yes" "No"; do
    case $yn in
        Yes ) break;;
        No ) exit;;
    esac
done


echo "*******EnDE Instalation -Begin*********"


ENDE_HOME="/devtools/pipeline-ende"
sudo python "$ENDE_HOME/ende.py" --install
echo [pipeline-ende] install done.

echo "---Running Test -Begin---"
test="raja_khan"
x="$(python "$ENDE_HOME/ende.py" --encr $test)"
y="$(python "$ENDE_HOME/ende.py" --decr $x)"


if [ "$test" = "$y" ]; then
    echo "Test Passed"
else
    echo "Test Failed: $y"
fi

echo "---Running Test -END---"


echo "*******EnDE Instalation -Finish-*********"
