echo "ENV CREATE STARTING"
conda create -p venv/ python==3.10 -y
# =  +
conda activate venv/
echo "ENV CREATE FINISHING"
pip install -r requirements.txt
echo "REQUIREMENTS INSTALLED"