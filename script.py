import grp, os

def ListAllUsersWithoutGroup():
	allUsers = getAllUsers()
	allUsersWithAdditionalGroup = []
	for group in grp.getgrall():
		for group_member in group.gr_mem:
			if (group_member not in allUsersWithAdditionalGroup and group_member in allUsers):
				allUsersWithAdditionalGroup.append(group_member)
	print('All users who do not have any group:')
	printAList(user for user in allUsers if user not in allUsersWithAdditionalGroup)

def getAllUsers():
	data = []
	with open('/etc/passwd', 'r') as f:
		for line in f.readlines():
			split = line.split(":")
			if (int(split[2]) >= 1000 and split[5].startswith('/home/')):
				data.append(split[0])
	return data

def printAList(list):
	for index, element in enumerate(list):
		print(f'{index + 1}: {element}')

def ListAllGroupsWithUsers():
	for index, group in enumerate(grp.getgrall()):
		if (len(group.gr_mem) == 0):
			continue
		print(f'{index + 1}: {group.gr_name}:')
		for i, group_member in enumerate(group.gr_mem):
			print(f'- {i + 1} {group_member}')

if __name__ == '__main__':
	print('Would you like to list all users without a group or would you like to list all users in groups?')
	action = 0
	while action != 1 and action != 2:
		print('all users without a group - 1')
		print('list all users in groups - 2')
		try :
			action = int(input(''))
		except:
			print('Input either 1 or 2')
	os.system('clear')
	if (action == 1):
		ListAllUsersWithoutGroup()
	else:
		ListAllGroupsWithUsers()
