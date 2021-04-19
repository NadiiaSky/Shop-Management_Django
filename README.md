# Shop-Management_Django
Django project with admin panel for editing data.

There are three entities - Shop, Product, and Category. The Product table has two foreign keys from other tables - shop title and category name.
The Product has an one_to_many relationship with the Shop table and has a many_to_many relationship with the Category table.

Also, two superuser exist in the model - shopAdmin and productAdmin.
shopAdmin can add, edit and delete the data of Shops, and search records by shop title.
productAdmin can add, edit and delete the data of Products, and can search records by product title. Creating the new record product entity has descriptions
about the category of product and shop tіtle, which can be chosen from Shop and Product entities.
