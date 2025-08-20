def find_missing_ranges(frames):
    # order the list
    for l in range(len(frames)):
        for num in range(0, len(frames) - l - 1):
            if frames[num] > frames[num+1]:
                frames[num], frames[num + 1] = frames[num + 1] , frames[num]

    # find the missing frames
    missing_frames = []

    for i in range(len(frames)-1):
        current_num = frames[i]
        next_num = frames[i + 1]

        if next_num - current_num > 1:
            for num in range(current_num+1, next_num):
                missing_frames.append(num)

    # find the gaps
    gaps = []
    if missing_frames:
        start = missing_frames[0]
        end = missing_frames[0]

        for num in missing_frames[1:]:
            if num == end + 1:
                end = num
            else:
                gaps.append([start,end])
                start = end = num
        gaps.append([start, end])

    # find the longest gap         
    longest_gap = []
    max_length = 0
    for g in gaps:
        length = g[1] - g[0] + 1
        if length > max_length:
            max_length = length
            longest_gap = g

    
    missing_count = len(missing_frames)


    result = {"gaps": gaps, "longest gap": longest_gap, "missing_count": missing_count}
    return result


    