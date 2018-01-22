## Library versions used
– Python 3.4.3  
– Django 2.0.1  
– Bootstrap v4.0.0  
– jQuery 3.2.1  


### Functionality
A really simple `TodoItem` model is served by 5 views / urls: `tasks`, `item`, `solve`, `save` and `remove`.  Another view passes the `index` / main template.   All views / urls except `index` is handled via AJAX by `static/todo.js`. 

<br>
   
#### A list of tasks:  
![basic](README-images/ss1.png)  
   
#### Tasks can be expanded to view details:  
![details](README-images/ss2.png)  

#### A task that is not marked as solved can be edited or removed (besides being marked as solved):  
![edit](README-images/ss3.png)  
   
#### A solved task get a distinct red colored title. It can no longer be edited but still be removed:   
![edit](README-images/ss4.png)  
