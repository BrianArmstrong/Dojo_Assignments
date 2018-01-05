var students = {};
students = [
	{first_name: 'Michael' , last_name: 'Jordan'},
	{first_name: 'John', last_name: 'Rosales'},
	{first_name: 'Mark', last_name: 'Tonel'}
	{first_name: 'KB', last_name: 'Tonel'}
];

function stu(){
	for(var i=0; i<students.length; i++){
		console.log(students[i].first_name, students[i].last_name)
	}
}
stu();

