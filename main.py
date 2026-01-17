import os
import time
import datetime

MONITORED_DIR = "monitored_dir"
REPORT_DIR = "reports"
REPORT_FILE = "reports/directory_report.txt"

def snapshot_directory():
	files = {}
	for filename in os.listdir(MONITORED_DIR):
		path = os.path.join(MONITORED_DIR, filename)
		if os.path.isfile(path):
			stat = os.stat(path)
			files[filename] = {
				"size" : stat.st_size,
				"mtime" : stat.st_mtime
			}
	return files

def main():
	if not os.path.exists(REPORT_DIR):
		os.mkdir(REPORT_DIR)

	print("Taking initial directory snapshot...")
	before = snapshot_directory()

	print("Waiting for changes... (60 seconds)")
	print("Please add, delete, or modify files in monitored_dir now.")
	time.sleep(60)

	after = snapshot_directory()

	now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

	with open(REPORT_FILE, "a") as report:
		report.write(f"\nDirectory Monitoring Report - {now}\n")

		# File creation
		for f in after:
			if f not in before:
				report.write(f"[CREATED] {f} at {now}\n")

		# File deletion
		for f in before:
			if f not in after:
				report.write(f"[DELETED] {f} at {now}\n")

		# File modification
		for f in before:
			if f in after and before[f]["mtime"] != after[f]["mtime"]:
				report.write(f"[MODIFIED] {f} at {now}\n")

	print("Directory monitoring completed.")
	print(f"Report saved to {REPORT_FILE}")


if __name__=="__main__":
	main()
