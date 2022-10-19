### db_index

####  

I would say you should use db_index=True when you have a field that is unique for faster lookups.

For example, if you a table customers with many records of users they'll each have their own unique user_id. When you
create an index, a pointer is created to where that data is stored within your database so that the next look up against
that column will give you a much more desirable time of query than say using their first_name or last_name.