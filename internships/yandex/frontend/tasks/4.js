// const payments = function (timesheet, hourRate) {

//     function payMode(hour) {
//         if (hour >= 8 && hour < 18) {
//             return 1
//         } else if (eventHour >= 18 && eventHour < 23) {
//             return 1.5
//         } else {
//             return 2
//         }
//     }
  
//     let totalPay = 0;
//     let lastEvent = null;
//     let lastEventTime = null;
  
//     for (let [event, time] of timesheet) {

//       const eventTime = new Date(time).getTime();
//       const eventHour = new Date(eventTime).getUTCHours();
  
//       if (lastEvent && event === "logout") {
//             const hoursWorked = Math.floor((eventTime - lastEventTime) / 3600000);
//             const lastEventHour = new Date(lastEventTime).getUTCHours();

//             for (let i = )
  
//             if (eventHour >= 8 && eventHour < 18) {
//                 totalPay += hoursWorked * hourRate;
//             } else if (eventHour >= 18 && eventHour < 23) {
//                 totalPay += hoursWorked * hourRate * 1.5;
//             } else {
//                 totalPay += hoursWorked * hourRate * 2;
//             }
//       }
  
//         lastEvent = event;
//         lastEventTime = eventTime;
//     }
  
//     return totalPay.toFixed(2);
// };

const payments = function calculateSalary(timesheet, hourRate) {

    function rate(h) {
      if (h >= 8 && h < 18) {
        return 1
      } else if (h >= 18 && h < 23) {
        return 1.5
      } else {
        return 2
      }
    }

    let salary = 0;

    let start = new Date(timesheet[0][1]).getUTCHours();
    let end = new Date(timesheet[1][1]).getUTCHours();
  
    if (start <= end) {
      for (let i = start; i <= end; i++) {
        salary += hourRate * rate(i);
      }
    } else {
      for (let i = start; i <= end + 24; i++) {
        const h = i >= 24 ? i - 24 : i
        salary += hourRate * rate(h);
      }
    }

  
    // salary += duration * hourRate * rate;
  
    return salary.toFixed(2);
}


const timesheet = [['login', 1669914900000], ['logout', 1669914900000 + 3*3600000 + 1]];
const hourRate = 51;
console.log(payments(timesheet, hourRate));


module.exports = function (timesheet, hourRate) {
  let totalHours = 0;
  let regularHours = 0;
  let peakHours = 0;
  let offPeakHours = 0;

  for (let i = 0; i < timesheet.length; i += 2) {
    const loginTime = new Date(timesheet[i][1]);
    const logoutTime = new Date(timesheet[i + 1][1]);

    const shiftDuration = (logoutTime - loginTime) / 3600000;

    totalHours += shiftDuration;

    if (loginTime.getUTCHours() >= 8 && logoutTime.getUTCHours() <= 18) {
      regularHours += shiftDuration;
    } else if (loginTime.getUTCHours() >= 18 && logoutTime.getUTCHours() <= 23) {
      peakHours += shiftDuration;
    } else {
      offPeakHours += shiftDuration;
    }
  }

  const totalPay = regularHours * hourRate + peakHours * hourRate * 1.5 + offPeakHours * hourRate * 2;

  return parseFloat(totalPay.toFixed(2));
};