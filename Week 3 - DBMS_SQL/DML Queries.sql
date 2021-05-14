
#Table_creation
CREATE TABLE barani(
Rollno int,
Name varchar(25),
Test varchar(25));

#insert_value_to_Table
insert into barani
values('12','barani','ten');


#insert_value_to_Table
insert into barani(Rollno,Name,Test)
values ('13','hari','eleven');

#insert_value_to_Table_with_value_in_Rollno_only
insert into barani(Rollno)
values ('15');

#updating_the_Column_value_Hari_with_the_Colomn_value_Test_as_B.E
update barani
set Test='B.E'
where Name='hari';

#Deleting the row with name as hari
delete
from barani
where Name='hari';

#adding the extra column company with datatype
alter table barani
add Company varchar(25);

#updating the company name as Expleo to all the rows
update barani
set Company='Expleo';

select * from barani;
