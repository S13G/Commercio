### db_index

####  

I would say you should use db_index=True when you have a field that is unique for faster lookups.

For example, if you a table customers with many records of users they'll each have their own unique user_id. When you
create an index, a pointer is created to where that data is stored within your database so that the next look up against
that column will give you a much more desirable time of query than say using their first_name or last_name.

### index_together

#### In the Meta class of the Product model, you use the index_together meta option
to specify an index for the id and slug fields together. You define this index because
you plan to query products by both id and slug. Both fields are indexed together
to improve performance for queries that utilize the two fields.

