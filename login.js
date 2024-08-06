const mysql = require('mysql2');

// Create a connection to the database
const connection = mysql.createConnection({
  host: 'localhost',
  user: 'root',
  password: 'mysql',
  database: 'MeltasticDB'
});

// Check login credentials
const checkLogin = (username, password) => {
  return new Promise((resolve, reject) => {
    connection.query(
      'SELECT * FROM Account WHERE name = ? AND password = ?',
      [username, password],
      (error, results) => {
        if (error) {
          return reject(error);
        }
        resolve(results);
      }
    );
  });
};

// Usage example
const username = 'example_user';
const password = 'example_password';

checkLogin(username, password)
  .then(results => {
    if (results.length > 0) {
      console.log('Login successful');
    } else {
      console.log('Invalid username or password');
    }
  })
  .catch(error => {
    console.error('Error during login:', error);
  });
