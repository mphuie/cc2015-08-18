# cc2015-08-18

Written in Flask (python microframework and Flask-Restful)

##Usage

    pip install -r requirements.txt
    
    python app.py
  
##Tests

    nosetests

##Notes

- No datastore, using in-memory array of hash/dict (no PKs)
- Ideally should be logging the users who added the item as well as auditing/logging all operations (possibly via session/cookie)
- Using DELETE HTTP method for taking an item out from inventory as GET method is generally idempotent.  
- With a datastore there would a status column as checked in or out instead of deleting the item. (and in this case, using PUT to update inventory by updating the status.)
- Notifications is an list of users attached to an inventory item.  there is a PUT method to add/remove users to this array.
- Expiration notification (#4) is done through a script which should be run periodically `notifyExpired.py`

##Endpoints

	GET /inventory   		                    # list all inventory items
	POST /inventory 							# add new item
	PUT /inventory/<label>?action=addNotify	    # add notification for user
	PUT /inventory/<label>?removeNotify=mphuie	# remove notification for user
	DELETE /inventory/<label> 					# remove item and notify
	
	GET /notifications                          # list notifications for all users
	GET /notifications/<user>                   # list notifications for specific users


##Sample output

	> curl http://localhost:5000/inventory -X POST -d "expirationDate=2016-01-01&label=TestItem"
	
	{"expirationDate": "2016-01-01", "notifyUsers": [], "label": "TestItem"}
	
	> curl http://localhost:5000/inventory
	
	[{"expirationDate": "2016-01-01", "notifyUsers": [], "label": "TestItem"}]
	
	> curl http://localhost:5000/inventory/TestItem?action=addNotify -X PUT -d "user=testuser"
	
	{"expirationDate": "2016-01-01", "notifyUsers": ["test"], "label": "TestItem"}
	
	> curl http://localhost:5000/notifications/test

	[]
	
	> curl http://localhost:5000/inventory/TestItem -X DELETE
	
	> curl http://localhost:5000/notifications/test
	
	[{"message": "TestItem was removed", "user": "test"}]
