/*
    Desc.: This program generates membership receipts for the St. John's Marina & Yacht Club
    Author: Joseph Gallant
    Dates: Nov. 15 2024 - Nov. 24 2024
*/

// Define the constants
const CURR_DATE = new Date();
const EVEN_SITE_COST = 80.0;
const ODD_SITE_COST = 120.0;
const ALT_MEM_COST = 5.0;
const SITE_CLEANING_COST = 50.0;
const VID_SURVEIL_COST = 35.0;
const STD_MEM_COST = 75.0;
const EXEC_MEM_COST = 150.0;
const YEARLY_PROC_FEE = 59.99;
const HST_RATE = 0.15;
const HST_REG_NO = "549-33-5849-47";

const CUR_2_FORMAT = new Intl.NumberFormat("en-CA", {
  style: "currency",
  currency: "CAD",
  minimumFractionDigits: "2",
  maximumFractionDigits: "2",
});

// Gather user data
let siteNum = parseInt(prompt("Enter the site number (1-100): "));
let firstName = prompt("Enter the first name:");
let lastName = prompt("Enter the last name:");
let strAddress = prompt("Enter the street address:");
let city = prompt("Enter the city:");
let prov = prompt("Enter the province (XX):").toUpperCase();
let postCode = prompt("Enter the postal code (X#X#X#):").toUpperCase();
let homePh = prompt("Enter the home phone number (##########):").toString();
let cellPh = prompt("Enter the cell phone number: (##########)").toString();
let memType = prompt(
  "Enter the membership type (S = Standard, E = Executive):"
).toUpperCase();
let numAltMem = parseInt(prompt("Enter the number of alternate members:"));
let wklySiteClean = prompt("Weekly site cleaning (Y/N)?").toUpperCase();
let vidSurveil = prompt("Video surveillance (Y/N)?").toUpperCase();

//  Calculate the site charge including the number of alternate members
let siteChrg = EVEN_SITE_COST;

if (siteNum % 2 != 0) {
  siteChrg = ODD_SITE_COST;
}

siteChrg += numAltMem * ALT_MEM_COST;

/*  Calculate the weekly site cleaning charge and assign a string value to
    display ("Yes" or "No") */

let siteCleanChrg = 0.0;
let wklySiteCleanStr = "Yes";

if (wklySiteClean == "Y") {
  siteCleanChrg = SITE_CLEANING_COST;
} else {
  siteCleanChrg = 0.0;
  wklySiteCleanStr = "No";
}

/*  Calculate the the video surveillance charge and assign a string value to
    display ("Yes" or "No") */

let vidSurveilChrg = 0.0;
let vidSurveilStr = "Yes";

if (vidSurveil == "Y") {
  vidSurveilChrg = VID_SURVEIL_COST;
} else {
  vidSurveilStr = "No";
}

// Calculate the extra charges
let extraChrg = siteCleanChrg + vidSurveilChrg;

// Calculate the subtotal and HST, and the total monthly charges
let subTot = siteChrg + extraChrg;
let hst = subTot * HST_RATE;

let totMonthlyChrg = subTot + hst;

/*  Calculate the monthly dues from the member type and assign a string value to 
    display for the member type */

let monthlyDues = STD_MEM_COST;
let memTypeStr = "Standard";

if (memType == "E") {
  monthlyDues = EXEC_MEM_COST;
  memTypeStr = "Executive";
}

// Calculate the total monthly fees
let totMonthlyFees = totMonthlyChrg + monthlyDues;

// Calculate the total yearly fees
let totYearlyFees = totMonthlyFees * 12;

// Calculate the monthly payment
let monthlyPayment = (totYearlyFees + YEARLY_PROC_FEE) / 12;

// Calculate the cancellation fee
let cancelFee = 12 * siteChrg * 0.6;

// Table for the receipt
document.write("<table class='marinayatchtable'>");

// Header
document.write(
  "<tr><th colspan='2'><br />St John's Marina & Yatch Club<br />Yearly Member Receipt<br /><br /></th></tr>"
);

// Client details
document.write(
  "<tr><td colspan='2'><br />Client Name and Address:<br /><br /></td></tr>"
);
document.write("<tr><td colspan='2'>" + firstName + " " + lastName + "<br />");
document.write(strAddress + "<br />");
document.write(city + ", " + prov + " " + postCode + "<br /><br /><br />");

// SubSection for phone number
document.write("<table class='phonetable'>");
document.write("<tr><td>Phone:</td><td>" + homePh + " (H)</td>");
document.write("<tr><td></td><td>" + cellPh + " (C)</td>");
document.write("</table>");
document.write("</td></tr>");

document.write(
  "<tr><td>Site #: " +
    siteNum +
    "</td><td class='textalignright'>Member Type: " +
    memTypeStr +
    "</td></tr>"
);

document.write(
  "<tr><td>Alternate members:<br />Weekly site cleaning:<br />Video surveillance:</td><td class='textalignright'>" +
    numAltMem +
    "<br />" +
    wklySiteCleanStr +
    "<br />" +
    vidSurveilStr +
    "</td></tr>"
);

document.write(
  "<tr><td>Site charges:<br />Extra charges:</td><td class='textalignright'>" +
    CUR_2_FORMAT.format(siteChrg) +
    "<br />" +
    CUR_2_FORMAT.format(extraChrg) +
    "</td></tr>"
);

document.write(
  "<tr><td>Subtotal:<br />Sales tax (HST):</td><td class='textalignright'>" +
    CUR_2_FORMAT.format(subTot) +
    "<br />" +
    CUR_2_FORMAT.format(hst) +
    "</td></tr>"
);

document.write(
  "<tr><td>Total monthly charges:<br />Monthly dues:</td><td class='textalignright'>" +
    CUR_2_FORMAT.format(totMonthlyChrg) +
    "<br />" +
    CUR_2_FORMAT.format(monthlyDues) +
    "</td></tr>"
);

document.write(
  "<tr><td>Total monthly fees:<br />Total yearly fees:</td><td class='textalignright'>" +
    CUR_2_FORMAT.format(totMonthlyFees) +
    "<br />" +
    CUR_2_FORMAT.format(totYearlyFees) +
    "</td></tr>"
);

document.write(
  "<tr><td>Monthly payment:</td><td class='textalignright'>" +
    CUR_2_FORMAT.format(monthlyPayment) +
    "</td></tr>"
);

document.write(
  "<tr><td>Issued:<br /><br />HST Reg No:<br /><br />Cancellation fee:</td><td class='textalignright'>" +
    CURR_DATE.getFullYear() +
    "-" +
    CURR_DATE.getMonth() +
    "-" +
    CURR_DATE.getDate() +
    "<br /><br />" +
    HST_REG_NO +
    "<br /><br />" +
    CUR_2_FORMAT.format(cancelFee) +
    "</td></tr>"
);

document.write("</table>");
