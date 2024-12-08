const fs = require('fs');
const randomUseragent = require('random-useragent');
const readlineSync = require('readline-sync');

function generateua(count) {
    const userAgents = [];

    for (let i = 0; i < count; i++) {
        const userAgent = randomUseragent.getRandom();
        userAgents.push(userAgent);
    }

    return userAgents;
}

function saveniga(userAgents) {
    const saved = 'ua.txt';

    fs.writeFile(saved, userAgents.join('\n'), (err) => {
        if (err) throw err;
        console.log(`Succes create user-agents | saved to ${saved}`);
    });
}

const rvlnd = generateua(Number(10000));
saveniga(rvlnd);