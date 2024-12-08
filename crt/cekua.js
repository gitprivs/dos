const fs = require('fs');
const https = require('https');

// Membaca file ua.txt
fs.readFile('ua.txt', 'utf8', (err, data) => {
    if (err) {
        console.error(err);
        return;
    }

    const userAgents = data.split('\n').filter(ua => ua.trim() !== ''); // Memisahkan setiap baris user agent
    let liveCount = 0;
    let deadCount = 0;

    userAgents.forEach(ua => {
        const options = {
            headers: {
                'User-Agent': ua
            },
            timeout: 5000 // Timeout dalam milidetik
        };

        const req = https.request('https://www.example.com', options, (res) => {
            console.log(`User agent ${ua} hidup.`);
            liveCount++;
        });

        req.on('error', (err) => {
            console.log(`User agent ${ua} mati.`);
            deadCount++;
        });

        req.end();
    });

    console.log(`Jumlah user agents yang hidup: ${liveCount}`);
    console.log(`Jumlah user agents yang mati: ${deadCount}`);
});
