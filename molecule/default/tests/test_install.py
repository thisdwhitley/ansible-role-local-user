import os
import pytest

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


@pytest.mark.parametrize("username,fullname,sudoer,create_dirs", [
    ("user_full_sudoer_dirs", "Full Sudoer Dirs", "true", ("GIT","BACKUP")),
    ("user_sudoer_dirs", "", "true", "PERSONAL"),
    ("user_full_dirs", "Full Dirs", "", "newdir"),
    ("user_nothing", "", "", "")
])
def test_new_users(host, username, fullname, sudoer, create_dirs):
    user = host.user(username)

    assert user.exists


    # assert host.user(username).gecos == fullname
    # assert host.file(create_dirs).exists


# def test_directories(host, username, fullname, sudoer, create_dirs):
#     # assert host.user(username).exists
#     assert host.file(create_dirs).exists


# @pytest.mark.parametrize("name", ["GIT","BACKUP"])
# def test_dirs(testing, name):
#     assert testing("/home/new_user1/"name).is_directory
