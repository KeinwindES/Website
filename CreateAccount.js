// Require the mysql2 package
const mysql = require('mysql2');

// Create a connection to the database
const connection = mysql.createConnection({
  host: 'localhost',
  user: 'root',
  password: 'mysql',
  database: 'MainDB'
});

// Connect to the database
connection.connect((err) => {
  if (err) {
    console.error('Error connecting to database: ' + err.stack);
    return;
  }
  console.log('Connected to database with ID: ' + connection.threadId);
});

// Create the Account table
connection.query(`
  CREATE TABLE IF NOT EXISTS Account (
    IDAccount INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL
  )
`, (err, results) => {
  if (err) {
    console.error('Error creating table: ' + err.message);
  } else {
    console.log('Account table created successfully');
  }
});

// Close the connection
connection.end();