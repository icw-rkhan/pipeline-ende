export ENDE_HOME="$HOME/rkhan/pipeline-ende"
python3 "$ENDE_HOME/ende.py" --install
chmod 777 "$ENDE_HOME/ende.sh"
chmod 777 "$ENDE_HOME/test.sh" 
export PATH=$PATH:$ENDE_HOME
echo [pipeline-ende] install done.
