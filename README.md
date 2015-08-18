# cc2015-08-18

Usage

    pip install -r requirements.txt
    
    python app.py
  
Tests

    nosetests



#Endpoints

	GET /inventory   		                    # list all inventory items
	POST /inventory 							# add new item
	PUT /inventory/<label>?action=addNotify	    # add notification for user
	PUT /inventory/<label>?removeNotify=mphuie	# remove notification for user
	DELETE /inventory/<label> 					# remove item and notify
	
	GET /notifications                          # list notifications for all users
	GET /notifications/<user>                   # list notifications for specific users
