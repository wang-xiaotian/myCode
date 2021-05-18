python3 -m pip install ansible
wget https://static.alta3.com/projects/ansible/modules/setup.sh -O mod-setup.sh
wget https://static.alta3.com/projects/ansible/max_teardown.sh -O max_teardown.sh
bash max_teardown.sh
bash mod-setup.sh