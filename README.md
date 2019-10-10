# Example of a stream connector in Python

At Device Insight the software CS Edge is used to send data to the Center Sight platform. It is possible to extend the functionality by adding a so called stream connector. Basically CS Edge needs to be configured to the start the script (see Centersight Edge manual) and gets started automatically.

This example shows how a python script can be used as a stream connector.

## Functionality

The stream connector needs to print the data as a string to stdout in the following format:

<code>{"datapointValue": {"key": "\<name of the datapoint>", "value": "\<value of the datapoint>", "dataType": "\<type of the datapoint", "tsIso8601": "\<timestamp>"}}</code>

Format of the timestamp needs to be according to Iso 8601:

2013-12-02T12:30:02.003+01:00
yyyy-MM-DDThh:mm:ss.fffT