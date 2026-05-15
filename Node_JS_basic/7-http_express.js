const express = require('express');
const fs = require('fs').promises;

async function getStudents(path) {
  try {
    const data = await fs.readFile(path, 'utf8');
    const lines = data.trim().split('\n').filter((line) => line.trim() !== '');
    const students = lines.slice(1);

    const fields = {};

    students.forEach((student) => {
      const [firstname, , , field] = student.split(',');

      if (!fields[field]) {
        fields[field] = [];
      }

      fields[field].push(firstname);
    });

    const output = [`Number of students: ${students.length}`];

    Object.keys(fields).forEach((field) => {
      output.push(
        `Number of students in ${field}: ${fields[field].length}. List: ${fields[field].join(', ')}`,
      );
    });

    return output.join('\n');
  } catch (error) {
    throw new Error('Cannot load the database');
  }
}

const app = express();

app.get('/', (request, response) => {
  response.send('Hello Holberton School!');
});

app.get('/students', async (request, response) => {
  response.set('Content-Type', 'text/plain');

  try {
    const students = await getStudents(process.argv[2]);
    response.send(`This is the list of our students\n${students}`);
  } catch (error) {
    response.send(`This is the list of our students\n${error.message}`);
  }
});

app.listen(1245);

module.exports = app;
