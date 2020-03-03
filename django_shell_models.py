Create new record/instance: ClassName.objects.create(......)
In [3]: Users.objects.create(first_name='Darrick', last_name='Truong', email_addre
   ...: ss='truong.darrick@gmail.com', age='33')                                  
Out[3]: <Wizard object: Darrick Truong truong.darrick@gmail.com 33 (1)>

In [6]: new_user = Users.objects.create(first_name='Shaquille', last_name="O'Neal"
   ...: , email_address='shaq.diesel@gmail.com', age = '45')                      

In [7]: new_user.save()    


Get/Retrieve ALL rows from a table. ClassName.objects.all()
In [8]: Users.objects.all()                                                       
Out[8]: <QuerySet [<Wizard object: Darrick Truong truong.darrick@gmail.com 33 (1)>, 
<Wizard object: Kobe Bryant kobe.bryant@gmail.com 40 (2)>, <Wizard object: Kevin Garnett 
kevin.garnet@gmail.com 45 (3)>, <Wizard object: Shaquille O'Neal shaq.diesel@gmail.com 45 (4)>]>


Get/Retrieve First/Last rows from a table. ClassName.objects.first/last()
In [9]: Users.objects.last()                                                      
Out[9]: <Wizard object: Shaquille O'Neal shaq.diesel@gmail.com 45 (4)>

In [10]: Users.objects.first()                                                    
Out[10]: <Wizard object: Darrick Truong truong.darrick@gmail.com 33 (1)>


Updating an existing record. ClassName.objects.get(id) > c.field_name = 'new value" > c.save()
In [13]: id3 = Users.objects.get(id='3')                                          
In [14]: id3.last_name = 'Pancakes'                                               
In [15]: id3.save()                                                               
In [16]: Users.objects.get(id='3')                                                
Out[16]: <Wizard object: Kevin Pancakes kevin.garnet@gmail.com 45 (3)>


Deleting an existing record > variable = ClassName.objects.get(id=1) > variable.delete()
In [17]: id2 = Users.objects.get(id='2')                                          
In [18]: id2.delete()                                                             
Out[18]: (1, {'ORM.Users': 1})


Ordering records
ClassName.objects.all().order_by("field_name") - orders by field provided, ascending
In [19]: Users.objects.all().order_by('first_name')                               
Out[19]: <QuerySet [<Wizard object: Darrick Truong truong.darrick@gmail.com 33 (1)>, <Wizard object: Kevin Pancakes 
kevin.garnet@gmail.com 45 (3)>, <Wizard object: Shaquille O'Neal shaq.diesel@gmail.com 45 (4)>]>

ClassName.objects.all().order_by("-field_name") - orders by field provided, descending
In [20]: Users.objects.all().order_by('-first_name')                              
Out[20]: <QuerySet [<Wizard object: Shaquille O'Neal shaq.diesel@gmail.com 45 (4)>, <Wizard object: Kevin Pancakes 
kevin.garnet@gmail.com 45 (3)>, <Wizard object: Darrick Truong truong.darrick@gmail.com 33 (1)>]>