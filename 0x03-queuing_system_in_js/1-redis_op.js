import { createClient } from 'redis';

const client = createClient({
  host: '127.0.0.1',
  port: 6379,
});
  
client.on('error', err => console.log('Redis client not connected to the server:', err));
client.on('connect', () => console.log('Redis client connected to the server'));

function setNewSchool(schoolName, value) {
  client.set(schoolName, value, (err, reply) => {
    if (err) {
      console.log("Error setting value", err);
    } else {
      console.log('Reply:', reply);
    }
  });
}

function displaySchoolValue(schoolName) {
  client.get(schoolName, (err, reply) => {
    if (err) {
      console.log("error getting key:", err);
    } else {
      console.log(reply);
    }
  });
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
