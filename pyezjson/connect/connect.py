import contextlib
import json

class Connect:
    def __init__(self, db_name = 'database.json', indent = None):
        """Connect to a json database.

        Args:
            db_name (str, optional): Database Name. Defaults to 'database.json'.
            indent (int, optional): Json File Indentation. Defaults to None.
        """
        try:
            self.data = json.load(open(db_name , 'rb'))
            self.db = db_name
        except FileNotFoundError:
            open(db_name , '+wt').write('{}')
            self.data = json.load(open(db_name , 'rb'))
            self.db = db_name
        self.indent = indent
        
    def commit(self):
        with open(self.db , 'w') as file:
            json.dump(self.data , file , indent=self.indent)
        self.data = json.load(open(self.db , 'rb'))
        
    def add_handler(self, *attribute, **values):
        """Handler for add and update functions."""
        to_execute = 'self.data'
        for i in attribute:
            to_execute = f'{to_execute}["{i}"]'
            try:
                exec(to_execute + '.update({})')
            except:
                exec(to_execute + '={}')
        if 'SELF' in str(values):
            values = '"'+values['SELF']+'"'
        to_execute = f'{to_execute}={str(values)}'
        with contextlib.suppress(Exception):
            exec(to_execute)
            self.commit()
        
    def add(self, update_if_exist = False, *attribute, **values):
        """Add key/value pair to the database.

        Args:
            update_if_exist (bool, optional): Update if key already exists. Defaults to False.
            *attribute (str): Attributes to add.
            **value (any): Values to add.
        """
        data = self.data
        if update_if_exist == True:
            self.add_handler(*attribute, **values)
        else:
            try:
                for i in attribute:
                    data = data[i]
            except KeyError:
                self.add_handler(*attribute, **values)
    
    def update(self, add_if_not_exist = False, *attribute, **value):
        """Update key/value pair in the database.

        Args:
            add_if_not_exist (bool, optional): Add if key does not exist. Defaults to False.
            *attribute (str): Attributes to update.
            **value (any): Values to update.
        """
        data = self.data
        if add_if_not_exist != True:
            try:
                for i in attribute:
                    data = data[i]
            except KeyError:
                return
        self.add_handler(*attribute, **value)

    def delete(self, *attribute):
        """Delete value from the database.
        
        Args:
        **attribute (str): Keys to delete.
        """
        to_execute = 'self.data'
        for i in attribute[:-1]:
            to_execute = f'{to_execute}["{i}"]'
        to_execute = f'{to_execute}.pop("{attribute[-1]}")'
        exec(to_execute)
        self.commit()

    def check(self, *attribute):
        """Check If Attribute Exists
        
        Args:
            *attribute (str): Attributes to check.
        """
        data = self.data
        try:
            for i in attribute:
                data = data[i]
            return True
        except KeyError:
            return False

            
    def get(self, *attribute):
        """Get Value Using Attribute
 
        Args:
            *attribute (str): Attributes to get data from.

        Returns:
            (any): value
        """
        data = self.data
        try:
            for i in attribute:
                data = data[i]
        except KeyError:
            return None
        return data
    
    def get_all(self):
        """Return All Data In The Database

        Returns:
            (dict): Full Database
        """
        return self.data
    
    def reset(self):
        """Reset the database."""
        with open(self.db,'w') as f:
            f.truncate(0)
            f.write("{}")