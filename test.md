# Problem Tracker\n\n ## Table of Contents

- [Feature login bug](#fix-login-bug)

---

---

---

---

#### 001

`solved`

## Fix login bug

Login fails on mobile devices due to incorrect API endpoint handling.

```python
# Sample code illustrating the issue
response = requests.post(url, data=payload)
```

Updated the API endpoint to handle mobile-specific headers correctly.

```python
headers = {'User-Agent': 'Mobile'}
response = requests.post(url, data=payload, headers=headers)
```

2

---

---

---

<hr>

# 🛠️ Problem Tracker

## 📋 Table of Contents

- [Fix login bug](#🆔-001---fix-login-bug)

---

### 🆔 001 - Fix login bug

**Status:** ✅ Solved  
**Language:** Python  
**Time Taken:** 2 hours

---

### 🐞 Problem Description

Login fails on mobile devices due to incorrect API endpoint handling.

```python
# Sample code illustrating the issue
response = requests.post(url, data=payload)
```

### ✅ Solution

Updated the API endpoint to handle mobile-specific headers correctly.

```python
headers = {'User-Agent': 'Mobile'}
response = requests.post(url, data=payload, headers=headers)
```

---
