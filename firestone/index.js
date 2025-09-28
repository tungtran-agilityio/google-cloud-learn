const {Firestore} = require('@google-cloud/firestore');

// Create a new client with project and database configuration
const firestore = new Firestore({
  projectId: 'learn-cloud-473302',
  databaseId: 'testdb'
});

async function quickstart() {
  try {
    // Obtain a document reference.
    const document = firestore.doc('users/user1');

    // Enter new data into the document.
    await document.set({
      title: 'Welcome to Firestore',
      body: 'Hello World',
    });
    console.log('Entered new data into the document');

    // Update an existing document.
    await document.update({
      body: 'My first Firestore app',
    });
    console.log('Updated an existing document');

    // Read the document.
    const doc = await document.get();
    console.log('Read the document');
    console.log('Document data:', doc.data());

    // Delete the document.
    // await document.delete();
    console.log('Deleted the document');
  } catch (error) {
    console.error('Error:', error);
  }
}
quickstart();