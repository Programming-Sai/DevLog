from argparse import *
import json
import re


# Issue Structure
'''
{
	'id': ''
	'title': '',
	'tag': 'solved' | 'pending' | 'ignored',
	'desc': '',
	'snippet': '',
	'solution-desc': '',
	'solution-snippet': '',
	'time-taken-to-solution': ''
},
'''
   

class pb(ArgumentParser):
	def __init__(self):
		super().__init__(description="Problem Tracker")  
		self.tracker_file = '.tracker.json'
		self.result_file = 'PROBLEMS.md'
		self.HOME_MESSAGE = """
🔹 DevLog - Your Personal Code Journal 📓

Usage:
  devlog <command> [options]

Commands:
  -i,  --init               Initialize a new issue tracker.
  -id, --id <id>            Set issue ID.
  -t,  --title <title>      Set issue title.
  -g,  --tag <status>       Set issue status (solved | pending | ignored).
  -l,  --language <lang>    Set the programming language.
  -d,  --desc <text>        Describe the issue.
  -s,  --snippet <code>     Code snippet for the issue.
  -sd, --solution-desc      Describe the solution.
  -ss, --solution-snippet   Code snippet for the solution.
  -tt, --time-taken         Time spent solving the issue.

  -c,  --compile            Generate markdown report.
       --file <name>        (Optional) Output file (default: PROBLEMS.md).
       --reverse            (Optional) Compile in reverse order (latest first).

  -del, --delete <id>        Delete an issue by ID.
  -clr,--clear              Permanently delete all issues.
  -ls, --list               Display all tracked issues.


Examples:
  devlog --init
  devlog --id 101 --title "Fix login bug" --desc "Login fails on mobile"
  devlog --id 101 --tag solved --solution-desc "Fixed API endpoint"
  devlog --list
  devlog --delete 101
  devlog --clear
  devlog --compile

OR

Examples:
  devlog -i
  devlog -id 101 -t "Fix login bug" -d "Login fails on mobile"
  devlog -id 101 -g solved -sd "Fixed API endpoint"
  devlog -ls
  devlog -del 101
  devlog -clr
  devlog -c --file my_log.md --reverse


Tip: Start by running 'devlog --init' OR 'devlog -i' to create your tracker.

🚀 Happy Coding!
"""

		self.subparsers = self.add_subparsers(dest="command", required=False, parser_class=ArgumentParser)
		self.problems = self.load_issues()
		self.add_arguments() 
		self.process_args()


	def add_arguments(self):
		self.add_argument('-i', '--init', action='store_true', help="Initialize a new issue tracker.")

		self.add_argument('-id', '--id', type=str, help="Unique identifier for the issue.")
		self.add_argument('-t', '--title', type=str, help="Title of the issue.")
		self.add_argument('-g', '--tag', type=str, help="Status of the issue (solved | pending | ignored).")
		self.add_argument('-l', '--language', type=str, help="Programming language related to the issue.")
		self.add_argument('-d', '--desc', type=str, help="Detailed description of the issue.")
		self.add_argument('-s', '--snippet', type=str, help="Code snippet demonstrating the issue.")
		self.add_argument('-sd', '--solution-desc', type=str, help="Explanation of the solution.")
		self.add_argument('-ss', '--solution-snippet', type=str, help="Code snippet for the solution.")
		self.add_argument('-tt', '--time-taken', type=str, help="Time taken to find the solution.")

		self.add_argument('-c', '--compile', action='store_true', help="Generate a detailed Markdown report of all logged issues.")
		self.add_argument('-f', '--file', type=str, help="Specify output markdown file (default is PROBLEMS.md).")
		self.add_argument('-r', '--reverse', action='store_true', help="Reverse the order of compilation (latest entries first).")
		
		self.add_argument('-del', '--delete', type=str, help="Delete a specific issue by ID.")
		self.add_argument('-clr', '--clear', action='store_true', help="Permanently remove all stored issues.")
		self.add_argument('-ls', '--list', action='store_true', help="Display a summary of all tracked issues.")


	

	def process_args(self):
		args = self.parse_args()
		if args.init:
			self.problems = []
			self.update_issues(self.problems)
			print("Initialised...")
		elif args.id:
			status = self.find_id_update_issue(args)
			self.update_issues(self.problems)
			print(f"{'Problem '+args.id+' Has been updated' if status else 'Problem '+args.id+' Has been created'}")
		elif args.compile:
			file_name = args.file if args.file else self.result_file
			reverse = args.reverse
			self.create_md(file_name, reverse)
		elif args.delete:
			self.delete_problem(args.delete)
		elif args.clear:
			self.problems = []
			self.update_issues(self.problems)
		elif args.list:
			self.show_problems()
		else:
			print(self.HOME_MESSAGE)

		
	def find_id_update_issue(self, args):
		new_problem = {}
		for problem in self.problems:
			if problem['id'] == args.id:
				problem['title'] = args.title or problem.get('title', '')
				problem['tag'] = args.tag or problem.get('tag', '')
				problem['language'] = args.language or problem.get('language', '')
				problem['desc'] = args.desc or problem.get('desc', '')
				problem['snippet'] = args.snippet or problem.get('snippet', '')
				problem['solution-desc'] = args.solution_desc or problem.get('solution-desc', '')
				problem['solution-snippet'] = args.solution_snippet or problem.get('solution-snippet', '')
				problem['time-taken'] = args.time_taken or problem.get('time-taken', '')
				return True
		new_problem['id'] = args.id or new_problem.get('id', '')
		new_problem['title'] = args.title or new_problem.get('title', '')
		new_problem['tag'] = args.tag or new_problem.get('tag', '')
		new_problem['language'] = args.language or new_problem.get('language', '')
		new_problem['desc'] = args.desc or new_problem.get('desc', '')
		new_problem['snippet'] = args.snippet or new_problem.get('snippet', '')
		new_problem['solution-desc'] = args.solution_desc or new_problem.get('solution-desc', '')
		new_problem['solution-snippet'] = args.solution_snippet or new_problem.get('solution-snippet', '')
		new_problem['time-taken'] = args.time_taken or new_problem.get('time-taken', '')
		self.problems.append(new_problem)
		return False

	def load_issues(self):
		try:
			with open(self.tracker_file, 'r') as j:
				res = json.load(j)
			return res
		except:
			res = []
			return res
	
	def update_issues(self, update):
		 with open(self.tracker_file, 'w') as j:
				json.dump(update, j, indent=4)

	def sluggifed_title(self, title):
		return  re.sub(r'[^\w\s-]', '', title).strip().lower().replace(' ', '-')

	def create_md(self, file_name, reverse):
		tag_emojis = {
			'solved': '✅',
			'pending': '⏳',
			'ignored': '🚫'
		}
		lines = ["# Problem Tracker", "<br><br>", "\n## 📋 Table of Contents", "<br>"]
		problem_items = self.problems[::-1] if reverse else self.problems
		# Add table of contents
		for problem in problem_items:
			lines.append(f"\n- [{problem['title']}](#🆔-{problem['id']}---{self.sluggifed_title(problem['title'])})\n")
		
		lines.append('\n---\n')

		for problem in problem_items:
				lines.append('\n---\n')

				lines.append(f'### 🆔 {problem['id']} - {problem['title']}\n')
				lines.append("<br>")
				lines.append(f"**Status:** {tag_emojis[problem['tag']]} {problem['tag'].capitalize()}\n")
				lines.append(f"\n**Language:** {problem['language'].capitalize()}\n")
				lines.append(f"\n**Time Taken:** {problem['time-taken']}\n")
				lines.append(f"\n### 🐞 Problem Description")
				lines.append("<br>")
				lines.append(f'\n{problem['desc']}\n')
				lines.append(f'''
```{problem['language']}
{problem['snippet']}
```
				''' if problem['snippet'] else '')
				# lines.append('<br><br>')
				if problem['solution-desc']:
					lines.append(f"\n### ✅ Solution Description")
					lines.append("\n<br>")
					lines.append(f'\n{problem['solution-desc']}\n')
					lines.append(f'''
```{problem['language']}
{problem['solution-snippet']}
```
				''' if problem['solution-snippet'] else '')
				lines.append("\n<br>\n")
				lines.append("<br>\n")

			
		with open(file_name, 'w', encoding="utf-8") as m:
			m.writelines(lines)

	def delete_problem(self, id):
		item_to_delete = ({}, -1)
		for idx, problem in enumerate(self.problems):
			if problem['id'] == id:
				item_to_delete = problem, idx
				break
		self.problems.pop(item_to_delete[1])
		self.update_issues(self.problems)

	def show_problems(self):
		if not self.problems:
			print("No issues found.")
			return

		# Define column headers
		headers = ["ID", "Title", "Status"]
		col_widths = [
			max(len(problem["id"]) for problem in self.problems) + 2 if self.problems else len(headers[0]) + 2,
			max(len(problem["title"]) for problem in self.problems) + 2 if self.problems else len(headers[1]) + 2,
			max(len(problem["tag"]) for problem in self.problems) + 2 if self.problems else len(headers[2]) + 2
		]

		# Print headers
		print(f"{headers[0].ljust(col_widths[0])} | {headers[1].ljust(col_widths[1])} | {headers[2].ljust(col_widths[2])}")
		print("-" * (sum(col_widths) + 6))  # Divider line

		# Print each issue in table format
		for problem in self.problems:
			print(f"{problem['id'].ljust(col_widths[0])} | {problem['title'].ljust(col_widths[1])} | {problem['tag'].ljust(col_widths[2])}")


if __name__ == '__main__':
	x = pb()