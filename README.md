# Easy Json Database
<p align="center">
    <a href="https://github.com/M4hbod/pyezjson">
        <img src="https://user-images.githubusercontent.com/74229780/172953702-e6df6dce-3b5c-45c3-91fb-8db90505027e.png" alt="pyezjson" width="256">
    </a>
    <br>
    <b>Easier Json Database For Python</b>
    <br>
</p>

# Installation
## Easy Way
```sh
pip install pyezjson
```
## Less Easy Way
```sh
pip install git+https://github.com/M4hbod/pyezjson.git
```

# Usage

## Connect:
```python
from pyezjson import connect

mydb = connect('my_database.json', indent=4)
```
## Add:
```python
mydb.add(False, 'users', 'user_1', first_name='Lee', last_name='Everet')

# `False` is for `update_if_exist` argument

"""
Result in my_database.json:

{
    "users": {
        "user_1": {
            "first_name": "Lee",
            "last_name": "Everet"
        }
    }
}
"""
```
## Update:
```python
mydb.update(False, 'users', 'user_1', 'last_name', SELF='Everett')

# If you use `SELF`, it will update it for the last argument
# You can also use `SELF` in `add` function 
# `False` is for `add_if_not_exist` argument

"""
Result in my_database.json:

{
    "users": {
        "user_1": {
            "first_name": "Lee",
            "last_name": "Everett"
        }
    }
}
"""
```
## Delete:
```python
mydb.delete('users', 'user_1', 'last_name')

"""
Result in my_database.json:

{
    "users": {
        "user_1": {
            "first_name": "Lee"
        }
    }
}
```
## Check:
```python
result_first_name = mydb.check('users', 'user_1', 'first_name')
result_last_name = mydb.check('users', 'user_1', 'last_name')

print(result_first_name)
print(result_last_name)

"""
Result:

>>> True
>>> False
"""
```
## Get:
```python
data = mydb.get('users', 'user_1')
print(data)

"""
Result:

>>> {'first_name': 'Lee'}
"""
```
## Get The Whole Database:
```python
data = mydb.get_all()
print(data)

"""
Result:

>>> {'users': {'user_1': {'first_name': 'Lee'}}}
"""
```
## Reset:
```python
mydb.reset()

"""
Result in my_database.json:

{}
```
