const callQueue = new Map();
const banned = new Set();

function updateCallQueue(ip, timestamp) {
    if (!callQueue.has(ip)) {
      callQueue.set(ip, [timestamp]);
    } else {
      callQueue.get(ip).push(timestamp);
    }
}


function isWithinLimit(ip, timestamp, maxRequests, timeInterval) {
    updateCallQueue(ip, timestamp);
    const calls = callQueue.get(ip);
    const cutoff = timestamp - timeInterval;
    const arr = []
    for (let call of calls) {
        if (call >= cutoff) {
            arr.push(call);
        }
    }
    
    if (arr.length > maxRequests) {
      return false;
    } else {
      return true;
    }
  }

function antifraud(originalFunction, timeInterval, maxRequests) {
    return function(ip, timestamp, ...args) {
        if (banned.has(ip)) {
            return undefined;
        }
        if (!isWithinLimit(ip, timestamp, maxRequests, timeInterval)) {
            banned.add(ip)
            return undefined;
        }
        return originalFunction(...args);
    }
  }

function sendSMS(phoneNumber, message) {
  // код отправки SMS
  console.log(`Отправлено SMS "${message}"`)
}

const protectedFunction = antifraud(sendSMS, 10, 2)

protectedFunction('128.0.0.1', 0, '+7 000 000 00-00', 'Первое сообщение')
// console.log('Отправлено SMS "Первое сообщение"')

protectedFunction('128.0.0.1', 5, '+7 000 000 00-00', 'Второе сообщение')
// console.log('Отправлено SMS "Второе сообщение"')

protectedFunction('128.0.0.1', 10, '+7 000 000 00-00', 'Третье сообщение')
// ничего не произошло, IP 128.0.0.1 отправился в бан

protectedFunction('128.0.0.1', 15, '+7 000 000 00-00', 'Третье сообщение')

protectedFunction('128.0.0.2', 20, '+7 000 000 00-00', 'Третье сообщение')
// ничего не произошло, IP 128.0.0.1 отправился в бан

protectedFunction('128.0.0.2', 40, '+7 000 000 00-00', 'gdjwjwhflkh сообщение')