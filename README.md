# REST API # 

Website content so far: 
* Comprised of two models, Album and Song related by one-many relation between each other. 
* Views are built to do the following: 
  * View entire website album inventory on the home page
  * View details of each album on the album's detail page e.g Album title
  * CRUD operations on album objects using class based Model forms i.e CreateView, DeleteView, Update View

* HTML template inheritance hiearchary: Base HTML -> Homepage HTML (All albums)
                                        Base HTML -> Album details HTML (Album details)
