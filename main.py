from argparse import *
import json


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
  --init             Initialize a new issue tracker.
  --id <id>          Specify an issue ID (used with other options).
  --title <title>    Set the title of an issue.
  --tag <status>     Set issue status (solved | pending | ignored).
  --language <lang>  Specify the programming language related to the issue.
  --desc <text>      Add a description of the issue.
  --snippet <code>   Include a code snippet demonstrating the issue.
  --solution-desc    Provide a description of the solution.
  --solution-snippet Include a code snippet of the solution.
  --time-taken       Log the time taken to solve the issue.
  --delete <id>      Delete an issue by ID.
  --list             Display all tracked issues with IDs and titles.
  --compile          Generate a Markdown report of all issues.
  --clear              Permanently delete all stored issues (Irreversible!).


Examples:
  devlog --init
  devlog --id 101 --title "Fix login bug" --desc "Login fails on mobile"
  devlog --id 101 --tag solved --solution-desc "Fixed API endpoint"
  devlog --list
  devlog --delete 101
  devlog --clear
  devlog --compile

Tip: Start by running 'devlog --init' to create your tracker.

🚀 Happy Coding!
"""

		self.subparsers = self.add_subparsers(dest="command", required=False, parser_class=ArgumentParser)
		self.problems = self.load_issues()
		self.add_arguments()
		self.process_args()


	def add_arguments(self):
		self.add_argument('--init', action='store_true', help="Initialize a new issue tracker.")

		self.add_argument('--id', type=str, help="Unique identifier for the issue.")
		self.add_argument('--title', type=str, help="Title of the issue.")
		self.add_argument('--tag', type=str, help="Status of the issue (solved | pending | ignored).")
		self.add_argument('--language', type=str, help="Programming language related to the issue.")
		self.add_argument('--desc', type=str, help="Detailed description of the issue.")
		self.add_argument('--snippet', type=str, help="Code snippet demonstrating the issue.")
		self.add_argument('--solution-desc', type=str, help="Explanation of the solution.")
		self.add_argument('--solution-snippet', type=str, help="Code snippet for the solution.")
		self.add_argument('--time-taken', type=str, help="Time taken to find the solution.")

		self.add_argument('--compile', action='store_true', help="Generate a detailed Markdown report of all logged issues, including descriptions, code snippets, and solutions.")

		self.add_argument('--delete', type=str, help="Delete a specific issue from the tracker by providing its unique ID.")

		self.add_argument('--clear', action='store_true', help="Permanently remove all stored issues from the tracker. Use with caution!")

		self.add_argument('--list', action='store_true', help="Display a summary of all tracked issues, showing their IDs, titles, and status.")



	

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
			self.create_md()
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

	def create_md(self):
		lines = ["# Problem Tracker\n\n## Table of Contents\n"]
    
		# Add table of contents
		for problem in self.problems:
			lines.append(f"- [{problem['title']}](#{problem['id']})\n")
		
		lines.append('\n---\n---\n---\n---\n')

		for problem in self.problems:
				lines.append('\n---\n')
				lines.append(f'#### {problem['id']}\n')
				lines.append(f'`{problem['tag']}`\n')
				lines.append(f'## {problem['title']}\n')
				lines.append(f'{problem['desc']}\n')
				lines.append(f'''
```{problem['language']}
{problem['snippet']}
```
				''' if problem['snippet'] else '')
				lines.append('\n<br><br>\n')
				lines.append(f'{problem['solution-desc']}\n')
				lines.append(f'''
```{problem['language']}
{problem['solution-snippet']}
```
				''' if problem['solution-snippet'] else '')
				lines.append(f"\n{problem['time-taken']}\n")
				lines.append('\n---\n')
			
		with open(self.result_file, 'w') as m:
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