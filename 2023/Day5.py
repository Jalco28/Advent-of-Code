from copy import copy


# with open('inputs/test5.txt', 'r') as f:
with open('inputs/Day5.txt', 'r') as f:
    data = f.read().split('\n\n')

seeds = data[0]
maps = data[1:]
seeds = [int(seed) for seed in seeds.split(': ')[1].split()]

for idx, map in enumerate(maps):
    maps[idx] = map.split('\n')[1:]
    for j, row in enumerate(maps[idx]):
        maps[idx][j] = [int(x) for x in row.split()]

# {map_idx -> {source_range -> delta}}
map_rules = {i: {} for i in range(7)}

for map_idx, map in enumerate(maps):
    for row in map:
        destination_start, source_start, length = row
        delta = destination_start-source_start
        source_range = range(source_start, source_start+length)
        map_rules[map_idx][source_range] = delta

locations = []
for seed in seeds:
    current_value = seed
    for map_idx, _ in enumerate(maps):
        for source_range, delta in map_rules[map_idx].items():
            if current_value in source_range:
                current_value += delta
                break
    locations.append(current_value)
print(locations)
print(min(locations))

# Part 2


class SeedRange:
    def __init__(self, start, length):
        self.start = start
        self.length = length

    def __repr__(self):
        return f'{self.start}-{self.end}'

    @property
    def end(self):
        return self.start+self.length-1

    def all_values(self):
        return range(self.start, self.start+self.length)

    def offset_range(self, delta):
        self.start += delta

    def split_range(self, a_final):
        """Splits into two objects
        this object is modified to contain self.start to a_final
        returned object contains a_final+1 till end"""
        a_length = a_final-self.start+1
        # a = SeedRange(self.start, a_length)
        b = SeedRange(a_final+1, self.length-a_length)
        self.length = a_length
        return b

    def take_chunk(self, chunk_start, chunk_length):
        """This object contains original start to chunk_start-1
        first returned object is the removed chunk
        second returned object is leftover numbers at end"""
        chunk = SeedRange(chunk_start, chunk_length)
        this_length = chunk_start-self.start
        leftovers = SeedRange(chunk_start+chunk_length,
                              self.length-chunk_length-this_length)
        self.length = this_length
        return chunk, leftovers


unprocessed = [SeedRange(seeds[i], seeds[i+1]) for i in range(0,len(seeds),2)]

for map in map_rules.values():
    processed = []
    while unprocessed:
        segment = unprocessed.pop(0)
        for source_range, delta in map.items():
            if segment.start >= source_range[0] and segment.end <= source_range[-1]:
                # Segment entirely inside source range
                segment.offset_range(delta)
                processed.append(segment)
                break
            if (segment.start <= source_range[0]) and (segment.end >= source_range[-1]):
                # Chunk of segment in source range
                chunk, leftover = segment.take_chunk(
                    source_range[0], len(source_range))
                unprocessed.append(segment)
                unprocessed.append(leftover)
                chunk.offset_range(delta)
                processed.append(chunk)
                break
            if segment.end in source_range and segment.start < source_range[0]:
                # Segment to left of rule source
                leftover = segment.split_range(source_range[0]-1)
                unprocessed.append(segment)
                leftover.offset_range(delta)
                processed.append(leftover)
                break
            if segment.start in source_range and segment.end > source_range[-1]:
                # Segment to right of rule source
                leftover = segment.split_range(source_range[-1])
                unprocessed.append(leftover)
                segment.offset_range(delta)
                processed.append(segment)
                break
        else:
            # No overlap
            processed.append(segment)
    unprocessed = copy(processed)

print(min(processed, key=lambda x: x.start).start)
