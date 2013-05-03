import os
import pickle
import test_radio

def get_last_modified_files(directory):
	file_time_tuple_list = []
	file_list = []
	for dirname, dirnames, filenames in os.walk(directory):
		for filename in filenames:
			filepath = os.path.join(dirname, filename)
			d = os.path.getmtime(filepath)
			file_time_tuple_list.append((d, filepath))
		pass
	file_time_tuple_list.sort(key=lambda x: x[0], reverse=1)

	for (time, filepath) in file_time_tuple_list:
		file_list.append(filepath)

	return file_list
	pass


def read_from_file_and_populate_data(filename):

	data = {}

	try:
		file_handle = open(filename, 'rb')
		data = pickle.load(file_handle)
		
	except Exception, e:
		raise IOError('Could not read file' + filename)

	finally:
		file_handle.close()

	return data

def flush_feedback_to_file(data):
	
	latest_feedback_files = []

	latest_feedback_files = get_last_modified_files('./feedback/')
	new_feedback_file = "./feedback/feedback." + str(len(latest_feedback_files) + 1)

	file_handle = open(new_feedback_file, 'wb')
	print 'File getter'
	print data

	pickle.dump(data, file_handle)
	file_handle.close()	
	pass

def read_from_file_and_populate_synonyms(filename):
	
	synonyms = {}

	try:
		file_handle = open(filename, 'rb')
		synonyms = pickle.load(file_handle)
		
	except Exception, e:
		raise IOError('Could not read file' + filename)

	finally:
		file_handle.close()

	return synonyms

def flush_synonyms_to_file(synonyms):
	
	latest_synonym_files = []

	latest_synonym_files = get_last_modified_files('./synonyms/')
	new_synonym_file = "./synonyms/synonyms." + str(len(latest_synonym_files) + 1)

	file_handle = open(new_synonym_file, 'wb')
	
	print 'File getter'
	print synonyms

	pickle.dump(synonyms, file_handle)
	
	file_handle.close()

	pass

if __name__ == '__main__':
	get_last_modified_files('./feedback/')
	get_last_modified_files('./synonyms/')
	pass

