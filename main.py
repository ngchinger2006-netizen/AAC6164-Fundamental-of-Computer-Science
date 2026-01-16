import os
import datetime

def main():
	print("===Linux Monitoring System===")

	#Current time
	now = datetime.datetime.now()
	print("Current Time:", now)

	#System info
	os.system("uname -a")

	#Create reports directory if not exists
	if not os.path.exists("reports"):
		os.mkdir("reports")

	#Write report file
	with open("reports/system_report.txt","w") as f:
		f.write("===Linux Monitoring System Report===\n")
		f.write("Generate at: " + str(now) + "\n")

	print("Report generated in reports/system_report.txt")

if __name__ == "__main__":
	main()

