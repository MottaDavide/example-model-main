export PYTHONPATH="./src"

if [[ -d .venv ]]; then
    source .venv/bin/activate
else
    echo "No virtualenv found."
    python -m venv .venv
    source .venv/bin/activate
    python -m pip install pdm
fi

if [[ -f .env ]]; then
    source script/source-env.sh .env
fi

if [[ -f config.local.sh ]]; then
    source config.local.sh
fi
