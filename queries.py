createTable_Application_Data = '''
if (exists (select * from INFORMATION_SCHEMA.TABLES where TABLE_SCHEMA = 'dbo' and TABLE_NAME = 'Application_Data'))
	 begin
		print 'table exists'
	 end
else
	begin
		print 'creating table Application_Data';
		use JobAppDB
		create table Application_Data(
			APP_ID int identity(1000,1) primary key not null,
			FirstName varchar(40) not null,
			LastName varchar(40) not null,
            DateOfBirth varchar(40),
			Email varchar(80) not null,
			Phone varchar(40) not null,
			CurrentPosition varchar(100),
			SalaryExpectation int,
			YrsExperience int,
			Degree Varchar(100),
			DateOfSubmission date,
			FileName varchar(100)
		)
	end;
'''

insert_into_Application_Data = '''
insert into Application_Data
values(?,?,?,?,?,?,?,?,?,?,?)
'''