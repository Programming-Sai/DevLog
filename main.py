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
		self.subparsers = self.add_subparsers(dest="command", required=False, parser_class=ArgumentParser)
		self.problems = self.load_issues()
		# print(self.problems)
		self.add_arguments()
		self.process_args()


	def add_arguments(self):
		self.add_argument('--init', action='store_true', help="Initialises the tracker.")
		
		self.add_argument('--id', type=str, help='id')
		self.add_argument('--title', type=str, help='title')
		self.add_argument('--tag', type=str, help='tag')
		self.add_argument('--language', type=str, help='language')
		self.add_argument('--desc', type=str, help='desc')
		self.add_argument('--snippet', type=str, help='snippet')
		self.add_argument('--solution-desc', type=str, help='solution-desc')
		self.add_argument('--solution-snippet', type=str, help='solution-snippet')
		self.add_argument('--time-taken', type=str, help='time-taken-to-solution')
	
	
	
		self.add_argument('--compile', action='store_true', help='compile-to-solution')

	

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
				


if __name__ == '__main__':
	x = pb()