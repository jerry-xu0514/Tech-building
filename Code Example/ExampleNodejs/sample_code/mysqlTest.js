const mysql = require('mysql');
const connection = mysql.createConnection({
  host: 'localhost',
  user: 'root',
  password: '',
  database: 'loginSys'
});
connection.connect((err) => {
  if (err) throw err;
  console.log('Connected!');
});

connection.query('SELECT * FROM users', (err,rows) => {
    if(err) throw err;

    console.log('Data received from Db:');
    console.log(rows);
});