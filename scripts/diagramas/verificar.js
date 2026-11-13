// Verifica legibilidade dos SVGs: texto fora das caixas do HTA, textos sobrepostos
// e texto passando da borda. Opcionalmente salva um PNG de cada arquivo.
// Uso: node verificar.js arquivo1.svg [arquivo2.svg ...] [--png pasta]
// Requer Node.js e Playwright com Chromium (npm i playwright && npx playwright install chromium).
const { chromium } = require('playwright');
const fs = require('fs');
const path = require('path');

(async () => {
  const args = process.argv.slice(2);
  const i = args.indexOf('--png');
  const pngDir = i >= 0 ? args.splice(i, 2)[1] : null;
  const browser = await chromium.launch();
  const page = await browser.newPage();
  let falhas = 0;
  for (const f of args) {
    const svg = fs.readFileSync(f, 'utf8');
    const m = svg.match(/viewBox="0 (-?\d+(?:\.\d+)?) (\d+) (\d+(?:\.\d+)?)"/);
    await page.setViewportSize({ width: +m[2], height: Math.ceil(+m[3]) });
    await page.goto('file://' + path.resolve(f));
    const issues = await page.evaluate(() => {
      const out = [];
      document.querySelectorAll('g[data-box]').forEach(g => {
        const rc = g.querySelector('.frame').getBBox();
        g.querySelectorAll('text').forEach(t => {
          const b = t.getBBox();
          if (b.x < rc.x + 4 || b.x + b.width > rc.x + rc.width - 4 || b.y < rc.y || b.y + b.height > rc.y + rc.height)
            out.push('fora da caixa: ' + t.textContent);
        });
      });
      const ts = [...document.querySelectorAll('text')].map(t => ({ s: t.textContent, b: t.getBBox() }));
      for (let a = 0; a < ts.length; a++) for (let c = a + 1; c < ts.length; c++) {
        const p = ts[a].b, q = ts[c].b;
        if (p.x < q.x + q.width && q.x < p.x + p.width && p.y < q.y + q.height && q.y < p.y + p.height)
          out.push('sobreposição: ' + ts[a].s + ' | ' + ts[c].s);
      }
      const W = document.documentElement.viewBox.baseVal.width;
      ts.forEach(t => { if (t.b.x < 0 || t.b.x + t.b.width > W - 20) out.push('passa da borda: ' + t.s); });
      return out;
    });
    console.log((issues.length ? 'PROBLEMA ' : 'OK       ') + path.basename(f));
    issues.forEach(s => console.log('   - ' + s));
    falhas += issues.length;
    if (pngDir) await page.screenshot({ path: path.join(pngDir, path.basename(f, '.svg') + '.png') });
  }
  await browser.close();
  process.exit(falhas ? 1 : 0);
})();
