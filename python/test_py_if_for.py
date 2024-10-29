import random



def test_if():
	user_pass = input("Enter user pass>");

	print(user_pass[0:len(user_pass)-1])
	if "e" in user_pass:
		print(" e is in your message.")
	else:
		print("e is not in your message.")

	if user_pass != "secret" and user_pass != "secret1" :
		print("Incorrect password, exiting function");
		return 1

	if user_pass not in ["secret", "secret1"] :
		print("Incorrect password, exiting function");
		return 1
	return 0


def test_loops():
	response = ""
	print("Enter response>");
	while response != "OK":
		response = input();
	print("You entered correct responce");

	for i in range(0, 50, 5):
		print(i, end=" ")