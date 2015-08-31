class ResourceManager(object):
	image_path_list = []
	sound_path_list = []
	scene_path_list = []

	def read_resources(file_name):
		with open(file_name) as file:
			ResourceManager.read_scenes(file)
			ResourceManager.read_image(file)
			ResourceManager.read_sound(file)
			file.close()

	def read_scenes(file):
		scene_num = int(file.readline().strip().split(' ')[1])

		for i in range(scene_num):
			scene_path = file.readline().strip()
			ResourceManager.scene_path_list.append(scene_path)

	def read_image(file):
		image_num = int(file.readline().strip().split(' ')[1])

		for i in range(image_num):
			file.readline()
			image_path = file.readline().strip()
			ResourceManager.image_path_list.append(image_path)

	def read_sound(file):
		sound_num = int(file.readline().strip().split(' ')[1])

		for i in range(sound_num):
			file.readline()
			sound_path = file.readline().strip()
			ResourceManager.sound_path_list.append(sound_path)