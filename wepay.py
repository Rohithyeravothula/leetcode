def alert(inputs, windowSize, allowedIncrease):
	input_length = len(inputs)
	prev_avg = None
	alert_count = 0
	alerts = {}
	for i in range(0, windowSize):
		alerts[i] = i
	for i in range(windowSize, input_length-windowSize+1):
		alerts[i]  = windowSize

	for i in range(input_length-windowSize+1, input_length):
		alerts[i] = input_length-i

	if input_length < windowSize:
		windowSize = input_length

	for i in range(0, input_length-windowSize+1):
		window = inputs[i:i+windowSize]
		# print(window)
		avg = sum(window)/len(window)
		for j in range(0, len(window)):
			if inputs[i+j] < avg*allowedIncrease:
				if alerts[i+j] == 1:
					return 1
				else:
					alerts[i+j] -= 1

		if prev_avg is not None:
			if avg >= prev_avg*allowedIncrease:
				return 1
		prev_avg = avg
	return 0


inps = [1,1,1,1,1,1]
windowSize_inp = 3
allowincr = 0.8
alert(inps, windowSize_inp, allowincr)



		