import os

import logging

from click.testing import CliRunner

from app import create_log_folder

runner = CliRunner()

def test_log_file_is_created_or_not():
    response = runner.invoke(create_log_folder)
    assert response.exit_code == 0
    root = os.path.dirname(os.path.abspath(__file__))
    # set the name of the apps log folder to logs
    logdir = os.path.join(root, '../app/logs')
    # make a directory if it doesn't exist
    if not os.path.exists(logdir):
        os.mkdir(logdir)
    # Validating if a directory is present or not
    assert os.path.exists(logdir) == True

    # set the path for creating the log file
    log_file = os.path.join(logdir, 'test_log.log')

    # creating the log file
    handler = logging.FileHandler(log_file)

    # validating if the log file is being created or not.
    assert os.path.exists(log_file) == True