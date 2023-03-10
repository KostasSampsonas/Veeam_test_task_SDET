import os
import time
import shutil
import argparse
import logging


def main():
    parser = argparse.ArgumentParser(description='Sync folders.')
    parser.add_argument('source_folder', type=str, help='source folder path')
    parser.add_argument('destination_folder', type=str,
                        help='destination folder path')
    parser.add_argument('sync_interval', type=int,
                        help='synchronization interval time in seconds')
    parser.add_argument('log_file', type=str, help='log file path')
    args = parser.parse_args()

    # Create log file and set up logger
    logging.basicConfig(filename=args.log_file, level=logging.INFO)

    while True:
        try:
            # Remove the replica folder if it exists
            if os.path.exists(args.destination_folder):
                shutil.rmtree(args.destination_folder)

            # Copy the entire source folder to the replica folder
            shutil.copytree(args.source_folder, args.destination_folder)

            # Log successful synchronization
            logging.info(
                f'Successful synchronization at {time.strftime("%Y-%m-%d %H:%M:%S")}')

        except Exception as e:
            # Log synchronization failure
            logging.error(
                f'Failed synchronization at {time.strftime("%Y-%m-%d %H:%M:%S")}: {e}')

        # Wait for the specified sync interval
        time.sleep(args.sync_interval)


if __name__ == '__main__':
    main()


# I run it from the terminal by writing all of the above as one command:
# python sync_folder.py
# /home/dude/Documents/python/venvs/veeam/source_folder
# /home/dude/Documents/python/venvs/veeam/destination_folder/
# 60
# /home/dude/Documents/python/venvs/veeam/logs.log
