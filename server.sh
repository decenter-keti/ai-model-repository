HERE=$(dirname $(realpath $0))
export PYTHONPATH=$HERE/
VIBE_UWSGI=$HERE/uwsgi_decenter.ini
uwsgi -i $VIBE_UWSGI
