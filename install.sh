export ENDE_HOME="$HOME/rkhan/pipeline-ende"
python3 "$ENDE_HOME/ende.py" --install
chmod +x ende.sh
export PATH=$PATH:$ENDE_HOME
echo [pipeline-ende] install done.
