// Walk-up Stairs

function stairs(n) {
  let res = [];
  const range = (start, end) => (
    (end > start)
      ? [...Array((end - start + 1)).keys()].map((k) => ((k + start)%10).toString())
      : [...Array((start - end + 1)).keys()].map((k) => ((k + end)%10).toString()).reverse()
  );
  
  for (i = 1; i <= n; i++) {
    const s = ' '.repeat(n*4 - i*4) + range(1, i).join(' ') + ' ' + range(i, 1).join(' ');
    res.push(s);
  }
  
    return res.join('\n');
}