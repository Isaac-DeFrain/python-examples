import datetime

# Parse the ISO 8601 datetime string

# Mina Protocol

## epoch 42
dt42_start = datetime.datetime.strptime('2022-12-01T18:00:00Z', '%Y-%m-%dT%H:%M:%SZ')
dt42_end   = datetime.datetime.strptime('2022-12-16T14:59:59Z', '%Y-%m-%dT%H:%M:%SZ')

## epoch 43
dt43_start = datetime.datetime.strptime('2022-12-16T15:00:00Z', '%Y-%m-%dT%H:%M:%SZ')
dt43_end   = datetime.datetime.strptime('2022-12-31T11:59:59Z', '%Y-%m-%dT%H:%M:%SZ')

# convert datetime to timestamp
ts42_start = dt42_start.timestamp()
ts42_end   = dt42_end.timestamp()
ts43_start = dt43_start.timestamp()
ts43_end   = dt43_end.timestamp()

# convert timestamp to ticks
start42 = int(ts42_start * 10000000)
end42   = int(ts42_end * 10000000)
start43 = int(ts43_start * 10000000)
end43   = int(ts43_end * 10000000)

print(f"epoch 42: {start42} - start")
print(f"epoch 42: {end42} - end")
print(f"epoch 43: {start43} - start")
print(f"epoch 43: {end43} - end")
