def draw_stars(x):
	stars = "*"
	for i in range(0, len(x)):
		if isinstance(x[i], int):
			print stars* x[i]
		elif isinstance(x[i], str):
			print x[i][0].lower() * len(x[i])


x = [4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"]
draw_stars(x)
