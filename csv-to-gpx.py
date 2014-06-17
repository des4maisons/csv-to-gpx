import sys
from datetime import datetime
from pytz import timezone

eastern = timezone('US/Eastern')

def process_line(line):
    def strip(s):
        return s.strip()
    date, time, elapsed, distance, speed, lat, lng, accuracy, altitude = \
        map(strip, line.split(','))
    timestamp = datetime.strptime(date + time, '%d/%m/%y%H:%M:%S %p GMT-4')
    timestamp = eastern.localize(timestamp)
    return dict(
        time=timestamp,
        lat=lat,
        lng=lng,
        altitude=altitude,
    )


def gpx_header():
    return """\
<?xml version="1.0"?>
<gpx
 version="1.0"
 xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
 xmlns="http://www.topografix.com/GPX/1/0"
 xsi:schemaLocation="http://www.topografix.com/GPX/1/0 http://www.topografix.com/GPX/1/0/gpx.xsd">
  <trk>
    <trkseg>
"""


def gpx_footer():
    return """\
    </trkseg>
  </trk>
</gpx>
"""


def gpx_datapoint(data):
    foo = data.copy()
    foo['time'] = data['time'].isoformat()
    return """\
<trkpt lat="{lat}" lon="{lng}">
  <ele>{altitude}</ele>
  <time>{time}</time>
</trkpt>""".format(**foo)


def output_xml(datapoints):
    print gpx_header()
    for datum in datapoints:
        print gpx_datapoint(datum)
    print gpx_footer()


def process_file(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
    datapoints = map(process_line, lines[1:])
    output_xml(datapoints)


if __name__ == "__main__":
    if not len(sys.argv) == 2:
        sys.stderr.write("usage: " + sys.argv[0] + " <filename>")
        sys.exit(1)
    filename = sys.argv[1]
    process_file(filename)
