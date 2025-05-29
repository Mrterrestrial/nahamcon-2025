(async () => {
  const TOTAL = 2_000_000;
  const CHUNK = 50_000;    
  const proto = location.protocol === 'https:' ? 'wss:' : 'ws:';
  const ws    = new WebSocket(proto + '//' + location.host + '/ws');
  await new Promise(r => ws.addEventListener('open', r));

  // ask for the current checked list
  const checked = await new Promise(resolve => {
    ws.addEventListener('message', ev => {
      const data = JSON.parse(ev.data);
      if (data.checked) {
        // decode+inflate exactly like the client
        const raw  = atob(data.checked);
        const buf  = new Uint8Array(raw.length);
        for (let i = 0; i < raw.length; i++) buf[i] = raw.charCodeAt(i);
        const json = pako.inflate(buf, { to: 'string' });
        resolve(new Set(JSON.parse(json)));
      }
    });
    ws.send(JSON.stringify({ action: 'get_state' }));
  });

  // build an array of just the missing indexes
  const missing = [];
  for (let i = 0; i < TOTAL; i++) {
    if (!checked.has(i)) missing.push(i);
  }

  // send them in chunks
  for (let i = 0; i < missing.length; i += CHUNK) {
    const slice = missing.slice(i, i + CHUNK);
    ws.send(JSON.stringify({ action: 'check', numbers: slice }));
    // small delay so the server can keep up
    await new Promise(r => setTimeout(r, 100));
  }
})();