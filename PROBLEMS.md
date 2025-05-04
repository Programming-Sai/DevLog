# Problem Tracker<br><br>
## 📋 Table of Contents<br>
- [Test Problem](#🆔-011---test-problem)

- [Sync vs Async Django views](#🆔-010---sync-vs-async-django-views)

- [Incorrect JSON Parsing in Python](#🆔-issue-005---incorrect-json-parsing-in-python)

- [Permission Denied Error in Bash](#🆔-issue-004---permission-denied-error-in-bash)

- [Bash Script Fails with 'Command Not Found'](#🆔-issue-003---bash-script-fails-with-command-not-found)

- [Undefined Variable in JavaScript](#🆔-issue-002---undefined-variable-in-javascript)

- [SyntaxError in Python Script](#🆔-issue-001---syntaxerror-in-python-script)

---

---
### 🆔 011 - Test Problem
<br>**Status:** ✅ Solved

**Language:** Python

**Time Taken:** 40m

### 🐞 Problem Description<br>
async def views with ratelimit caused unawaited coroutine under WSGI, Django expected sync views.

```python
async def search_view(request):\n    result = await engine.regular_search(...)
```
				
### ✅ Solution Description
<br>
Changed to regular def views and wrapped async calls with async_to_sync().

```python
def search_view(request):\n    result = async_to_sync(engine.regular_search)(query)\n    return JsonResponse(...)
```
				
<br>
<br>

---
### 🆔 010 - Sync vs Async Django views
<br>**Status:** ✅ Solved

**Language:** Python

**Time Taken:** 40m

### 🐞 Problem Description<br>
async def views with ratelimit caused unawaited coroutine under WSGI, Django expected sync views.

```python
async def search_view(request):\n    result = await engine.regular_search(...)
```
				
### ✅ Solution Description
<br>
Changed to regular def views and wrapped async calls with async_to_sync().

```python
def search_view(request):\n    result = async_to_sync(engine.regular_search)(query)\n    return JsonResponse(...)
```
				
<br>
<br>

---
### 🆔 issue-005 - Incorrect JSON Parsing in Python
<br>**Status:** ✅ Solved

**Language:** Python

**Time Taken:** 10 minutes

### 🐞 Problem Description<br>
The JSON parser fails when reading a file with single quotes instead of double quotes.

```python
import json
json.loads("{'key': 'value'}")
```
				
### ✅ Solution Description
<br>
Replaced single quotes with double quotes in JSON string.

```python
json.loads('{"key": "value"}')
```
				
<br>
<br>

---
### 🆔 issue-004 - Permission Denied Error in Bash
<br>**Status:** ✅ Solved

**Language:** Bash

**Time Taken:** 5 minutes

### 🐞 Problem Description<br>
Script execution fails with 'Permission denied'. The script lacks execution permissions.

```bash
./myscript.sh
```
				
### ✅ Solution Description
<br>
Resolved by making the script executable using chmod.

```bash
chmod +x myscript.sh
```
				
<br>
<br>

---
### 🆔 issue-003 - Bash Script Fails with 'Command Not Found'
<br>**Status:** ⏳ Pending

**Language:** Bash

**Time Taken:** 

### 🐞 Problem Description<br>
A command inside the script isn't recognized. It could be due to a missing package or incorrect path.

```bash
mycommand --option
```
				
<br>
<br>

---
### 🆔 issue-002 - Undefined Variable in JavaScript
<br>**Status:** 🚫 Ignored

**Language:** Js

**Time Taken:** 

### 🐞 Problem Description<br>
ReferenceError: 'myVar' is not defined. Occurs when trying to use 'myVar' before declaration.

```js
console.log(myVar);
```
				
<br>
<br>

---
### 🆔 issue-001 - SyntaxError in Python Script
<br>**Status:** ⏳ Pending

**Language:** Python

**Time Taken:** 

### 🐞 Problem Description<br>
Running the script results in a SyntaxError due to a missing colon in an if-statement.

```python
if x == 10
    print('X is 10')
```
				
<br>
<br>
