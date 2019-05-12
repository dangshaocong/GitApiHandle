# GitApiHandle
## backgroud
```
The project use  the GitHub V3 restful API to operate GitHub with code to improve efficiency and ease of use.
```
## Language and Platform
- python3.6
- win10
- virtualenv

## steps

#### 1. clone source code

   ``` git clone https://github.com/dangshaocong/GitApiHandle.git```
   
#### 2. in cloned folder GitApiHandle use win cmd-line Tool  execute command:

   ```
      venv\scripts\activate
      pip install -r requirements.txt
   ```
#### 3. then you can create demo.py to Call function of the module GitHandle.py 
- create demo.py in GitApiHandler folder
- write the below codes in demo.py
```
   from GitHandle import Git
   # Initialization object
   
   GitDemo = Git.Git(arg)  # arg is require type string this is your accesstoken of the application in github
   # use function eg 1
   data = GitDemo.get_all_repos() # get all repositoris
   print data
   
   # eg 2 create a repository
   repo = GitDemo.git.create_one_repo(name={rep name}, description={description message})
   print repo
   # and so on ....
 
```
- run the demo.py
```
venv/Scripts/python demo.py

```

## 3.Support the following Important functions
- ```get_repro(username) ==> [get the Specified user repositoris]```
- ```get_flowwer(username) ==> [get the Specified user followers]```
- ```delete_one_repo(owner, repo) ==> [delete the owner repository ]```
- ```create_one_repo(name={rep name}, description={description message}) ==> [create one  repository]```
- ```and so on ......```

## 4.Reference link
- [github v3 api](https://developer.github.com/v3/)
- [git accessToken](https://github.blog/2013-05-16-personal-api-tokens/)



  

   


