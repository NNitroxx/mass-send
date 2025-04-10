import scratchattach as sa
import random
import time

username = input("put your scratch username: ")
password = input("put your scratch password: ")

try:
	session = sa.login(username, password)
except Exception as e:
	print(f"error logging in: {e}")
else:
	print(f"logged on as {username}")

check_type = input("find accounts from studio, project, or user: ")
if check_type == "user":
	check_from = input("type username to find accounts from (CHOSE USER WITH VERY ACTIVE COMENTS!!!): ")
	place = session.connect_user(check_from)
elif check_type == "studio":
	check_from = input("type studio id to find accounts from (CHOSE STUDIO WITH VERY ACTIVE COMENTS!!!): ")
	place = session.connect_studio(int(check_from))
elif check_type == "project":
	check_from = input("type project id to find accounts from (CHOSE PROJECT WITH VERY ACTIVE COMENTS!!!):")
	place = session.connect_project(int(check_from))

message = input("type message to send to everyone: ")

posted = []

while True:
	comment = place.comments(limit=1)[0]

	try:
		target = session.connect_user(comment.author_name)
	except Exception as e:
		print(f"error conecting to scraped user: {e}")
	if comment.author_name not in posted:
		try:
			target.post_comment(f"{random.randint(1000,9999)} {message}")
		except Exception as e:
			print(f"error posting comment: {e}")
		else:
			print(f"commented on {comment.author_name}")
	posted.append(comment.author_name)
	if session.new_scratcher:
		time.sleep(30)
	else:
		time.sleep(10)
