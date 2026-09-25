// Renders build/pdf.html to portfolio.pdf with headless Chromium (Playwright).
// Internal <a href="#id"> links become clickable links inside the PDF.
const path = require('path');
let chromium;
try { ({ chromium } = require('playwright')); } catch (e) { ({ chromium } = require(process.env.PWPATH)); }

(async () => {
  const root = path.resolve(__dirname, '..');
  const browser = await chromium.launch();
  const page = await browser.newPage();
  await page.goto('file://' + path.join(root, 'build', 'pdf.html'));
  await page.evaluate(() => document.fonts.ready);
  await page.pdf({ path: path.join(root, 'portfolio.pdf'), width: '1280px', height: '720px', printBackground: true, preferCSSPageSize: true });
  await browser.close();
  console.log('wrote portfolio.pdf');
})();
