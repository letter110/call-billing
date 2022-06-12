# call-billing
**program that charges a user to pay** 
## 1. Description
### database.db: 
column:
- `use_name` : feature of user
- `call_duration`: an integer describing the call time in milliseconds
### main.py:
- contains the program's api
### test.api:
- test api from `main.py`
### dockerfile
- create docker image
### requirement.txt
- libraries to install and run in dockerfile
### controllDB:
- delete data in database if need

### 2. Clone repository
First of all, you need to download the repository. You can either run the script below on the command-line or terminal:

`git clone https://github.com/letter110/call-billing.git`
## 3. Change directory
Change the `path` that points to your call-billing folder.

```
cd path/to/call-billing
```
## 4. Run API
first:
```
python main.py
```
then:
```
python test.py
```
