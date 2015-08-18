# cc2015-08-18

##Usage

    pip install -r requirements.txt
    
    python app.py
  
##Tests

    nosetests

##notes

- no datastore, using array of hash/dict (no PKs)
- using DELETE HTTP method for taking an item out from inventory as GET method is generally idempotent
- notifications is an list of users attached to an inventory item.  there is a PUT method to add/remove users to this array.
- expiration notification is done through a script which should be run periodically `notifyExpired.py`

##Endpoints

	GET /inventory   		                    # list all inventory items
	POST /inventory 							# add new item
	PUT /inventory/<label>?action=addNotify	    # add notification for user
	PUT /inventory/<label>?removeNotify=mphuie	# remove notification for user
	DELETE /inventory/<label> 					# remove item and notify
	
	GET /notifications                          # list notifications for all users
	GET /notifications/<user>                   # list notifications for specific users
