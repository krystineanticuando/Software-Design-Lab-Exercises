import pickle


myList = [1, 3, 4]

def repeat():
	with open('dd.dat', 'wb') as f:
		pickle.dump(myList, f)
	
	newList = []



	with open('dd.dat', 'rb') as f:
		newList = pickle.load(f)
		
	print(newList)


def main():
	repeat()
	repeat()

if __name__ == '__main__':
	main()