from dataclasses import dataclass
import datetime
import re

DATETIME_FORMAT = '%Y-%m-%d %H:%M'
TIMESTAMP_REGEX = re.compile('^.*\[(?P<timestamp>.+)\].*$')
SHIFT_START_REGEX = re.compile('^.*Guard #(?P<id_num>\d+) begins.*$')


# Actions
SHIFT_STARTS = 'SHIFT_STARTS'
WAKES_UP = 'WAKES_UP'
FALLS_ASLEEP = 'FALLS_ASLEEP'

@dataclass
class Event:
    id_num: int
    timestamp: datetime.datetime
    action: str

    def __cmp__(self, other):
        if self.timestamp > other.timestamp:
            return 1
        elif self.timestamp < other.timestamp:
            return -1
        else:
            return 0

    def __lt__(self, other):
        return self.timestamp < other.timestamp

    def __gt__(self, other):
        return self.timestamp > other.timestamp


def parse_line(line):
    id_num = None
    action = None

    m = TIMESTAMP_REGEX.search(line)
    timestamp_string = m.group('timestamp')
    timestamp = datetime.datetime.strptime(timestamp_string, DATETIME_FORMAT)

    if 'begins' in line:
        action = SHIFT_STARTS
    elif 'wakes' in line:
        action = WAKES_UP
    elif 'asleep' in line:
        action = FALLS_ASLEEP
    else:
        raise ValueError('Unrecognized action')

    if action == SHIFT_STARTS:
        m = SHIFT_START_REGEX.search(line)
        id_num = int(m.group('id_num'))

    return Event(id_num, timestamp, action)

def events_to_timeline(events):
    sorted_events = sorted(events)
    prev_id_num = None
    for event in sorted_events:
        if event.id_num is None:
            event.id_num = prev_id_num
        else:
            prev_id_num = event.id_num
    return sorted_events


if __name__ == '__main__':
    with open('input', 'r') as f:
        lines = f.readlines()
    events = [parse_line(line) for line in lines]
    timeline = events_to_timeline(events)

    minute_count_by_guard = {}
    guard_id = None
    sleep_start_minute = None
    sleep_stop_minute = None
    for event in timeline:
        if event.action == SHIFT_STARTS:
            guard_id = event.id_num
        elif event.action == FALLS_ASLEEP:
            sleep_start_minute = event.timestamp.minute
        elif event.action == WAKES_UP:
            sleep_stop_minute = event.timestamp.minute
            for minute in range(sleep_start_minute, sleep_stop_minute):
                minute_counts = minute_count_by_guard.get(guard_id, {})
                minute_counts[minute] = minute_counts.get(minute, 0) + 1
                minute_count_by_guard[guard_id] = minute_counts

    most_consistent_guard_id = None
    most_slept_minute = None
    max_minute_count = 0

    for guard_id, minute_counts in minute_count_by_guard.items():
        for minute, count in minute_counts.items():
            if count > max_minute_count:
                most_consistent_guard_id = guard_id
                most_slept_minute = minute
                max_minute_count = count

    answer = most_consistent_guard_id * most_slept_minute

    print(answer)
