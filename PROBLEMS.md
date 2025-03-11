# Problem Tracker

## Table of Contents
- [SyntaxError in Python Script](#issue-001)
- [Undefined Variable in JavaScript](#issue-002)
- [Bash Script Fails with 'Command Not Found'](#issue-003)
- [Permission Denied Error in Bash](#issue-004)
- [Incorrect JSON Parsing in Python](#issue-005)

---
---
---
---

---
#### issue-001
`pending`
## SyntaxError in Python Script
Running the script results in a SyntaxError due to a missing colon in an if-statement.

```python
if x == 10
    print('X is 10')
```
				
<br><br>




---

---
#### issue-002
`ignored`
## Undefined Variable in JavaScript
ReferenceError: 'myVar' is not defined. Occurs when trying to use 'myVar' before declaration.

```js
console.log(myVar);
```
				
<br><br>




---

---
#### issue-003
`pending`
## Bash Script Fails with 'Command Not Found'
A command inside the script isn't recognized. It could be due to a missing package or incorrect path.

```bash
mycommand --option
```
				
<br><br>




---

---
#### issue-004
`solved`
## Permission Denied Error in Bash
Script execution fails with 'Permission denied'. The script lacks execution permissions.

```bash
./myscript.sh
```
				
<br><br>
Resolved by making the script executable using chmod.

```bash
chmod +x myscript.sh
```
				
5 minutes

---

---
#### issue-005
`solved`
## Incorrect JSON Parsing in Python
The JSON parser fails when reading a file with single quotes instead of double quotes.

```python
import json
json.loads("{'key': 'value'}")
```
				
<br><br>
Replaced single quotes with double quotes in JSON string.

```python
json.loads('{"key": "value"}')
```
				
10 minutes

---
