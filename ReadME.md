# Final - Project - QA & Automation Testing


STD - https://github.com/DayanShay/Final_Project/blob/main/STD%20%E2%80%93%20BookStore%20%E2%80%93%20Final%20Project.pdf


At this Project You can find.

Pytest Project with Selenium & PlayWright

Must install requirements needed

USE !

```commandline
pip install -r "FullPath\Final_Project\requirements.txt"
```

Edit Configuration for tests :

![image](https://user-images.githubusercontent.com/108628136/191582056-0d55d543-a373-44a2-bd1e-a8bcc7bd311a.png)

For Remote : Run before Executing the tests

Needed - Selenium Grid

Can see here :

https://www.selenium.dev/documentation/grid/getting_started/


Run with CMD - Make sure to be at Root Library of the Project

```commandline
docker-compose -f selenium_grid.yml up
```


Add the `-d` flag at the end for detached execution

```commandline
docker-compose -f selenium_grid.yml up -d
```

To Stop it from Runing : 

```commandline
docker-compose -f selenium_grid.yml down
```


To run the BookStore - 


```commandline
docker-compose -f BookStorev1.yaml up
```


Add the `-d` flag at the end for detached execution

```commandline
docker-compose -f BookStorev1.yaml up -d
```

To Stop it from Runing : 

```commandline
docker-compose -f BookStorev1.yaml down
```

Website Can Be Found :

```URL
http://localhost/
```
RestAPI can be found : 

```URL
http://localhost:7017/swagger/index.html
```


How To run the tests : 


```commandline
pytest --options "args"  .\tests_book_store\  
```
--url = Website URL .
--api_url = RestApi Url .
--remote_url = Selenium Grid - Do not Touch .
--remote = false or True, Works only with Selenium.
--sys_use = "selenium" or "playwright".
--browse = "Chrome" or "Firefox" Supports only this for now.

Or 

Edit default Configuration:

File = ".Final_Project\test_configuration.json"
```json
{
  "url": "http://localhost/",
  "api_url": "http://localhost:7017/",
  "remote_url":"http://127.0.0.1:4444/wd/hub",
  "remote": false, 
  "sys_use": "playwright",
  "browse": "Firefox"
}
```


To run with allure report : 

Allure will take a Pic if a Test is Faild. 


```commandline
pytest --alluredir=reports\ tests_book_store\
```

After Tests Finish :

```commandline
allure serve .\reports\
```




Thanks For Reading That far , Hope you will enjoy! 
