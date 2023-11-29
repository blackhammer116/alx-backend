import { createClient } from 'redis';
import { promisify } from 'util';

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

const getAsync = promisify(client.get).bind(client);

async function displaySchoolValue(schoolName) {
  try {
    const value = await getAsync(schoolName);
    console.log(value);
  } catch (error) {
    console.log(error);
  }
}

client.hset('HolbertonSchools', 'Portland', '50', (err, reply) => {
  if (err) {
    console.log(err);
  } else {
    console.log('Reply:', reply);
  }
});

client.hset('HolbertonSchools', 'Seattle', '80', (err, reply) => {
  if (err) {
    console.log(err);
  } else {
    console.log('Reply:', reply);
  }
});
client.hset('HolbertonSchools', 'New York', '20', (err, reply) => {
  if (err) {
    console.log(err);
  } else {
    console.log('Reply:', reply);
  }
});
client.hset('HolbertonSchools', 'Bogota', '20', (err, reply) => {
  if (err) {
    console.log(err);
  } else {
    console.log('Reply:', reply);
  }
});
client.hset('HolbertonSchools', 'Cali', '40', (err, reply) => {
  if (err) {
    console.log(err);
  } else {
    console.log('Reply:', reply);
  }
});
client.hset('HolbertonSchools', 'Paris', '2', (err, reply) => {
  if (err) {
    console.log(err);
  } else {
    console.log('Reply:', reply);
  }
});

client.hgetall('HolbertonSchools', (err, reply) => {
  if (err) {
    console.log(err);
  } else {
    console.log(reply);
  }
});
