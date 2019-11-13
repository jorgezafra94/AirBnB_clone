![](https://holbertonintranet.s3.amazonaws.com/uploads/medias/2018/6/65f4a1dd9c51265f49d0.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUXW7JF5MT%2F20191112%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20191112T225437Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=ec34fc29f3a2ec4e194de9ba80cb5132e3d464d9e6b88bd252231eb45a515206)

# README CLONE ARBNB
## Description 
In this project we create the first part of the clone of Arbnb, which one is about to create a console in order to get different commands because we are going to have Objects in our platform as Places, Cities, States, Amenities, Users, and Review based in a parent class called BaseModel. And we have to manage it so that have a interactive web application, that is why we have to create, update, show, count, destroy and print the differents instances that are in our platform.
## How to use it
- **excecution or Start**: 
  for excecute the console type:
  `./console.py`
- **help command**:
  help command helps you to understand each one of the commands that we create
  if you want to know what are all the possible commands you have to type:
  `help`
  but if you want to know what is an specific command you have to type:
  `help command` like `help quit`
- **create command**:
   if you want to create a new object you have to type:
    `create <object class>`
     so the classes that we manage are:
      1. BaseModel
       2. User
        3. Amenity
	 4. City
	  5. Place
	   6. State
	    7. Review
	     so you have to take care of the capital letters when you call the class.
	      once the object was created it will return the its id number
- **all command**:
   with this command you will be able to print all the created objects that exists
    nowadays, if you want to do that you have to type:
     `all` or `.all()`
      but if you want to print all the objects of a specific class you have to type:
       `all <class name>` like `all User` or the second way `<class name>.all()` like `City.all()`
- **count command**:
  with count you can print the number of objects that belong to a specific class
  so if you want to do it you have to type:
  `count <class name>` like `count Place` or the second way `<class name>.count()` like `Review.count()`
- ** show command**:
  This command prints the string representation of a specific objects. To see the information type:
  `show <class name> <id>` ex: `show Review 12345`or the second way `<class name>.show("id")` like `Review.show("12345")`.
- ** destroy command**:
  This command deletes a specific objects. To remove the object type:
  `destroy <class name> <id>` ex: `destroy Review 12345`or the second way `<class name>.destroy("id")` like `Review.destroy("12345")`.
- ** update command**:
  This command updates a specific objects. To update the object type one of these three way to do it:
  1. `update <class name> <id> <name> "<value>"` ex: `update Review 12345 name "Marco"`
  2. `<class name>.update("id", "<name>", "<value>")` ex: `City.update("12345", "item", "bed")`
  3.  `<class name>.update("id", {'<name1>: "<value1>", '<name2>': "<value2>"})` ex `City.update("12345", {'item1': "bed", 'item2': "bathroom"})`
   if the attribute of the class exists it will be replace with the new value, otherwise it will create a new attribute for the specified instance.
- **commands to exit the program**
   if you want to exit the program you should type:
    `quit` or `Ctrl+D` or `EOF`