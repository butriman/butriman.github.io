const puppeteer = require('puppeteer');

(async () => {
  const browser = await puppeteer.launch();
  const page = await browser.newPage();
  await page.goto('YOUR_HTML_PAGE_URL', {waitUntil: 'networkidle2'}); // Replace YOUR_HTML_PAGE_URL with your page URL
  await page.pdf({path: 'output.pdf', format: 'A4'});
  await browser.close();
})();
