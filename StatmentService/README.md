# Statement Store as Service
  Storing User statements into database. This statements can be use as blog posts,tweet or any string.
 
# MongoDB
  MongoDB stores data in flexible, JSON-like documents, meaning fields can vary from document to document and data structure can be changed over time.MongoDB is free and open-source, published under the GNU Affero General Public License. To install mongodb to your system please follow this page: https://docs.mongodb.com/manual/installation/

# Flask
  Flask is a microframework for Python based on Werkzeug, Jinja 2 and good intentions. And before you ask: It's BSD licensed!!.

# Statement Storing
Easy app for storing statements on your blog posts. User need to register them selves by creating unique user name 
and password (`TODO: check password strength`). Duplicates username are not allowed. 


# Implemented REST API

| RESTAPI       | ENDPOINT    | METHOD | EXAMPLE DATA |
| ------------- | ----------- | ------ |    ------    |
| Register      | "/register" | POST   | `{"Username":"user1","Password":"test123"}` |
| Storage       | "/store"    | POST   | `{"Username":"user1","Password":"test123", "Statement":"Hello this is my blog"}` |
| GetStatement  | "/statement"| GET    | |


# Docker Infra
This project is deployed via docker. to deploy just checkout repo with following command
`sudo docker-compose build`
`sudo docker-compose up`
