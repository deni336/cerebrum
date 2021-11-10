const fs = require('fs');
const inventory = require('./data/inventory.json');
const express = require('express');
const readline = require('readline');
const { google } = require('googleapis');

const app = express();

app.set('view engine', 'ejs');

app.use(express.urlencoded({ extended: true }));

app.get('/', async(req, res) => {
    res.render('index');
});

app.get('/jobs', async(req, res) => {

    /* Google API authenticate sheets*/
    const auth = new google.auth.GoogleAuth({
        keyFile: 'credentials.json',
        scopes: 'https://www.googleapis.com/auth/spreadsheets.readonly',
    });

    const client = await auth.getClient();

    const googleSheets = google.sheets({ version: 'v4', auth: client });

    const spreadsheetId = '11fge5RcQuAg2MVF2AxQ8FB4EVKFIFI__90Ff2daSHuM';

    const metaData = await googleSheets.spreadsheets.get({
        auth,
        spreadsheetId
    });

    // Gets the entire data sheet
    const getRows = await googleSheets.spreadsheets.values.get({
        auth,
        spreadsheetId,
        range: 'Sheet1',
    });
    //viperoutservice@viperout.iam.gserviceaccount.com

    /*DATA VARIABLES FOR TABLE*/
    let fullList = [];
    let table_heads = [];
    let table_data = [];
    let customerList = [];

    fullList = getRows.data.values;

    fullList.forEach(element => {
        if (element[0] === 'For DATA- DO NOT DELETE' || element[0] === '') {
            delete fullList[element];
        } else {
            table_data.push(element);
        }
    });
    table_data.shift();

    //res.send(getRows.data.values);
    table_heads = fullList[0];
    console.log(table_heads);


    for (let i = 0; i < table_data.length; i++) {
        customerList.push(table_data[i][0]);
    }
    console.log(customerList);

    console.log(table_data.length);
    res.render('index', { table_heads, table_data });

});

app.get('/Inventory', async(req, res) => {
    let inventoryList = JSON.parse(JSON.stringify(inventory));
    let cameraList = inventoryList.cameras;
    let workers = inventoryList.workers;

    class Camera {
        constructor(id, model, serial, status, checkoutDate, checkinDate, location, who_has, password) {
            this.id = id;
            this.model = model;
            this.serial = serial;
            this.status = status;
            this.checkoutDate = checkoutDate;
            this.checkinDate = checkinDate;
            this.location = location;
            this.who_has = who_has;
            this.password = password;
        }

        checkOut(who_has, location) {
            this.status = "OUT";
            this.who_has = who_has;
            this.location = location;
        }

        checkIn(model, serial) {
            this.model = model;
            this.serial = serial;
            this.status = "IN";
        }
    }

    class Worker {
        constructor(id, cameras, items) {
            this.id = id;
            this.cameras = [cameras];
            this.items = [items];
        }

        addCamera(camera) {
            this.cameras.push(camera);
        }
    }

    const addCameraToInventory = (camera) => {

    }

    const getCameraFromInventroy = (camera) => {

    }

    let james = new Worker(1, cameraList[0]);
    james.addCamera(cameraList[1]);
    console.log(james);
    res.render('inventory', { cameraList });
});

// Make software_modules archetype
// Make testing_status archetype
// Make info links
app.listen(1337, (req, res) => console.log('listening on 1337'));