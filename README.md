csv-to-gpx
----------

This script takes csv output from the Speed Tracker android app and converts it
to a gpx file that contains enough information for endomondo to import it.
(The gpx file exported by Speed Tracker by default does not contain date-time
information for each of the tracked points, which endomondo needs)

installation
============

```bash
cd $repo
virtualenv env
env/bin/pip install -r requirements.txt
```

usage
=====

```bash
env/bin/python csv-to-gpx.py speed-tracker-output.csv > endomondo.gpx
```
