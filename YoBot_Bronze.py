# This file is part of YoBot_Bronze UCI Chess Engine.
# Copyright (C) 2021- Yohaan Seth Nathan (TheYoBots)
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the MIT License.
#
# You should have received a copy of the MIT License along with this 
# UCI Chess Engine. If not, view this https://opensource.org/licenses/MIT

import logging
import uci
import sys

def main():

    logging.basicConfig(filename='logs.txt', level=logging.INFO, format='%(asctime)s %(message)s')
    logging.info('YoBot Bronze started')

    try:
        while True:
            msg = input()
            uci.commandReceived(msg)

    except Exception:
        logging.exception('Fatal error in main loop')

if __name__ == '__main__':
    main()