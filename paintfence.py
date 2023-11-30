def paintTheFence(ranges, n, q):

	# Part 1: Find all pairs
	pairs = []
	
	i = 0
	j = 0
	while i < q:
		j = i
		while j < q:
			if i < j:
				pairs.append((i, j))
			j += 1
		i += 1
	
	# Part 2: Use all pairs to find optimal result
	optimal_res = 0
	for ele in pairs:
		(ignore_painter1, ignore_painter2) = ele

		run_res = 0

		# dummy list to check if an fence is painted or not
		dummy_list = []
		for i in range(n):
			dummy_list.append(0)
		# iterate through all painters q - 2 and count the number of painted
		# fence using these q - 2 painters
		ori_res = 0
		for i in range(q):
			if i == ignore_painter1 or i == ignore_painter2:
				continue # skip to next iteration
			l, r = ranges[i]

			ori_res += r - l + 1
			# check if section from l to r has been painted or not
			for run in range(l-1, r):
				if dummy_list[run] == 0: # not painted yet, valid count in ori_res
					# update it as painted by ith painter
					dummy_list[run] = 1
				else: # already painted, not a valid count, decrease ori_res
					ori_res -= 1
		
		optimal_res = max(optimal_res, ori_res)

	return optimal_res