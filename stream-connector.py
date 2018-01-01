#!/usr/bin/env python
from time import sleep
from random import random
from datetime import datetime

if __name__ == "__main__":

    while True:
            sleep(1.0)
            temperature = random() * 100
            now = datetime.utcnow().isoformat()
            print('{"datapointValue": {"key": "temp", "value": "%s", "dataType": "Float", "tsIso8601": "%sZ"}}' % (temperature, now))
