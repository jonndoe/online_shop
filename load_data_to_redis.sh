#!/bin/bash

echo "export -f conda"
echo "export -f __conda_activate"
echo "export -f __conda_reactivate"
echo "export -f __conda_hashr"
echo "export -f __add_sys_prefix_to_path"
echo 'eval "$(conda shell.bash hook)"'

source ~/miniconda3/etc/profile.d/conda.sh
conda activate env38_online_shop
pip list
python manage.py shell < load_data_to_redis.py

echo "finishing task"
